# Remove .env from Git history (all branches)

`.env` was pushed to GitHub. Follow one of the options below to remove it from **all** branches, then force-push.

---

## Option A: PowerShell script (git filter-branch)

From the repo root in PowerShell:

```powershell
.\remove-env-from-history.ps1
```

Then:

1. **Rotate any secrets** that were in `.env` (API keys, etc.) — they may have been cached or cloned.
2. **Force-push all branches:**
   ```powershell
   git push origin --force --all
   ```
3. If you have tags: `git push origin --force --tags`
4. Delete the script and this file if you like:  
   `Remove-Item remove-env-from-history.ps1, REMOVE_ENV_FROM_HISTORY.md`

---

## Option B: git-filter-repo (recommended if script fails)

[git-filter-repo](https://github.com/newren/git-filter-repo) is often more reliable and doesn’t require a clean working tree.

1. Install: `pip install git-filter-repo`
2. From repo root:
   ```powershell
   git filter-repo --path .env --invert-paths --force
   ```
3. Rotate any secrets that were in `.env`.
4. Force-push: `git push origin --force --all` (and `--tags` if you use tags).

---

## After rewriting history

- Anyone who has cloned the repo should re-clone or run:
  ```powershell
  git fetch origin
  git reset --hard origin/<branch-name>
  ```
  for each branch they use.
- Ensure `.env` is in `.gitignore` (it already is in this project).
