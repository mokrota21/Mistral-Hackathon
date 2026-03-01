/* ── AInki PDF Reader ── */

import * as pdfjsLib from 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/4.0.379/pdf.min.mjs';

pdfjsLib.GlobalWorkerOptions.workerSrc =
    'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/4.0.379/pdf.worker.min.mjs';

const API = '/api';

// ── Extract book name from URL ──
const pathParts = window.location.pathname.split('/reader/');
const bookName = decodeURIComponent(pathParts[1] || '');

if (!bookName) {
    alert('No book specified');
    window.location = '/';
}

// ── State ──
let pdfDoc = null;
let currentPage = 1;
let totalPages = 0;
let rendering = false;
let pagesVisited = new Set();
let answeredCount = 0;
let sessionStartTime = Date.now();
let masteryData = [];
let currentQuestion = null;
let knowledgeMode = 'grouped'; // 'grouped' or 'raw'
let currentProvider = 'mistral'; // active LLM provider

// Zoom state
let userZoom = 2.0; // default 2x zoom
const ZOOM_MIN = 0.5;
const ZOOM_MAX = 5.0;
const ZOOM_STEP = 0.25;

// Q&A timer config
const POPUP_INTERVAL_MS = 3 * 60 * 1000; // 3 minutes
let popupTimerInterval = null;
let nextPopupTime = Date.now() + POPUP_INTERVAL_MS;
let timerPaused = false;

// ── DOM refs ──
const canvas = document.getElementById('pdf-canvas');
const ctx = canvas.getContext('2d');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');
const pageInfo = document.getElementById('page-info');
const pageSlider = document.getElementById('page-slider');
const bookTitle = document.getElementById('book-title');
const progressRing = document.getElementById('progress-ring');
const progressPct = document.getElementById('progress-pct');
const progressDetail = document.getElementById('progress-detail');
const statTime = document.getElementById('stat-time');
const statPages = document.getElementById('stat-pages');
const statConcepts = document.getElementById('stat-concepts');
const statAnswered = document.getElementById('stat-answered');
const masteryBar = document.getElementById('mastery-bar');
const knowledgeToggle = document.getElementById('knowledge-toggle');
const knowledgeList = document.getElementById('knowledge-list');
const sessionTimerEl = document.getElementById('session-timer');
const nextQuestionBadge = document.getElementById('next-question-badge');
const qaOverlay = document.getElementById('qa-overlay');
const qaTopic = document.getElementById('qa-topic');
const qaQuestion = document.getElementById('qa-question');
const qaAnswer = document.getElementById('qa-answer');
const qaSubmit = document.getElementById('qa-submit');
const qaSkip = document.getElementById('qa-skip');
const qaFeedback = document.getElementById('qa-feedback');
const qaModal = document.getElementById('qa-modal');

const zoomInBtn = document.getElementById('zoom-in-btn');
const zoomOutBtn = document.getElementById('zoom-out-btn');
const zoomFitBtn = document.getElementById('zoom-fit-btn');
const zoomLevel = document.getElementById('zoom-level');
const providerSelect = document.getElementById('provider-select');
const rerunBtn = document.getElementById('rerun-btn');

// ── Zoom controls ──
function updateZoomDisplay() {
    zoomLevel.textContent = Math.round(userZoom * 100) + '%';
    zoomOutBtn.disabled = userZoom <= ZOOM_MIN;
    zoomInBtn.disabled = userZoom >= ZOOM_MAX;
}

function zoomIn() {
    userZoom = Math.min(userZoom + ZOOM_STEP, ZOOM_MAX);
    updateZoomDisplay();
    renderPage(currentPage);
}

function zoomOut() {
    userZoom = Math.min(Math.max(userZoom - ZOOM_STEP, ZOOM_MIN), ZOOM_MAX);
    updateZoomDisplay();
    renderPage(currentPage);
}

async function zoomFit() {
    if (!pdfDoc) return;
    const page = await pdfDoc.getPage(currentPage);
    const container = document.getElementById('canvas-container');
    const containerWidth = container.clientWidth - 32;
    const containerHeight = container.clientHeight - 32;
    const unscaledViewport = page.getViewport({ scale: 1.0 });
    const scaleW = containerWidth / unscaledViewport.width;
    const scaleH = containerHeight / unscaledViewport.height;
    userZoom = Math.min(scaleW, scaleH);
    updateZoomDisplay();
    renderPage(currentPage);
}

