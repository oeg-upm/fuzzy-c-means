import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fuzzycmeans",
    version="1.0.1",
    author="Ahmad Alobaid",
    author_email="aalobaid@fi.upm.es",
    description="Fuzzy c-means according to the research paper by James C. Bezdek et. al",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oeg-upm/fuzzy-c-means",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries",
    ),
)