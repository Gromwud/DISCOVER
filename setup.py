from setuptools import setup, find_packages

setup(
    name="dso",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "tensorflow==1.15",  # Match your requirements
    ],
    python_requires=">=3.7",
)