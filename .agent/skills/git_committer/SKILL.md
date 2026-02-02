---
name: git_committer
description: A skill for summarizing changes, generating commit messages, and committing code via git.
---

# Git Committer

## Purpose
Use this skill when you need to save changes to the version control system. It ensures that commit messages are descriptive, follow best practices, and that the correct files are staged.

## Instructions

1.  **Analyze the Workspace State**:
    *   Run `git status` to see which files have been modified, added, or deleted.
    *   Run `git diff` to view the specific line-by-line changes for modified files.
    *   If there are untracked files, check if they should be added or ignored.

2.  **Formulate a Commit Message**:
    *   Based on the `git diff` output, draft a commit message.
    *   **Format**: Use normal language in the present tense (imperative mood).
        *   Example: "Add support for JSON output" or "Fix bug in parser".
        *   Do NOT use prefixes like `feat:`, `fix:`, or `chore:`.
    *   **Quality**: The message must be concise but descriptive. Avoid vague messages like "update code".

3.  **Execute Git Commands**:
    *   **Stage Files**: Use `git add <file>` for specific files or `git add .` if all changes are related to the single commit.
    *   **Commit**: Use `git commit -m "message"`.

4.  **Verification**:
    *   Run `git status` again to ensure the working directory is clean (or matches the expected state).

## Examples

**Scenario**: User added a new login feature.
1.  Agent runs `git status` -> sees `login.py` modified.
2.  Agent runs `git diff` -> sees added `def login(): ...`.
3.  Agent runs:
    ```bash
    git add login.py
    git commit -m "Implement basic login function"
    ```
