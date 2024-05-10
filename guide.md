# Creating a "Hello World" Python Package

This guide provides a step-by-step process to create a basic "Hello World" Python package.

## Step 1: Setting Up the Environment

### 1.1 Install Conda

First, ensure that Conda is installed on your system. If not, you can download and install it from the [Anaconda](https://www.anaconda.com/products/distribution) website.

### 1.2 Create a Conda Environment

Once Conda is installed, create a new environment specifically for your package development:

```bash
conda create --name mypackage python=3.10
```

Activate the newly created environment:

```bash
conda activate mypackage
```

## Step 2: Project Structure

Organise your project with the following structure:

```
hello_world_package/
|-- hello_world/
|   |-- __init__.py
|   |-- core.py
|-- tests/
|   |-- __init__.py
|   |-- test_core.py
|-- setup.py
|-- README.md
```

- `hello_world/`: This directory will contain all the package code.
- `tests/`: This directory will include tests for your package.
- `setup.py`: This script will facilitate the installation of the package.
- `README.md`: A markdown file to explain the purpose of the package and how to install it.

## Step 3: Writing the Code

### 3.1 The Package Code

Edit `hello_world_package/hello_world/core.py` to include a simple function that prints "Hello, World!":

```python
def say_hello():
    print("Hello, World!")
```

### 3.2 The `__init__.py` File

In `hello_world_package/hello_world/__init__.py`, import the function:

```python
from .core import say_hello
```

### 3.3 Writing Tests

In `hello_world_package/tests/test_core.py`, write a simple test case:

```python
from hello_world.core import say_hello

def test_say_hello(capsys):
    say_hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
```

## Step 4: Setup Script

Edit `hello_world_package/setup.py` to set up the package:

```python
from setuptools import setup, find_packages

setup(
    name='hello_world',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Dependencies can be added here, for example:
        # 'numpy',
    ],
    entry_points={
        'console_scripts': [
            'hello_world=hello_world.core:say_hello',
        ],
    }
)
```

## Step 5: Including Additional Files in the Package

If your package requires including non-Python files, such as a CSV file, you need to ensure they are included when the package is built and installed. This is done using a `MANIFEST.in` file and proper setup in your `setup.py`.

### 5.1 Create the `MANIFEST.in` File

In the root of your project directory (`hello_world_package/`), create a `MANIFEST.in` file to specify which files should be included:

```plaintext
include hello_world/data/example.csv
```

This line tells the packaging system to include the `example.csv` file located in the `hello_world/data/` directory within the package.

### 5.2 Accessing the Data File

To access this file from within your package, use the `pkg_resources` module provided by `setuptools`. Modify the `core.py` file to access the CSV file:

```python
import pkg_resources

def read_data():
    data_path = pkg_resources.resource_filename('hello_world', 'data/example.csv')
    with open(data_path, 'r') as file:
        data = file.read()
    return data
```

This function finds the correct path for `example.csv` and reads it, returning the contents. We can then update our `setup.py` file:

```python
from setuptools import setup, find_packages

setup(
    name='hello_world',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,  # Ensures that package data specified in MANIFEST.in is included in packages
    package_data={
        # If there are any package-specific data files, they need to be listed here
        'hello_world': ['data/*.csv'],
    },
    install_requires=[
        # Dependencies can be added here, for example:
        # 'numpy',
    ],
    entry_points={
        'console_scripts': [
            'hello_world=hello_world.core:say_hello',
        ],
    }
)
```

## Step 6: Building the Package

Before distributing your package, you need to build it:

### 6.1 Install Required Tools

Ensure you have the required tools installed:

```bash
pip install setuptools wheel twine
```

### 6.2 Build Your Package

Run the following command to build your package:

```bash
python setup.py sdist bdist_wheel
```

This command creates a source distribution (`sdist`) and a binary distribution (`bdist_wheel`) in the `dist/` directory.

## Step 6: Local Installation and Testing

Before building your package for distribution, it is essential to install it locally to ensure that everything works as expected. This step should come after building the package (Step 6) but before publishing it to PyPI (Step 7).

### 6.1 Install the Package Locally

Navigate to the root of your project directory where the `setup.py` file is located. Install the package locally by running:

```bash
pip install .
```

This command tells pip to find the `setup.py` file in the current directory and install the package accordingly. If your package includes scripts or command line tools defined in `entry_points`, they will be installed in your environment's `bin` directory.

### 6.2 Verify Local Installation

To verify the installation, try running any scripts or commands defined in your package. For example, if your package includes a `hello_world` command, you can run:

```bash
hello_world
```

Additionally, you can start a Python interpreter and try importing your module and using its functions to ensure they behave as expected:

```python
from hello_world.core import say_hello, read_data

say_hello()
print(read_data())
```

This should execute without errors, displaying the "Hello, World!" message and the contents of the CSV file, if applicable. Verifying the package locally ensures that all components, including additional files, are correctly included and functional.

## Step 8: Publishing Your Package to PyPI

To publish your package to the Python Package Index (PyPI), follow these steps:

### 8.1 Register on PyPI

Ensure you have an account on [PyPI](https://pypi.org) and [TestPyPI](https://test.pypi.org) (optional, for testing).

### 8.2 Upload Your Package

First, upload your package to TestPyPI to ensure everything works as expected:

```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

If the upload is successful and you can install your package from TestPyPI, proceed to upload it to PyPI:

```bash
twine upload dist/*
```

### 8.3 Install Your Package

Once your package is on PyPI, anyone can install it using pip:

```bash
pip install hello_world
```

## Step 9: Verifying Installation

After installation, you should be able to run the command `hello_world` from anywhere in your terminal, as defined in the `entry_points` in your `setup.py`. Also, you can check the functionality that reads from the included CSV file by importing and calling the appropriate function from your package.

This comprehensive guide should now provide you with the knowledge and tools to create, build, include additional resources, and publish a Python package to PyPI, following best practices in package development.