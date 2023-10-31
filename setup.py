import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_dynamic_path",
    version="0.1.0",
    author="Alex Fischer",
    author_email="alex@quadrant.net",
    description="A django path() replacement enabling truly dynamic urls",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quadrant-newmedia/django_dynamic_path",
    packages=['django_dynamic_path', 'django_dynamic_path.tests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["Django>=2.2,<4.3"],
)