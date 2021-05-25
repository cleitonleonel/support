from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="support",
    version="0.0.1",
    author="Cleiton Leonel Creton",
    author_email="cleiton.leonel@gmail.com",
    description="Simple share desktop with python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cleitonleonel/support.git",
    packages=["."],
    install_requires=[
        'pyngrok',
        'PyYAML'
    ],
    project_urls={
        "Bug Tracker": "https://github.com/cleitonleonel/support/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
