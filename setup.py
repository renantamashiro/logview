import pathlib
import setuptools

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setuptools.setup(
    name="logview",
    version="0.1.0",
    description="A CLI application to visualize Linux events with filtering and sorting options",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/renantamashiro/logview",
    author="Renan Tamashiro",
    author_email="tamashirorenan@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=setuptools.find_packages(exclude=("tests")),
    include_package_data=True,
    # install_requires=[],
    entry_points={
        "console_scripts": [
            "logview=logview.__main__:main",
        ]
    },
)