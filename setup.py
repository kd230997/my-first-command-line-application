from setuptools import setup

setup(
    name="duy-command-line",
    version="1.0",
    py_modules=["hello_world"],
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "hello-world=hello_world:HelloWorld",
        ],
    },
)