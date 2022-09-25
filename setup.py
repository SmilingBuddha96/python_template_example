"""Python setup.py for python_template_example package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("python_template_example", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="python_template_example",
    version=read("python_template_example", "VERSION"),
    description="Awesome python_template_example created by SmilingBuddha96",
    url="https://github.com/SmilingBuddha96/python_template_example/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="SmilingBuddha96",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["python_template_example = python_template_example.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
