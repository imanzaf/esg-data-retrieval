# Introduction to Financial Markets (IFTE0001)

**Objective:** Create a solution capable of dynamically retrieving and categorizing scope 1 (direct emissions) and scope 2
(indirect emissions from purchased electricity) data for any specified ISIN or company name of a listed company.

## Development Best Practices

#### Writing New Code
*Note:* **Don't** push commits directly to the main branch
- Create a branch from main. Use standard naming conventions, e.g., feature/my-new-feature
- Run the pre-commit hooks before pushing your code to ensure your it's well-formatted.
- Pull Requests:
    - When creating a pull request to merge back into dev, add a clear description to the pull request. Include details of any new features or changes to existing features.
    - Make sure at least **one** person reviews your PR before merging

#### Testing Code
- Write unit tests to test *at least* 50% of your code before merging into dev
- For new scripts or updates to existing scripts, run the script *at least once* before merging to make sure no code is broken

#### Project Dependencies
- Install python > 3.10.0 in your development environment (for consistency across team members)
- If using any new python package, please add it to the requirements.txt to make it easier to keep track of project dependencies
