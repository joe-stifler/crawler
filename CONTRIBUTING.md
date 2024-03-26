# Contributing Guidelines

### Key Points to Note:

- **Not Absolute Truths**: the information herein is not exhaustively curated and is subject to change.

- **Reference Official Documentation**: In case of uncertainty, it's always better to consult the official documentation, relevant books, or content provided by our great professors.

- **Open to Suggestions**: Your participation in this project is highly valued. So feel free to open an Issue or Pull Request to propose enhancements to this guide.

---

## Main Software Engineering Book References

One highly recommended resource is [Software Engineering at Google](https://abseil.io/resources/swe-book/), a treasure trove of best practices and insights from Google’s software development experiences. While a detailed summary will be added later, we encourage all contributors to explore this book for a deeper understanding of collaborative software engineering.

---

## Guidelines

Adopting standards in software development is essential for consistency, readability, and collaboration. Standards simplify the complexity of collaborative projects and support automation processes such as [Semantic Versioning](https://semver.org/) and [Releases](https://github.com/semantic-release/semantic-release).

### Git

Understanding Git is crucial for our workflow. While the [VS Code extension for Git](https://code.visualstudio.com/docs/sourcecontrol/overview) is a time-saver, knowing how to use [Git CLI](https://git-scm.com/docs) is fundamental. For quick reference, consult the [Git Cheat Sheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf).


<details>
<summary><b>Relevant Links:</b></summary>

- [Official Git Documentation](https://git-scm.com/docs)
- [VS Code Git Extension](https://code.visualstudio.com/docs/sourcecontrol/overview)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

</details>


### Branch Methodology

We follow [GitHub Flow](https://githubflow.github.io/), a straightforward and effective branch-based workflow. GitHub Flow is a lightweight, branch-based workflow that emphasizes collaboration, review, and prompt integration. It involves creating branches for new features or fixes, implementing changes, opening PRs for review, revising, merging against main, and then deleting the feature branch upon completion. Ultimately, the `main` branch is the primary source of truth. For a more in-depth discussion, see [Software Engineering at Google book - Version Control and Branch Management Chapter](https://abseil.io/resources/swe-book/html/ch16.html).

<details>
<summary><b>Relevant Links:</b></summary>

- [GitHub Flow](https://githubflow.github.io/)
- [Critique of Git Flow](https://georgestocker.com/2020/03/04/please-stop-recommending-git-flow/)
- [Git Flow Model](https://nvie.com/posts/a-successful-git-branching-model/)
- [Chapter on Version Control and Branch Management](https://abseil.io/resources/swe-book/html/ch16.html)
</details>

### Commit Message Convention

We adhere to [Conventional Commits](https://www.conventionalcommits.org/) standards:

```markdown
<type>: <short summary> ( #<pull-request-reference> )
  │           │                       |
  |           |                       └─⫸ The PR reference number.
  |           |
  │           └─⫸ Summary in present tense. Not capitalized. No period at the end.
  │
  └─⫸ Commit Type: feat|feat!|fix|fix!|perf|perf!|refactor|refactor!|test|bench|build|ci|docs|style|chore
```

<details>
<summary><b>Commit Types:</b></summary>

| Type       | Description                                          | Example                                                        |
|------------|------------------------------------------------------|----------------------------------------------------------------|
| feat       | add a new feature                                    | `feat: add linear algebra solver for Computational Mathematics module` |
| feat!      | a breaking change to a feature                       | `feat!: add linear algebra solver for Computational Mathematics module` |
| fix        | a bug fix                                            | `fix: correct data preprocessing bug in ML project`            |
| fix!       | a breaking change to a bug fix                       | `fix!: correct data preprocessing bug in ML project`           |
| perf       | a code change that improves performance              | `perf: optimize pipeline for reduced training time`            |
| perf!      | a breaking change to a performance improvement       | `perf!: optimize pipeline for reduced training time`           |
| refactor   | a code change that neither fixes a bug nor adds a feature | `refactor: optimize pipeline for reduced training time`        |
| refactor!  | a breaking change to a refactoring                  | `refactor!: optimize pipeline for reduced training time`       |
| test       | adding missing tests or correcting existing tests   | `test: add unit tests for data preprocessing pipeline`         |
| bench      | improvements to benchmarks                          | `bench: improve performance of data preprocessing pipeline`    |
| build      | changes to build system or external dependencies    | `build: update dependencies for Data Science module`           |
| ci         | changes to CI configuration files and scripts       | `ci: update CI configuration for Data Science module`          |
| docs       | documentation only changes                          | `docs: update README for Modern Programming Methods`           |
| style      | changes that do not affect the meaning of the code  | `style: update code formatting for Data Science module`        |
| chore      | changes to the build process or auxiliary tools and libraries | `chore: update dependencies for Data Science module`        |
</details>

<details>
<summary><b>Commit Rules:</b></summary>

1) Follow the commit naming convention.
2) Be concise and descriptive.
3) Use English.
4) Start with a verb in imperative mood.
5) Use present tense.
6) Avoid ending with a period.
</details>

<details>
<summary><b>Relevant Links:</b></summary>

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Angular Commit Message Guidelines](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines)
</details>

### Branch Naming Convention

Branch names should be descriptive, following this format:

```markdown
<type>/<issue-reference>/<description>
  │           │                |
  |           |                └─⫸ A short description of the branch's purpose.
  |           |
  │           └─⫸ The github issue/ticket number. Use `no-ref` if no issue.
  │
  └─⫸ Branch Type: feat|feat!|fix|fix!|perf|perf!|refactor|refactor!|test|bench|build|ci|docs|style|chore
```

<details>
<summary><b>Branch Name Examples:</b></summary>

- `fix/no-ref/update-dependencies`
- `fix/issue-27/fix-data-sync-error`
- `test/no-ref/refactor-math-algorithms`
- `feature/issue-15/implement-regression-analysis`
</details>

<details>
<summary><b>Relevant Links:</b></summary>

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Simplified Naming Convention](https://dev.to/varbsan/a-simplified-convention-for-naming-branches-and-commits-in-git-il4)
</details>

### Pull Requests (PRs) and Code Reviews

PRs are vital for proposing and reviewing changes. Reviewers ensure code quality, while contributors address feedback for merge-readiness. According to [Software Engineering at Google - Code Review Chapter](https://abseil.io/resources/swe-book/html/ch09.html), code reviews are key for knowledge sharing and documentation. PR titles should follow the same commit naming convention as before:

```markdown
<type>: <short summary> ( #<pull-request-reference> )
  │           │                       |
  |           |                       └─⫸ The PR reference number.
  |           |
  │           └─⫸ Summary in present tense. Not capitalized. No period at the end.
  │
  └─⫸ Commit Type: feat|feat!|fix|fix!|perf|perf!|refactor|refactor!|test|bench|build|ci|docs|style|chore
```

<details>
<summary><b>PR Description Template:</b></summary>

```markdown
## Why this PR?
- Explain the need.

## What Changes?
- Summarize changes.

## Tests added?
- State test status.

## Breaking changes created?
- Highlight any disruptions.

## Additional context?
- Provide more information.
```
</details>

<details>
<summary><b>PR Description Example:</b></summary>

```markdown
## Why this PR?
- To address performance issues in our ML model training process.

## What Changes?
- Enhanced the DataPreprocessing class in data_processing.py.

## Tests added?
- Comprehensive unit tests were included.

## Breaking changes created?
- None.

## Additional context?
- Related to issue #1234 and reviewed by the data science team.
```
</details>

<details>
<summary><b>PR Rules:</b></summary>

- PR titles must follow the commit naming convention.
- PR descriptions should adhere to the template.
- Link PRs to relevant issues.
- Ensure PRs are reviewed by knowledgeable team members.
- Tag PRs appropriately.
- Assign PRs to responsible individuals.
- Link PRs to milestones and projects.
- PRs must pass automated checks.
- Use `Squash and Merge` for merging.
- PRs should be up-to-date with `main`.

</details>

<details>
<summary><b>Relevant Links:</b></summary>

- [GitHub PRs Overview](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)
- [PR Templates](https://docs.github.com/en/github/building-a-strong-community/creating-a-pull-request-template-for-your-repository)
- [PR Labels](https://docs.github.com/en/github/managing-your-work-on-github/applying-labels-to-issues-and-pull-requests)
- [Assigning PRs](https://docs.github.com/en/github/managing-your-work-on-github/assigning-issues-and-pull-requests-to-other-github-users)
- [PR Milestones](https://docs.github.com/en/github/managing-your-work-on-github/about-milestones)
- [PR Projects](https://docs.github.com/en/github/managing-your-work-on-github/about-project-boards)
- [PR Checks](https://docs.github.com/en/actions/guides/about-continuous-integration)
- [Merge Methods on GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github)

</details>

### Issues
TODO: Provide guidelines for effective issue management.

### Code Style
TODO: Define code style guidelines.

### Continuous Integration and Deployment
TODO: Detail our CI/CD practices.

### Semantic Versioning and Releases
TODO: Explain versioning and release management.

### Semantic Versioning and Releases

TODO: Explain versioning and release management.

### Collaboration and Communication

TODO: Outline collaboration and communication protocols.

---

## Code of Conduct

This file was crafted with the assistance of ChatGPT.