// ── Toast ──
function showToast(message, type = 'info') {
    const container = document.getElementById('toast-container');
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    container.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transition = 'opacity 0.3s';
        setTimeout(() => toast.remove(), 300);
    }, 3500);
}

// ── Format time ──
function formatTime(ms) {
    const s = Math.floor(ms / 1000);
    const m = Math.floor(s / 60);
    const sec = s % 60;
    return `${m}:${sec.toString().padStart(2, '0')}`;
}

// ══════════════════════════════
//  PDF RENDERING
// ══════════════════════════════

async function renderPage(pageNum) {
    if (rendering) return;
    rendering = true;

    try {
        const page = await pdfDoc.getPage(pageNum);

        const viewport = page.getViewport({ scale: userZoom });

        // Use device pixel ratio for sharp rendering
        const dpr = window.devicePixelRatio || 1;
        canvas.width = viewport.width * dpr;
        canvas.height = viewport.height * dpr;
        canvas.style.width = viewport.width + 'px';
        canvas.style.height = viewport.height + 'px';

        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

        await page.render({ canvasContext: ctx, viewport }).promise;
    } catch (e) {
        console.error('Render error:', e);
    } finally {
        rendering = false;
    }
}

function goToPage(pageNum) {
    if (pageNum < 1 || pageNum > totalPages || pageNum === currentPage) return;
    currentPage = pageNum;
    pagesVisited.add(pageNum);
    updateUI();
    renderPage(currentPage);
    loadNearbyKnowledge();
}

function updateUI() {
    // Page info
    pageInfo.textContent = `${currentPage} / ${totalPages}`;
    pageSlider.value = currentPage;
    prevBtn.disabled = currentPage <= 1;
    nextBtn.disabled = currentPage >= totalPages;

    // Progress
    const pct = Math.round((currentPage / totalPages) * 100);
    progressPct.textContent = `${pct}%`;
    progressDetail.textContent = `Page ${currentPage} of ${totalPages}`;
    const circumference = 2 * Math.PI * 30; // r=30
    progressRing.style.strokeDashoffset = circumference - (pct / 100) * circumference;

    // Stats
    statPages.textContent = pagesVisited.size;
    statAnswered.textContent = answeredCount;

    // Mastery bar: highlight current
    masteryBar.querySelectorAll('.mastery-segment').forEach((seg, i) => {
        seg.classList.toggle('current', i + 1 === currentPage);
    });
}

// ══════════════════════════════
//  MASTERY SIDEBAR
// ══════════════════════════════

async function loadMastery() {
    try {
        const res = await fetch(`${API}/books/${encodeURIComponent(bookName)}/mastery`);
        if (!res.ok) return;
        const data = await res.json();
        masteryData = data.mastery;
        renderMasteryBar();
    } catch (e) {
        console.error('Mastery load error:', e);
    }
}

function renderMasteryBar() {
    masteryBar.innerHTML = '';
    masteryData.forEach((item, i) => {
        const seg = document.createElement('div');
        seg.className = 'mastery-segment';
        if (i + 1 === currentPage) seg.classList.add('current');

        // Color by score
        const score = item.score;
        let color;
        if (score > 0.7) color = '#10B981';      // green
        else if (score > 0.4) color = '#F59E0B';  // yellow
        else color = '#EF4444';                    // red

        seg.style.background = color;
        seg.title = `Page ${i + 1}: ${Math.round(score * 100)}% mastery`;

        seg.addEventListener('click', () => goToPage(i + 1));
        masteryBar.appendChild(seg);
    });
}

// ══════════════════════════════
//  KNOWLEDGE LIST (sidebar)
// ══════════════════════════════

