import setuptools

with open("README.md") as file:
    read_me_description = file.read()
requirements = ["requests<=2.21.0"]


setuptools.setup(
    name="ApiPyTelegram",
    version="0.1",
    author="weirdoo",
    author_email="weirdoo145@gmail.com",
    description="telegram bots core for python. ",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/resweirdoo/ApiPyTelegram",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)