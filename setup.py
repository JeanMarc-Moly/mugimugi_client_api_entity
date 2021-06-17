from pathlib import Path
from setuptools import setup, find_packages

with (Path(__file__).resolve().parent / "README.md").open(encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mugimugi-client-api-entity",
    version="0.4.0",
    description="Mugimugi api client entities parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JeanMarc-Moly/mugimugi_client_api_entity",
    author="MOLY Jean-Marc",
    author_email="jeanmarc.moly@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="development",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    python_requires=">=3.9.*, <4",
    install_requires=["xsdata==21.6"],
    extras_require={
        "dev": [
            "appdirs==1.4.4",
            "astroid==2.6.0.dev0; python_version ~= '3.6'",
            "attrs==21.2.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "backcall==0.2.0",
            "black==19.10b0",
            "cached-property==1.5.2",
            "cerberus==1.3.4",
            "certifi==2021.5.30",
            "chardet==4.0.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "click==8.0.1; python_version >= '3.6'",
            "colorama==0.4.4; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "decorator==5.0.9; python_version >= '3.5'",
            "distlib==0.3.2",
            "idna==2.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "ipython==7.24.1",
            "ipython-genutils==0.2.0",
            "isort==5.8.0",
            "jedi==0.18.0; python_version >= '3.6'",
            "lazy-object-proxy==1.6.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5'",
            "matplotlib-inline==0.1.2; python_version >= '3.5'",
            "mccabe==0.6.1",
            "mypy==0.902",
            "mypy-extensions==0.4.3",
            "orderedmultidict==1.0.1",
            "packaging==20.9; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "parso==0.8.2; python_version >= '3.6'",
            "pathspec==0.8.1",
            "pep517==0.10.0",
            "pexpect==4.8.0; sys_platform != 'win32'",
            "pickleshare==0.7.5",
            "pip-shims==0.5.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "pipenv-setup==3.1.1",
            "pipfile==0.0.2",
            "plette[validation]==0.2.3; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "prompt-toolkit==3.0.18; python_full_version >= '3.6.1'",
            "ptyprocess==0.7.0",
            "pygments==2.9.0; python_version >= '3.5'",
            "pylint==3.0.0a3",
            "pyparsing==3.0.0b2; python_version >= '3.5'",
            "python-dateutil==2.8.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "regex==2021.4.4",
            "requests==2.25.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "requirementslib==1.5.16; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "six==1.16.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "toml==0.10.2; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "tomlkit==0.7.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "traitlets==5.0.5; python_version >= '3.7'",
            "typed-ast==1.4.3",
            "typing-extensions==3.10.0.0",
            "urllib3==1.26.5; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4.0'",
            "vistir==0.5.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "wcwidth==0.2.5",
            "wheel==0.36.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "wrapt==1.12.1",
        ]
    },
    dependency_links=[],
)