async function loadNearbyKnowledge() {
    try {
        const res = await fetch(
            `${API}/books/${encodeURIComponent(bookName)}/knowledge?page=${currentPage - 1}&limit=20&mode=${knowledgeMode}&provider=${encodeURIComponent(currentProvider)}`
        );
        if (!res.ok) return;
        const data = await res.json();

        knowledgeList.innerHTML = '';

        // Grouped mode: render clusters
        if (data.mode === 'grouped' && data.clusters && data.clusters.length > 0) {
            statConcepts.textContent = data.clusters.length;

            data.clusters.forEach(cluster => {
                const item = document.createElement('div');
                item.className = 'knowledge-item knowledge-cluster';
                const qCount = cluster.question_count || cluster.questions.length;
                item.innerHTML = `
                    <div class="knowledge-item-topic">
                        ${cluster.cluster_name}
                        <span class="knowledge-item-count">${qCount} Q</span>
                    </div>
                    <div class="knowledge-cluster-questions" style="display:none">
                        ${cluster.questions.map(q => `<div class="knowledge-cluster-q">${q}</div>`).join('')}
                    </div>
                `;
                // Click to expand/collapse questions
                item.addEventListener('click', () => {
                    const qList = item.querySelector('.knowledge-cluster-questions');
                    const isOpen = qList.style.display !== 'none';
                    qList.style.display = isOpen ? 'none' : 'block';
                    item.classList.toggle('expanded', !isOpen);
                });
                knowledgeList.appendChild(item);
            });
            return;
        }

        // Raw mode: render individual questions
        if (data.questions && data.questions.length > 0) {
            statConcepts.textContent = data.questions.length;

            data.questions.forEach(q => {
                const item = document.createElement('div');
                item.className = 'knowledge-item';
                item.innerHTML = `
                    <div class="knowledge-item-topic">${q.knowledge_object}</div>
                    <div class="knowledge-item-question">${q.question}</div>
                `;
                knowledgeList.appendChild(item);
            });
            return;
        }

        // No data
        statConcepts.textContent = 0;
        knowledgeList.innerHTML = '<div style="font-size:0.8rem;color:var(--text-muted);padding:8px">No concepts extracted for this area yet.</div>';
    } catch (e) {
        console.error('Knowledge load error:', e);
    }
}

// ══════════════════════════════
//  Q&A POPUP SYSTEM
// ══════════════════════════════

async function fetchQuestion() {
    try {
        const res = await fetch(
            `${API}/books/${encodeURIComponent(bookName)}/knowledge?page=${currentPage - 1}&limit=20&mode=${knowledgeMode}&provider=${encodeURIComponent(currentProvider)}`
        );
        if (!res.ok) return null;
        const data = await res.json();

        // Grouped mode: pick random cluster, then random question from it
        if (data.mode === 'grouped' && data.clusters && data.clusters.length > 0) {
            const cluster = data.clusters[Math.floor(Math.random() * data.clusters.length)];
            const question = cluster.questions[Math.floor(Math.random() * cluster.questions.length)];
            return {
                question: question,
                knowledge_object: cluster.cluster_name,
                reference: cluster.references ? Math.min(...cluster.references) : 0,
            };
        }

        // Raw mode: pick from questions
        if (data.questions && data.questions.length > 0) {
            return data.questions[Math.floor(Math.random() * data.questions.length)];
        }

        return null;
    } catch (e) {
        return null;
    }
}

function showQuestionPopup(question) {
    currentQuestion = question;
    timerPaused = true;

    qaTopic.textContent = question.knowledge_object;
    qaQuestion.textContent = question.question;
    qaAnswer.value = '';
    qaFeedback.style.display = 'none';
    qaAnswer.style.display = '';
    document.querySelector('.qa-actions').style.display = '';

    qaOverlay.classList.add('active');
    setTimeout(() => qaAnswer.focus(), 100);
}

function dismissPopup() {
    qaOverlay.classList.remove('active');
    currentQuestion = null;
    timerPaused = false;
    nextPopupTime = Date.now() + POPUP_INTERVAL_MS;
}

async function submitAnswer() {
    if (!currentQuestion) return;
    const answer = qaAnswer.value.trim();
    if (!answer) {
        qaAnswer.style.borderColor = 'var(--error)';
        return;
    }

    try {
        await fetch(`${API}/books/${encodeURIComponent(bookName)}/answers`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                question: currentQuestion.question,
                knowledge_object: currentQuestion.knowledge_object,
                user_answer: answer,
                page: currentPage - 1,
            }),
        });
    } catch (e) {
        // ignore errors for dummy endpoint
    }

    answeredCount++;
    statAnswered.textContent = answeredCount;

    // Show feedback
    qaAnswer.style.display = 'none';
    document.querySelector('.qa-actions').style.display = 'none';
    qaFeedback.textContent = 'Answer recorded! Keep reading.';
    qaFeedback.style.display = 'block';

    setTimeout(dismissPopup, 1500);
}

