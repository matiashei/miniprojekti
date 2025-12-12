# miniprojekti

[![CI](https://github.com/matiashei/miniprojekti/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/matiashei/miniprojekti/actions/workflows/ci.yml)
![Pylint Status](https://github.com/matiashei/miniprojekti/actions/workflows/pylint.yml/badge.svg)
[![codecov](https://codecov.io/gh/matiashei/miniprojekti/graph/badge.svg?token=RHLFH9FXF0)](https://codecov.io/gh/matiashei/miniprojekti)


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
* A new feature should fulfill the acceptance criteria for it. The acceptance criteria is defined in the Product Backlog (link above) for each user story chosen for the sprint.
* The implemented code is tested with automated robot tests and unit tests:
  * Robot Framework tests are used to verify at least some of the user stories.
  * Unittests are used to verify at least some features.
  * The test coverage is on a reasonable level.
* The customer can view the code in the public GitHub repository.
* Continuous integration (CI) is implemented using GitHub Actions.
  * The status of the code and tests is visible in GitHub Actions. A badge with a link to the CI status can be found in README.md.
* The code should be as easily maintainable as possible:
  * Clear and justified architecture.
  * Clear and consistent naming conventions.
  * Consistent, clean coding style, which is monitored using Pylint. The Pylint threshold for passing is 8/10, and the Pylint status is displayed in README.md.
* New feature branch merges into main and dev branches are done through pull requests, in which the reviewer can check the code with the Definition of Done in mind.
