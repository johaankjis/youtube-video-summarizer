# Contributing to YouTube Video Summarizer

Thank you for your interest in contributing to YouTube Video Summarizer! This document provides guidelines for contributing to this project.

## Code of Conduct

By participating in this project, you are expected to uphold our [Code of Conduct](CODE_OF_CONDUCT.md).

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include error messages and stack traces**
- **Include your environment details** (OS, Python version, dependency versions)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and explain the behavior you expected to see**
- **Explain why this enhancement would be useful**

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** with clear, concise commits
3. **Test your changes** thoroughly
4. **Update documentation** as needed
5. **Follow the existing code style**
6. **Write clear commit messages**

#### Pull Request Process

1. Update the README.md with details of changes if applicable
2. Update the CHANGELOG.md with a note describing your changes
3. Ensure all tests pass
4. Make sure your code lints without errors
5. The PR will be merged once you have the sign-off of at least one maintainer

## Development Setup

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/youtube-video-summarizer.git
   cd youtube-video-summarizer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API keys as described in README.md

4. Make your changes and test them locally

## Style Guidelines

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise
- Add comments for complex logic

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

## Testing

Please ensure your code changes are tested:

- Add tests for new features
- Ensure existing tests pass
- Test with different Python versions if possible
- Test with different input scenarios

## Documentation

- Update README.md if you change functionality
- Add docstrings to new functions
- Update CHANGELOG.md with your changes
- Comment complex code sections

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

Thank you for contributing! 🎉
