# Day 3 — Git & GitHub Advanced

## DevSentinel AI — 90-Day AI + DevOps Project

**Day:** 3
**Topic:** Git & GitHub Advanced
**Project:** DevSentinel AI
**Git Branch:** `main`

---

# 1. What I Learned Today

Today I learned how Git is used in a real DevOps workflow.

The main topics were:

* Git branches
* Feature branches
* Switching branches
* Git merge
* Git pull
* Git stash
* Git reset
* Git tags
* Merge conflicts
* Conflict resolution
* Branch cleanup
* GitHub push
* Checking repository status
* Viewing commit history

---

# 2. Git Branches

A Git branch is an independent line of development.

Branches allow developers to work on features without directly changing the main branch.

Example:

```bash
git branch
```

This shows the available branches.

The `*` symbol shows the current branch.

Example:

```text
* main
```

This means I am currently working on the `main` branch.

---

# 3. Create a Feature Branch

I created a feature branch for Linux monitoring:

```bash
git switch -c feature/linux-monitoring
```

This command:

1. Creates a new branch.
2. Switches to that branch.

The branch name was:

```text
feature/linux-monitoring
```

---

# 4. Branch Information Script

I created:

```text
scripts/linux/branch-info.sh
```

The script displays information about the current Git branch and system.

```bash
#!/bin/bash

echo "========================================"
echo "      DevSentinel AI"
echo "      Branch Information"
echo "========================================"

echo "Current Branch: $(git branch --show-current)"
echo "Current User  : $(whoami)"
echo "Current Folder: $(pwd)"

echo "========================================"
```

I made the script executable:

```bash
chmod +x scripts/linux/branch-info.sh
```

Then executed it:

```bash
./scripts/linux/branch-info.sh
```

It showed:

```text
Current Branch: feature/linux-monitoring
Current User  : hari
Current Folder: /mnt/c/Users/gandu/devsentinel-ai
```

---

# 5. Git Merge

After completing the feature work, I switched back to `main`:

```bash
git switch main
```

Then merged the feature branch:

```bash
git merge feature/linux-monitoring
```

The feature was merged into `main`.

I then pushed the changes:

```bash
git push origin main
```

---

# 6. Git Pull

`git pull` downloads changes from the remote repository and integrates them into the local branch.

Command:

```bash
git pull
```

My result:

```text
Already up to date.
```

This means my local repository already contained the latest changes from GitHub.

---

# 7. Git Stash

`git stash` temporarily saves uncommitted changes.

It is useful when I am working on something but need to switch branches or work on another task.

Example:

```bash
git stash
```

To see saved stashes:

```bash
git stash list
```

Example:

```text
stash@{0}: WIP on main
```

To restore the latest stash:

```bash
git stash pop
```

In my practice, I:

1. Created a temporary file.
2. Staged it.
3. Used `git stash`.
4. Verified the stash.
5. Used `git stash pop`.
6. Removed the temporary practice file.

---

# 8. Git Reset

`git reset` can remove changes from the staging area.

For example:

```bash
git add file.txt
```

stages a file.

Then:

```bash
git reset
```

unstages the file.

The file itself is not deleted.

In my practice, I created:

```text
scripts/linux/reset-test.txt
```

Then staged it:

```bash
git add scripts/linux/reset-test.txt
```

Then unstaged it:

```bash
git reset
```

Finally, I removed the temporary practice file.

---

# 9. Git Tags

A Git tag is used to mark an important point in Git history.

I created the first DevSentinel AI project tag:

```bash
git tag -a v0.1.0 -m "DevSentinel AI initial foundation"
```

To list tags:

```bash
git tag
```

Result:

```text
v0.1.0
```

To view tag information:

```bash
git show v0.1.0
```

I pushed the tag to GitHub:

```bash
git push origin v0.1.0
```

Tags are useful for:

* Releases
* Versions
* Stable milestones
* Production versions

Example:

```text
v0.1.0
v0.2.0
v1.0.0
```

---

# 10. Merge Conflicts

A merge conflict happens when Git cannot automatically combine changes from two branches.

I intentionally created a merge conflict to understand how real DevOps teams handle conflicts.

First, I created:

```text
scripts/linux/conflict-demo.txt
```

Initial content:

```text
Environment: Development
```

Then I created a branch:

```bash
git switch -c conflict-demo
```

On this branch, I changed the file to:

```text
Environment: Testing
```

and committed it.

Then I switched back to `main`:

```bash
git switch main
```

On `main`, I changed the same line to:

```text
Environment: Production
```

and committed it.

Then I attempted:

```bash
git merge conflict-demo
```

Git produced a merge conflict.

---

# 11. Understanding Conflict Markers

Git showed the following:

```text
<<<<<<< HEAD
Environment: Production
=======
Environment: Testing
>>>>>>> conflict-demo
```

Meaning:

```text
<<<<<<< HEAD
```

