# Remove .env from entire git history (all branches)
# Run from repo root. After running: force-push all branches and rotate any exposed secrets.

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

# filter-branch requires a clean working tree
$status = git status --porcelain
if ($status) {
    Write-Host "Stashing uncommitted changes..."
    git stash push -u -m "remove-env-from-history"
    $stashed = $true
}

$env:FILTER_BRANCH_SQUELCH_WARNING = "1"
Write-Host "Removing .env from all commits on all branches..."
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch .env" --prune-empty --tag-name-filter cat -- --all
$filterExit = $LASTEXITCODE

if ($stashed) {
    Write-Host "Restoring stashed changes..."
    git stash pop
}

if ($filterExit -eq 0) {
    Write-Host ""
    Write-Host "Done. .env has been removed from history."
    Write-Host ""
    Write-Host "IMPORTANT next steps:"
    Write-Host "1. Rotate any secrets that were in .env (API keys, etc.) - they may have been cached or copied."
    Write-Host "2. Force-push all branches to update GitHub:"
    Write-Host "   git push origin --force --all"
    Write-Host "3. If you have tags: git push origin --force --tags"
    Write-Host "4. Delete this script: Remove-Item remove-env-from-history.ps1"
} else {
    Write-Host "filter-branch failed. You can try git filter-repo instead (pip install git-filter-repo)."
}
