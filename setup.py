import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="performance_utils",
    version="0.0.1",
    author="Carter Hinsley",
    author_email="carterhinsley@outlook.com",
    description="Performance Analytics utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Performance-Analytics/PerformanceUtils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)