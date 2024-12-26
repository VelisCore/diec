# Contributing to diec

First off, thank you for considering contributing to **diec**! We appreciate all contributions, whether it's reporting an issue, fixing bugs, suggesting improvements, or creating new features. By contributing, you help make **diec** a better tool for everyone.

## How to Contribute

### 1. **Fork the Repository**
   - Click the **fork** button at the top right of this page.
   - Clone your forked repository to your local machine:
     ```bash
     git clone https://github.com/<your-username>/diec.git
     ```

### 2. **Create a Branch**
   - It's best to create a new branch for every feature or bug fix you work on:
     ```bash
     git checkout -b feature-<name>
     ```
     Replace `<name>` with a descriptive name of your feature/bugfix.

### 3. **Make Changes**
   - Write clear, concise commit messages that explain what your changes do.
   - If your contribution is a bug fix or feature addition, ensure that your code is **well-documented**.
   - If you're modifying the codebase, write **tests** that verify your changes.

### 4. **Run Tests Locally**
   - Before submitting a pull request, make sure all tests pass:
     ```bash
     pytest
     ```

### 5. **Submit a Pull Request (PR)**
   - Push your branch to your fork:
     ```bash
     git push origin feature-<name>
     ```
   - Go to your fork on GitHub and create a pull request against the `main` branch of the **diec** repository.
   - Provide a **clear description** of your changes and why they are necessary.
   - If applicable, reference any related issues (e.g., `Fixes #123`).

### 6. **Review and Feedback**
   - After submitting your PR, the project maintainers will review it and provide feedback.
   - Be open to suggestions and improvements! If any changes are requested, update your PR accordingly.

## Code Style

- **Python 3.9+** is used in this project. Make sure your code is compatible with this version or higher.
- Follow **PEP 8** for Python code style. Ensure proper indentation, variable names, and formatting.
- Add comments where necessary to explain complex or non-obvious code.
- Write unit tests for any new features or bug fixes you implement.

## Writing Tests

- We use **pytest** for testing. If you're adding a new feature or fixing a bug, please add tests for it.
- Tests should cover the basic functionality of your code, including edge cases and error handling.

## Issue Reporting

If you encounter any bugs or have suggestions for new features, please follow these steps:

### 1. **Check Existing Issues**
   - Before submitting a new issue, search the existing issues to see if it has already been reported. If so, add your comments to the existing thread.

### 2. **Provide a Detailed Description**
   - If you're reporting a bug, please include:
     - Steps to reproduce the bug.
     - Expected and actual behavior.
     - Any relevant error messages or logs.
     - Details about your environment (OS, Python version, diec version).

### 3. **Feature Requests**
   - If you have an idea for a new feature, feel free to open an issue! Provide a description of the feature and why it would be useful.

## Code of Conduct

We strive to maintain a welcoming, inclusive environment for everyone. Please follow the [Code of Conduct](CODE_OF_CONDUCT.md) when interacting with other contributors. Harassment or offensive behavior will not be tolerated.

## License

By contributing to **diec**, you agree that your contributions will be licensed under the project's **MIT License**.

## Thank You!

We thank you for taking the time to contribute to **diec**! Whether you're fixing bugs, submitting a new feature, or providing feedback, your input is what makes this project better.
