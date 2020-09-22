import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="integrity_check", 
    version="0.0.1",
    author="ArtFab",
    author_email="",
    description="A replacement for assert",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArtFab/integrity-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
