from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="resizing_image",
    version="0.0.1",
    author="Ivisson César",
    author_email="ivissoncesar@gmail.com",
    description="Este pacote é responsável por ler uma imagem e redimensioná-la de forma livre",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)