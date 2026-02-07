<h1 align="center">💫 PyGit</h1>

<p align="center">
  <b>Git + GitHub CLI, but in Python.</b><br>
  <i>Less typing in terminal — more coding in editor.</i>
</p>

![Preview](./demo/demo.gif)

<p align="center">
    <p align="center">
  <a href="https://github.com/Silletr/PyGit/stargazers">
    <img src="https://img.shields.io/github/stars/Silletr/PyGit?style=for-the-badge&logo=neovim&logoColor=8281f3&color=8281f3&labelColor=242529" alt="GitHub Stars" />
  </a>

  <a href="https://github.com/Silletr/PyGit/issues">
    <img src="https://img.shields.io/github/issues/Silletr/PyGit?style=for-badge&logo=github" alt="Issues">
  </a>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/github/license/Silletr/PyGit?style=for-the-badge&color=8281f3&labelColor=242529" alt="License" />
  <img src="https://img.shields.io/github/last-commit/Silletr/PyGit?style=for-the-badge&color=8281f3&labelColor=242529" alt="Last Commit" />
</p>
</p>

## Why PyGit?

- Beautiful TUI (thanks to Typer)
- One command for everything: `pygit pull`, `pygit commit "fix bug"`, `pygit push`
- Custom logs per command (`logs/pull.log`, `logs/commit.log`, etc.)
- Built-in gh CLI integration (auth, repo create, etc.)
- Zero external dependencies hell — works in poetry/venv

## Quick Start

```bash
# Install from git (recommended for now)
pip install git+https://github.com/Silletr/PyGit.git

# Or clone & install editable
git clone https://github.com/Silletr/PyGit.git
cd PyGit
poetry install
poetry shell

# Use it
pygit status
pygit commit "feat: add push command"
pygit pull
pygit push
```

## Development

```bash
git clone https:github.com/Silletr/PyGit.git
cd PyGit
poetry install
poetry shell

# Run any command
pygit auth status
```

## Contribuing

PR's are welcome! But for **Major changes** open the issue first pls!

## License

MIT - do whatever tf you want because im not eager :D