function startPopupTimer() {
    nextPopupTime = Date.now() + POPUP_INTERVAL_MS;

    popupTimerInterval = setInterval(async () => {
        if (timerPaused) return;

        if (Date.now() >= nextPopupTime) {
            const q = await fetchQuestion();
            if (q) {
                showQuestionPopup(q);
            } else {
                // No questions available, try again later
                nextPopupTime = Date.now() + POPUP_INTERVAL_MS;
            }
        }
    }, 1000);
}

// ══════════════════════════════
//  SESSION TIMER
// ══════════════════════════════

function startSessionTimer() {
    setInterval(() => {
        const elapsed = Date.now() - sessionStartTime;
        const timeStr = formatTime(elapsed);
        sessionTimerEl.innerHTML = `&#128337; ${timeStr}`;
        statTime.textContent = timeStr;

        // Update next-question countdown
        if (!timerPaused) {
            const remaining = Math.max(0, nextPopupTime - Date.now());
            nextQuestionBadge.textContent = `Next Q in ${formatTime(remaining)}`;
        } else {
            nextQuestionBadge.textContent = 'Answering...';
        }
    }, 1000);
}

// ══════════════════════════════
//  KNOWLEDGE TOGGLE
// ══════════════════════════════

knowledgeToggle.addEventListener('click', () => {
    knowledgeToggle.classList.toggle('expanded');
    knowledgeList.classList.toggle('expanded');
});

// ══════════════════════════════
//  RERUN KNOWLEDGE EXTRACTION
// ══════════════════════════════

async function rerunKnowledge() {
    const provider = providerSelect.value;
    if (!confirm(`Rerun knowledge extraction using "${provider}" provider?\n\nThis will extract new Q&A pairs from the book using the selected LLM.`)) {
        return;
    }

    rerunBtn.disabled = true;
    rerunBtn.textContent = '⏳ Running...';

    try {
        const res = await fetch(`${API}/books/${encodeURIComponent(bookName)}/rerun`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ provider }),
        });

        if (!res.ok) {
            const err = await res.json();
            showToast(err.detail || 'Rerun failed', 'error');
            rerunBtn.disabled = false;
            rerunBtn.textContent = '↻ Rerun';
            return;
        }

        showToast(`Knowledge extraction started (${provider})`, 'success');

        // Poll for completion
        pollRerunStatus();
    } catch (e) {
        showToast('Failed to start rerun', 'error');
        rerunBtn.disabled = false;
        rerunBtn.textContent = '↻ Rerun';
    }
}

function pollRerunStatus() {
    const interval = setInterval(async () => {
        try {
            const res = await fetch(`${API}/books/${encodeURIComponent(bookName)}/status`);
            if (!res.ok) return;
            const data = await res.json();

            if (data.status === 'rerunning' || data.status === 'analyzing') {
                rerunBtn.textContent = '⏳ Running...';
            } else if (data.status === 'ready') {
                clearInterval(interval);
                rerunBtn.disabled = false;
                rerunBtn.textContent = '↻ Rerun';
                showToast('Knowledge extraction complete!', 'success');
                // Reload knowledge with new provider data
                loadNearbyKnowledge();
            } else if (data.status === 'error') {
                clearInterval(interval);
                rerunBtn.disabled = false;
                rerunBtn.textContent = '↻ Rerun';
                showToast(`Rerun failed: ${data.error_message || 'Unknown error'}`, 'error');
            }
        } catch (e) {
            // ignore polling errors
        }
    }, 3000);
}

// ══════════════════════════════
//  INITIALIZATION
// ══════════════════════════════

