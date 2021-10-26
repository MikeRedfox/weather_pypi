import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weather-Mike_Redfox",
    version="0.0.1",
    author="Michele Guarda",
    author_email="michele97.guarda@hotmail.com",
    description="Shows you the weather forecast for the next the current day and 2 days after",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mikeredfox/weather_pypi",
    project_urls={
        "Bug Tracker": "https://github.com/mikeredfox/weather_pypi/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)