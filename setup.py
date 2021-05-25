import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="support",
    version="0.0.1",
    author="Cleiton Leonel Creton",
    author_email="cleiton.leonel@gmail.com",
    description="Simple share desktop with python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cleitonleonel/support",
    project_urls={
        "Bug Tracker": "https://github.com/cleitonleonel/support/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'support': 'support'},
    packages=setuptools.find_packages(where="support"),
    python_requires=">=3.6",
)
