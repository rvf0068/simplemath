from setuptools import setup, find_packages

setup(
    name="simplemath",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    test_suite="tests",
    author="Your Name",
    description="A simple math package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/simplemath",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
