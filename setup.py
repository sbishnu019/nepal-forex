import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nepal-forex",
    version="0.0.1",
    author="Bishnu Sharma",
    author_email="sbishnu019@gmail.com",
    description="Nepal ForEx is a Python package for making Currency Exchange easier and fast between "
                "NPR and Foreign Currencies.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sbishnu019/nepal-forex",
    download_url='https://github.com/sbishnu019/nepal-forex/archive/v1.0.tar.gz',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
