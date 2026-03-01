/* ── AInki Library Page ── */

const API = '/api';
const POLL_INTERVAL = 3000;
let pollingTimers = {};

// ── Toast notifications ──

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

// ── Status helpers ──

const STATUS_LABELS = {
    uploading: 'Uploading',
    ocr_processing: 'Running OCR...',
    chunking: 'Chunking text...',
    analyzing: 'Extracting knowledge...',
    ready: 'Ready',
    error: 'Error',
};

function statusBadgeClass(status) {
    if (status === 'ready') return 'badge-ready';
    if (status === 'error') return 'badge-error';
    return 'badge-processing';
}

function isProcessing(status) {
    return ['uploading', 'ocr_processing', 'chunking', 'analyzing'].includes(status);
}

// ── Render book card ──

function renderBookCard(book) {
    const card = document.createElement('div');
    card.className = 'book-card';
    card.id = `book-${CSS.escape(book.name)}`;

    const processing = isProcessing(book.status);

    card.innerHTML = `
        <div class="book-card-header">
            <span class="book-icon">${processing ? '\uD83D\uDD04' : '\uD83D\uDCD5'}</span>
            <span class="book-title" title="${book.name}">${book.name.replace('.pdf', '')}</span>
        </div>
        <div class="book-meta">
            ${book.total_pages != null ? `<span class="book-meta-item">\uD83D\uDCC4 ${book.total_pages} pages</span>` : ''}
            ${book.total_knowledge_objects != null ? `<span class="book-meta-item">\uD83E\uDDE0 ${book.total_knowledge_objects} concepts</span>` : ''}
        </div>
        <div class="book-status-line">
            <span class="badge ${statusBadgeClass(book.status)}">
                ${processing ? '<span class="spinner"></span>' : ''}
                ${STATUS_LABELS[book.status] || book.status}
            </span>
            ${book.error_message ? `<span style="font-size:0.78rem;color:var(--error)">${book.error_message}</span>` : ''}
        </div>
        <div class="book-actions">
            ${book.status === 'ready'
                ? `<a class="btn-primary" href="/reader/${encodeURIComponent(book.name)}">Open reader</a>`
                : `<button class="btn-primary" disabled>${processing ? 'Processing...' : 'Unavailable'}</button>`
            }
        </div>
    `;

    return card;
}

// ── Poll for processing status ──

function startPolling(bookName) {
    if (pollingTimers[bookName]) return;

    pollingTimers[bookName] = setInterval(async () => {
        try {
            const res = await fetch(`${API}/books/${encodeURIComponent(bookName)}/status`);
            if (!res.ok) return;
            const book = await res.json();

            // Update card
            const grid = document.getElementById('books-grid');
            const oldCard = document.getElementById(`book-${CSS.escape(book.name)}`);
            const newCard = renderBookCard(book);
            if (oldCard) {
                grid.replaceChild(newCard, oldCard);
            }

            // Stop polling if done
            if (!isProcessing(book.status)) {
                clearInterval(pollingTimers[bookName]);
                delete pollingTimers[bookName];
                if (book.status === 'ready') {
                    showToast(`"${book.name}" is ready to read!`, 'success');
                } else if (book.status === 'error') {
                    showToast(`Error processing "${book.name}"`, 'error');
                }
            }
        } catch (e) {
            console.error('Polling error:', e);
        }
    }, POLL_INTERVAL);
}

// ── Load books ──

async function loadBooks() {
    const grid = document.getElementById('books-grid');

    try {
        const res = await fetch(`${API}/books`);
        const data = await res.json();

        if (data.books.length === 0) {
            grid.innerHTML = `
                <div class="empty-state">
                    <span class="empty-state-icon">\uD83D\uDCDA</span>
                    <div class="empty-state-text">No books yet. Upload a PDF to get started!</div>
                </div>
            `;
            return;
        }

        grid.innerHTML = '';
        data.books.forEach(book => {
            grid.appendChild(renderBookCard(book));
            if (isProcessing(book.status)) {
                startPolling(book.name);
            }
        });
    } catch (e) {
        console.error('Failed to load books:', e);
        showToast('Failed to load library', 'error');
    }
}

// ── Upload handling ──

async function uploadFile(file) {
    if (!file || !file.name.toLowerCase().endsWith('.pdf')) {
        showToast('Please select a PDF file', 'error');
        return;
    }

    const progress = document.getElementById('upload-progress');
    progress.classList.add('active');

    try {
        const form = new FormData();
        form.append('file', file);

        const res = await fetch(`${API}/books/upload`, { method: 'POST', body: form });

        if (res.status === 409) {
            showToast('This book already exists in your library', 'error');
            return;
        }
        if (!res.ok) {
            const err = await res.json();
            throw new Error(err.detail || 'Upload failed');
        }

        const data = await res.json();
        showToast(`"${data.name}" uploaded! Processing started...`, 'success');

        // Add card and start polling
        const grid = document.getElementById('books-grid');
        // Remove empty state if present
        const empty = grid.querySelector('.empty-state');
        if (empty) empty.remove();

        grid.appendChild(renderBookCard({
            name: data.name,
            status: data.status,
            total_pages: null,
            total_knowledge_objects: null,
            error_message: null,
        }));
        startPolling(data.name);

    } catch (e) {
        console.error('Upload error:', e);
        showToast(e.message || 'Upload failed', 'error');
    } finally {
        progress.classList.remove('active');
    }
}

// ── Event listeners ──

document.addEventListener('DOMContentLoaded', () => {
    loadBooks();

    const zone = document.getElementById('upload-zone');
    const fileInput = document.getElementById('file-input');

    zone.addEventListener('click', () => fileInput.click());

    zone.addEventListener('dragover', (e) => {
        e.preventDefault();
        zone.classList.add('dragover');
    });
    zone.addEventListener('dragleave', () => {
        zone.classList.remove('dragover');
    });
    zone.addEventListener('drop', (e) => {
        e.preventDefault();
        zone.classList.remove('dragover');
        const file = e.dataTransfer.files[0];
        uploadFile(file);
    });

    fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) {
            uploadFile(fileInput.files[0]);
            fileInput.value = '';
        }
    });
});
