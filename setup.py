import os
from typing import Dict
import setuptools
from pysdbots import __docs__

base_path = os.path.abspath(os.path.dirname(__file__))

with open("README.md", encoding="utf8") as readme:
    long_description = readme.read()

about: Dict = {}
with open(
    os.path.join(
        base_path,
        'pysdbots',
        '__version__.py',
    ), encoding='utf-8',
) as f:
    exec(f.read(), about)

setuptools.setup(
    name="pysdbots",
    packages=setuptools.find_packages(),
    version=about['__version__'],
    license="MIT",
    description="A Project Made To Centralize Various APIs 📖 No Authorization Needed :)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="DamanthaJasinghe",
    author_email="damanthaja@gmail.com",
    url="https://github.com/Damantha126/pysdbots",
    keywords=["sdbots", "python-pakage", "sd-api", "api", "damanthaja", "mritzme", "damantha126", "pysdbots", "jasinghe", "damantha-jasinghe"],
    install_requires=["requests"],
    project_urls={
        "Tracker": "https://github.com/Damantha126/pysdbots/issues",
        "Community": "https://t.me/SDBOTs_inifinity",
        "Source": "https://github.com/Damantha126/pysdbots",
        "Documentation": __docs__,
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)