
[[2026Jul01_1757 git]]  
## 1. Install Git

**Windows**  
Download from [git-scm.com](https://git-scm.com) – use default options.  
After install, open **Git Bash** (simulates Linux commands).

**Linux (Ubuntu/Debian)**  
```bash
sudo apt install git
```

Verify installation:  
```bash
git --version
```

---

## 2. config 
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --list
```
## 3. local repository

```bash
git init # this make .git which it is hidden and it a place to track changes but nothing in it.

# start a projeck or add file or change code
# make hello.txt file

# Add the file git list to track them. 
git add hello.txt
git add . -A # add all files and once 
git status # Check status – Git sees an untracked file
# Now commit it with a message
git commit -m "i have Added hello.txt"
```

---

## 4. Connect to a remote (GitHub)

Make sure you have a GitHub account, then:

**A. Create a new empty repo on GitHub** (do **not** add README, .gitignore, or license).

**B. Link your local repo to GitHub**

```bash
git remote add origin https://github.com/your-username/your-repo.git
git push --set-upstream origin master

```

**C. Push your code**

```bash
git push # it would push master to origin repor but for use below
# git push -u new_origin main
```

The `-u` sets the upstream so next time you can just type `git push`.

---
## 5. Clone an existing repo

Instead of starting from scratch, you can copy a remote repo:

```bash
git clone https://github.com/user/repo-name.git
# you use it but you can not push it on origin repo, you must make_pull reaqust or and new upstearm repo 
git checkout -b add-feature
# work on and commite and
git push origin add-feature # you chack pull requte after in website 
# fork you should do it form website 
```

---

## 5. Modify and see history

```bash
# what 
git diff <fileone> 

# Stage and commit again
git add hello.txt
git commit -m "Update greeting"

# View the commit log
git log --oneline
```

```
Working Directory → git add → Staging Area → git commit → Repository (history)
    (your files)                    (ready to save)         (permanent snapshot)
```

## 6. Create a branch (experiment safely)

Branches let you work on different features without touching the main code.

```bash
# See current branch (main or master)
git branch

# Create a new branch called "feature"
git branch <feature>

# Switch to it
git checkout <feature>

# Or do both in one command
git checkout -b <feature>
```

Make changes, commit them, then switch back to `main`:
```bash
git checkout main
```

Your changes are isolated in the `feature` branch.

---

## 9. Merge a branch

When your feature is ready, bring it into `main`:

```bash
git checkout main
git merge feature
```

## 10. othor 

```bash 
git restore --staged <file> # get oubt file form tracking but keep chinging 
git reset --soft HEAD~1 #like up

```