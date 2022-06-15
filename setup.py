import setuptools
import pathlib


# The directory containing this file
HERE = pathlib.Path(__file__).parent


# The text of the README file
with open("README.md") as f:
    README = f.read()
    lines = README.split('\n')
    desc_lines = [line for line in lines if line[:2] != "[!"]
    README = "\n".join(desc_lines)


setuptools.setup(
    name="fuzzycmeans",
    version="1.0.4",
    author="Ahmad Alobaid",
    author_email="aalobaid@fi.upm.es",
    description="Fuzzy c-means according to the research paper by James C. Bezdek et. al",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/oeg-upm/fuzzy-c-means",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=[
              'numpy', 'six', 'bokeh'
    ],
)
