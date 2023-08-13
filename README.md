# deep-client
[![Gitpod](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/deep-foundation/deep-client) [![Discord](https://badgen.net/badge/icon/discord?icon=discord&label&color=purple)](https://discord.gg/deep-foundation)

Deep Client - a way to connect your favourite language with Deep.

## Install dependencies

```
pip install -r requirements.txt
```

## Running Tests

To run the test suite, execute the following commands from the root directory of the project:

```
python -m unittest discover -s tests -v
python -m unittest tests.test_select.TestDeepClientSelect.testSelect
```