from setuptools import find_packages, setup

setup(
    name="RAGsystem",
    version="0.0.1",
    author="RITIK",
    author_email="ritikpadhi1507@gmail.com",
    packages=find_packages(),
    install_requires=["langchain","langchainhub","streamlit","pypdf","faiss-cpu"]
)
