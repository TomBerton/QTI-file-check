# QTI Testing CLI Tool

## Install

First, make sure that there isn't a previous install in the "qti_test" folder.

```shell
rm -rf __pycache__ *egg*
```

Next, change the directory to the `qti_test` folder and run the following command to install the dependencies.

```shell
pip install -e .
```

## Usage

For help type the following:

```shell
qtitest --help
```

To test your QTI text files by providing the path to the file after running the following command:

```shell
qtitest test
```
