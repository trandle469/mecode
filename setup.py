import re
from os import path
from setuptools import setup, find_packages


def get_version():
    with open("mecode/__init__.py") as f:
        content = f.read()
    match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", content, re.M)
    if match:
        return match.group(1)
    raise RuntimeError("Unable to find version string.")


INFO = {
    "name": "mecodewithmeca",
    "version": get_version(),
    "description": "Simple GCode generator",
    "author": "Ty Randle",
    "author_email": "rtelles@g.harvard.edu",
}

here = path.abspath(path.dirname(__file__))

"""gather install package requirements"""
with open(path.join(here, "requirements.txt")) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [
        line
        for line in requirements_file.read().splitlines()
        if not line.startswith("#")
    ]

requirements = [r for r in requirements if not r.startswith("git+")]

"""gather development requirements"""
with open(path.join(here, "requirements.dev.txt")) as dev_requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    dev_requirements = [
        line
        for line in dev_requirements_file.read().splitlines()
        if not line.startswith("#")
    ]

dev_requirements = [r for r in dev_requirements if not r.startswith("git+")]

setup(
    name=INFO["name"],
    version=INFO["version"],
    description=INFO["description"],
    author=INFO["author"],
    author_email=INFO["author_email"],
    packages=find_packages(),
    url="https://github.com/rtellez700/mecode",
    download_url="https://github.com/rtellez700/mecode/tarball/master",
    keywords=["gcode", "3dprinting", "cnc", "reprap", "additive"],
    zip_safe=False,
    package_data={
        "": ["*.txt", "*.md"],
    },
    install_requires=requirements,
    tests_require=dev_requirements,
)