async function init() {
    bookTitle.textContent = bookName.replace('.pdf', '');
    document.title = `AInki - ${bookName.replace('.pdf', '')}`;

    // Load PDF
    try {
        const loadingTask = pdfjsLib.getDocument(`${API}/pdfs/${encodeURIComponent(bookName)}`);
        pdfDoc = await loadingTask.promise;
        totalPages = pdfDoc.numPages;

        pageSlider.max = totalPages;
        pageSlider.value = 1;
        currentPage = 1;
        pagesVisited.add(1);

        await renderPage(1);
        updateUI();
    } catch (e) {
        console.error('PDF load error:', e);
        showToast('Failed to load PDF', 'error');
        return;
    }

    // Load book metadata and populate provider dropdown
    try {
        const pagesRes = await fetch(`${API}/books/${encodeURIComponent(bookName)}/pages`);
        if (pagesRes.ok) {
            const pagesData = await pagesRes.json();
            const availableProviders = pagesData.available_providers || ['mistral'];
            const providersWithData = pagesData.providers_with_data || [];
            const defaultProvider = pagesData.default_provider || 'mistral';

            // Populate dropdown
            providerSelect.innerHTML = '';
            availableProviders.forEach(prov => {
                const opt = document.createElement('option');
                opt.value = prov;
                opt.textContent = prov;
                // Mark providers that have data
                if (!providersWithData.includes(prov)) {
                    opt.textContent += ' (no data)';
                }
                providerSelect.appendChild(opt);
            });

            // Select first provider that has data, or the default
            if (providersWithData.length > 0) {
                currentProvider = providersWithData.includes(defaultProvider)
                    ? defaultProvider
                    : providersWithData[0];
            } else {
                currentProvider = defaultProvider;
            }
            providerSelect.value = currentProvider;
        }
    } catch (e) {
        console.error('Pages metadata load error:', e);
    }

    // Provider change handler
    providerSelect.addEventListener('change', () => {
        currentProvider = providerSelect.value;
        loadNearbyKnowledge();
    });

    // Rerun button
    rerunBtn.addEventListener('click', rerunKnowledge);

    // Load mastery data
    loadMastery();

    // Load nearby knowledge
    loadNearbyKnowledge();

    // Start timers
    startSessionTimer();
    startPopupTimer();

    // ── Navigation event listeners ──
    prevBtn.addEventListener('click', () => goToPage(currentPage - 1));
    nextBtn.addEventListener('click', () => goToPage(currentPage + 1));

    pageSlider.addEventListener('input', () => {
        const val = parseInt(pageSlider.value, 10);
        pageInfo.textContent = `${val} / ${totalPages}`;
    });
    pageSlider.addEventListener('change', () => {
        goToPage(parseInt(pageSlider.value, 10));
    });

    // Knowledge mode toggle
    const modeGroupedBtn = document.getElementById('mode-grouped');
    const modeRawBtn = document.getElementById('mode-raw');

    function setKnowledgeMode(mode) {
        knowledgeMode = mode;
        modeGroupedBtn.classList.toggle('active', mode === 'grouped');
        modeRawBtn.classList.toggle('active', mode === 'raw');
        // Reload knowledge for current page
        loadNearbyKnowledge();
    }
    modeGroupedBtn.addEventListener('click', () => setKnowledgeMode('grouped'));
    modeRawBtn.addEventListener('click', () => setKnowledgeMode('raw'));

    // Zoom controls
    zoomInBtn.addEventListener('click', zoomIn);
    zoomOutBtn.addEventListener('click', zoomOut);
    zoomFitBtn.addEventListener('click', zoomFit);
    updateZoomDisplay();

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (qaOverlay.classList.contains('active')) return; // don't navigate while popup open
        if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
            e.preventDefault();
            goToPage(currentPage - 1);
        } else if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
            e.preventDefault();
            goToPage(currentPage + 1);
        } else if ((e.key === '=' || e.key === '+') && (e.ctrlKey || e.metaKey)) {
            e.preventDefault();
            zoomIn();
        } else if (e.key === '-' && (e.ctrlKey || e.metaKey)) {
            e.preventDefault();
            zoomOut();
        } else if (e.key === '0' && (e.ctrlKey || e.metaKey)) {
            e.preventDefault();
            zoomFit();
        }
    });

    // Window resize → re-render
    let resizeTimeout;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(() => renderPage(currentPage), 200);
    });

    // Q&A popup buttons
    qaSubmit.addEventListener('click', submitAnswer);
    qaSkip.addEventListener('click', dismissPopup);

    // Enter to submit in answer textarea
    qaAnswer.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && e.ctrlKey) {
            e.preventDefault();
            submitAnswer();
        }
    });
    qaAnswer.addEventListener('input', () => {
        qaAnswer.style.borderColor = '';
    });
}

init();
