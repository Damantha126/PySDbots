import setuptools

with open("README.md", encoding="utf8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="pysdbots",
    packages=setuptools.find_packages(),
    version="0.0.1",
    license="MIT",
    description="python pakage pakage for sdbots api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="DamanthaJasinghe",
    author_email="damanthaja@gmail.com",
    url="https://github.com/damantha126/pysdbots",
    keywords=["sdbots", "python-pakage", "sd-api"],
    install_requires=["requests>=2.28.1"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)