marks the changes from the current branch.

```text
=======
```

separates the two versions.

```text
>>>>>>> conflict-demo
```

marks the changes coming from the other branch.

---

# 12. Resolving the Conflict

I manually resolved the conflict by choosing:

```text
Environment: Production
```

Then I staged the resolved file:

```bash
git add scripts/linux/conflict-demo.txt
```

Then committed the merge:

```bash
git commit -m "Resolve merge conflict"
```

Git created a merge commit:

```text
d0abf34 Resolve merge conflict
```

This taught me that merge conflicts are solved by:

1. Opening the conflicted file.
2. Understanding both changes.
3. Choosing or combining the correct content.
4. Removing Git conflict markers.
5. Running `git add`.
6. Creating the merge commit.

---

# 13. Branch Cleanup

After merging the branches, I deleted the old practice branches.

First:

```bash
git branch -d conflict-demo
```

Then:

```bash
git branch -d feature/linux-monitoring
```

Finally:

```bash
git branch
```

Result:

```text
* main
```

This means the local repository now has only the `main` branch.

---

# 14. Git Commit History

I used:

```bash
git log --oneline
```

to view the commit history.

I also used:

```bash
git log --oneline origin/main..main
```

to see commits that existed locally but had not yet been pushed.

The four Git practice commits were:

```text
04a8c59 Add merge conflict practice file
576629e Change environment to production
a115c4b Change environment to testing
d0abf34 Resolve merge conflict
```

These commits demonstrated a real merge-conflict workflow.

---

# 15. Git Status

I used:

```bash
git status
```

to check the repository state.

Final result:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

This means:

* I am on `main`.
* Local `main` is synchronized with GitHub.
* There are no uncommitted changes.
* The working directory is clean.

---

# 16. GitHub Push

After completing the Git practice, I pushed the local commits:

```bash
git push origin main
```

GitHub confirmed:

```text
09a7110..d0abf34  main -> main
```

Therefore the local Git repository and GitHub repository are synchronized.

---

# 17. Important Git Commands Learned

| Command                     | Purpose                       |
| --------------------------- | ----------------------------- |
| `git branch`                | List branches                 |
| `git switch -c branch-name` | Create and switch to a branch |
| `git switch main`           | Switch to main                |
| `git merge branch-name`     | Merge a branch                |
| `git pull`                  | Get latest remote changes     |
| `git stash`                 | Temporarily save changes      |
| `git stash list`            | Show stashes                  |
| `git stash pop`             | Restore latest stash          |
| `git reset`                 | Unstage changes               |
| `git tag`                   | List tags                     |
| `git tag -a`                | Create an annotated tag       |
| `git push origin main`      | Push main to GitHub           |
| `git push origin tag-name`  | Push a tag                    |
| `git status`                | Check repository state        |
| `git log --oneline`         | View commit history           |
| `git branch -d`             | Delete a merged branch        |

---

# 18. Real DevOps Git Workflow

A common development workflow is:

```text
Developer
    ↓
Create Feature Branch
    ↓
Write Code
    ↓
Test
    ↓
Commit
    ↓
Push Feature Branch
    ↓
Pull Request
    ↓
Code Review
    ↓
Merge
    ↓
main
    ↓
CI/CD Pipeline
    ↓
Build
    ↓
Test
    ↓
Security Scan
    ↓
Deploy
```

This workflow will become important later when I learn Jenkins and CI/CD.

---

# 19. What I Practiced in DevSentinel AI

Today I used Git as part of a real project instead of learning Git only through theory.

I practiced:

```text
Branch
  ↓
Feature Development
  ↓
Commit
  ↓
Merge
  ↓
Conflict
  ↓
Conflict Resolution
  ↓
Branch Cleanup
  ↓
Push to GitHub
```

This gives me practical experience with the Git workflow used in software and DevOps projects.

---

# 20. Day 3 Summary

Today I learned that Git is more than just:

```bash
git add
git commit
git push
```

I learned how to work with:

* Branches
* Feature development
* Merging
* Conflicts
* Stashing
* Resetting
* Tags
* Remote repositories
* GitHub synchronization
* Branch cleanup
* Commit history

The most important lesson was understanding how developers can safely work on different changes and later combine them using Git.

---

# 21. Day 3 Achievement

### DevSentinel AI — Git Foundation Completed

I can now:

* Create Git branches
* Work with feature branches
* Merge branches
* Understand merge conflicts
* Resolve merge conflicts
* Temporarily stash changes
* Unstage changes with reset
* Create Git tags
* Push tags to GitHub
* Clean up merged branches
* Check Git history
* Synchronize local and remote repositories

**Day 3 Status: COMPLETED ✅**

---

# 22. Next Step

The next DevSentinel AI learning stage will build on this Git foundation and move toward automation, scripting, application development, containers, CI/CD, cloud, and eventually AI-powered DevOps automation.
