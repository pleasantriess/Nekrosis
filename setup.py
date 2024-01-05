"""
setup.py: Setup script for Nekrosis application.

Usage:
    python3 -m build --wheel
"""

from setuptools import setup, find_packages


def fetch_property(property: str) -> str:
    """
    Fetch a property from the main Nekrosis class.

    Parameters:
        property (str): The name of the property to fetch.

    Returns:
        The value of the property.
    """
    for line in open("nekrosis/__init__.py", "r").readlines():
        if not line.startswith(property):
            continue
        return line.split("=")[1].strip().strip('"')
    raise ValueError(f"Property {property} not found.")


setup(
    name="nekrosis",
    version=fetch_property("__version__:"),
    description="Multi-platform persistence tool for user-provided payloads.",
    long_description_content_type="text/markdown",
    long_description=open("README.md", "r").read(),
    author=fetch_property("__author__:"),
    author_email="",
    license="3-clause BSD License",
    url="https://github.com/Nekrosis-ISS-Capstone/Nekrosis",
    python_requires='>=3.6',
    packages=find_packages(include=['nekrosis', 'nekrosis.support', 'nekrosis.support.*']),
    package_data={
        'nekrosis': ['*'],
        'nekrosis.support': ['*'],
        'nekrosis.support.*': ['*'],
    },
    py_modules=["nekrosis"],
    include_package_data=True,
    install_requires=open("requirements.txt", "r").readlines(),
)