import setuptools


long_description = """
# fuzzy-c-means
Fuzzy c-means Clustering

## Description
This implementation is based on the paper
**FCM: The fuzzy c-means clustering algorithm**  by: *James C.Bezdek, Robert Ehrlich, and  William Full*

## To run the tests
`sh tests/run_tests.sh`

## Install via pip
```pip install fuzzycmeans```

"""


setuptools.setup(
    name="fuzzycmeans",
    version="1.0.3",
    author="Ahmad Alobaid",
    author_email="aalobaid@fi.upm.es",
    description="Fuzzy c-means according to the research paper by James C. Bezdek et. al",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oeg-upm/fuzzy-c-means",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries",
    ),
    install_requires=[
              'numpy', 'six', 'bokeh'
    ],

)
