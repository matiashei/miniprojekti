# miniprojekti

[![CI](https://github.com/matiashei/miniprojekti/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/matiashei/miniprojekti/actions/workflows/ci.yml)
![Pylint Status](https://github.com/matiashei/miniprojekti/actions/workflows/pylint.yml/badge.svg)


Project Backlog and individual Sprint Backlogs: [Google Docs](https://docs.google.com/spreadsheets/d/1Oh1xeJ6td34I5xTl3dneJ4uoo6Xl9Ed_Dc_2IyDjGgE/edit?usp=sharing)

### Installation and usage instructions
#### System requirements
- Check that both Python and Poetry are installed: 
```
$ python3 --version
$ poetry --version
```
#### Installation
- **Clone the project**. If using SSH the command is:
```
$ git clone git@github.com:matiashei/miniprojekti.git
```
- **Install poetry dependencies** in the project’s root directory:
```
$ poetry install
```
#### Usage
- Start the application:
```
$ poetry run python src/index.py 
```

### Definition of Done
* Acceptance criteria have been defined in the Product Backlog for each user story chosen for the sprint.
  * Starting from sprint 2, the acceptance criteria will be documented in Robot Framework syntax.
  * A link to the Product Backlog can be found in README.md.
* The implemented code is tested with automated robot tests and unit tests.
  * The test coverage is on a reasonable level.
* The customer can see the code in the GitHub repository.
* Continuous integration (CI) is implemented using GitHub Actions.
  * The status of the code and tests is visible in GitHub Actions. A badge with a link to the CI status can be found in README.md.
* The code should be as easily maintainable as possible
  * Clear and justified architecture.
  * Clear and consistent naming conventions.
  * Consistent, clean coding style, which is monitored using Pylint. The Pylint score is at least 8/10, and the Pylint status is displayed in README.md.
