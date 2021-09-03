import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nc-learn",
    version="0.0.4",
    author="Necmettin Ceylan",
    author_email="necmettinceylan@hotmail.com",
    description="A simple package to mimic sklearn library while learning ml algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nnceylan/nc-learn",
    project_urls={
        "Bug Tracker": "https://github.com/nnceylan/nc-learn/issues",
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