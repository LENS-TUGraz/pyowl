---
name: skill_writer
description: A meta-skill for defining and creating new skills for the agent.
---

# Skill Writer Instructions

Use this skill when the user asks you to create, update, or refine a "skill". A skill is a specialized package of instructions that allows you to perform complex or repetitive tasks reliably.

## Standard Skill Structure
When creating a new skill, you must strictly follow this directory and file structure:

```text
.agent/skills/
└── <skill_name>/        # The directory name must match the skill name (snake_case)
    ├── SKILL.md         # REQUIRED: The main instruction file
    ├── scripts/         # OPTIONAL: Python or Bash scripts helper scripts
    └── resources/       # OPTIONAL: Templates, static files, or reference docs
```

## SKILL.md Format
The `SKILL.md` file implies the "logic" of the skill. It MUST start with YAML frontmatter.

```markdown
---
name: <skill_name>
description: <Short, one-sentence summary of what this skill does>
---

# <Human Readable Title>

## Purpose
Briefly explain when and why this skill should be used.

## Instructions
1. Step-by-step instructions for the agent to follow.
2. Be specific about tool usage (e.g., "Use `run_command` to execute X").
3. Refer to files in the `scripts/` or `resources/` folder relative to the skill root if necessary.

## Examples (Optional)
Provide usage examples if the task is complex.
```

## Workflow for Creating a Skill
1.  **Identify the functionality**: What specific task should this skill solve?
2.  **Determine the name**: Use concise `snake_case` (e.g., `unit_test_generator`, `database_migrator`).
3.  **Create the directory**: `.agent/skills/<skill_name>/`.
4.  **Draft `SKILL.md`**: Write clear, imperative instructions intended for an AI agent.
5.  **Add support files**: If the skill requires custom scripts (e.g., a complex regex parser or a specific linter config), place them in `scripts/` or `resources/` and reference them in `SKILL.md`.
