from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Vitor Gomes Valim",
    author_email="vitorvalim1@hotmail.com",
    description="Transformador de tonalidade em imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vitorvalim/image-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)