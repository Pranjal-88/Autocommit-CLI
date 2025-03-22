from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="autocommit-cli",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "click",
        "gitpython",
        "python-dotenv",
        "google-generativeai"
    ],
    entry_points={
        "console_scripts": [
            "autocommit=autocommit.cli:cli"
        ]
    },
    author="Pranjal Kishor",
    license="MIT",
    description="A CLI tool for AI-powered Git commit messages using Google Gemini API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pranjal-88/Autocommit-CLI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

