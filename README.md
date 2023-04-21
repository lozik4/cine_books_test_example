# CINE_BOOKS_test_example
Only UI framework with Python+PyTest+Selenium+Allure

### Link to main library's
* [Python 3.9+](https://www.python.org/)
* [Pytest](https://docs.pytest.org/en/7.2.x/contents.html)
* [Selenium](https://www.selenium.dev/documentation/webdriver/) or [Selenium with Python](https://selenium-python.readthedocs.io/)
* [Allure Framework](https://docs.qameta.io/allure/#_python)
* [Selenium Grid](https://www.selenium.dev/documentation/grid/)


## Installation

### For MAC

- [Install Homebrew](http://osxdaily.com/2018/03/07/how-install-homebrew-mac-os/)

```bash
brew install allure
```

Clone project from GIT

```bash
git clone https://github.com/lozik4/cine_books_test_example.git
cd my-project
```

Install requirements

```bash
pip install -r requirements.txt
```

To run tests, run the following command

```bash
pytest --headless False tests/{path_to_test_folder_or_file}
```

To run tests in parallel (used [xdist](https://pypi.org/project/pytest-xdist/)), run the following command

```bash
pytest -n 4 --dist loadscope tests/{path_to_test_folder_or_file}
```

Make allure report, run the following command

```bash
allure generate -c allure-results
allure open /allure-report
```
If you need history data you mast copy **history** folder from previous run to current report folder

| Key                 | Description                                                                                        |
|:--------------------|:---------------------------------------------------------------------------------------------------|
| `--browser_name`    | Browser name: (chrome, firefox, edge, safari) Default: Chrome                                      |
| `--browser_version` | Browser version to run test                                                                        |
| `--hub`             | Use local o remote browser. True or False. <br>Default **False**                                   |
| `-n`                | Count parallel process. <br>Ex: **-n 4**                                                           |
| `--headless`        | Use browser UI or No. Default **True**                                                             |
| `--dist`            | Recommended **loadscope**  [docs](https://pytest-xdist.readthedocs.io/en/latest/distribution.html) |
| `--lang`            | Run Language test. Use ISO code. <br>(Only: en, uk, ru, de, fr, vi, es, el)                        |
| `--env`             | Optional how env use (dev, stage, prod)                                                            |

## Project Structure

#### Folders

| Name            | Desc                                                            | Rules                                                                                                                                                                                                                              |
|:----------------|:----------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `configs`       | configuration files for different ENV (dev.py, stage.py …)      | file name - lowercase data is stored in variables or in classes<br/>(for direct access to them)                                                                                                                                    |
| `data`          | static data (files, dictionaries, queries, parameters ...)      | file name - lowercase                                                                                                                                                                                                              |
| `modules`       | libraries for working with various services, api, libraries ... | file name - Domain Specific Language (DSL)                                                                                                                                                                                         |
| `src/elements`  | page_elements about UI                                          | file name - lowercase (the name must contain the name from the tag class= element)<br/>class names - Domain Specific Language (DSL)<br/>(the class ends on Element) example `from src.elements.input_control import ButtonElement` |
| `src/pages`     | page_objects about UI                                           | file, directory name - lowercase class name - Domain Specific Language (DSL)<br/>(the class ends on Page) example `from src.pages.index.index_page import IndexPage`                                                               |
| `tests/ui`      | the folder for saving UI tests                                  | file name see on pytest.ini recommended: test_*                                                                                                                                                                                    |

#### Files
| Name               | Desc                                         | Rules |
|:-------------------|:---------------------------------------------|:------|
| `conf_file.py`     | main configuration file                      |       |
| `conftest.py`      | pytest configuration (options, fixtures ...) |       |
| `pytest.ini`       | parameters pytest                            |       |
| `requirements.txt` | libraries are necessary for the project      |       |

## Report Example

![allure_1](https://github.com/lozik4/cine_books_test_example/blob/main/example/allure_1.png) <br>
![allure_2](https://github.com/lozik4/cine_books_test_example/blob/main/example/allure_2.png) <br>
![allure_3](https://github.com/lozik4/cine_books_test_example/blob/main/example/allure_3.png) <br>
![allure_4](https://github.com/lozik4/cine_books_test_example/blob/main/example/allure_4.png) <br>
![console_report](https://github.com/lozik4/cine_books_test_example/blob/main/example/console_1.png) <br>


