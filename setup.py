import setuptools

with open("README.md", encoding="utf8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="pysdbots",
    packages=setuptools.find_packages(),
    version="0.1.1",
    license="MIT",
    description="A Project Made To Centralize Various APIs 📖 No Authorization Needed :)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="DamanthaJasinghe",
    author_email="damanthaja@gmail.com",
    url="https://github.com/damantha126/pysdbots",
    keywords=["sdbots", "python-pakage", "sd-api", "api", "damanthaja", "mritzme", "damantha126"],
    install_requires=["requests>=2.28.1"],
    project_urls={
        "Tracker": "https://github.com/damantha126/pysdbots/issues",
        "Community": "https://t.me/SDBOTs_inifinity",
        "Source": "https://github.com/damantha126/pysdbots",
        "Documentation": "https://docs.sdbots.tk",
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
    ],
)