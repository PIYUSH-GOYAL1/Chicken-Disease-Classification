import setuptools

with open("README.md" , "r" , encoding= "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classification"
AUTHOR_USER_NAME = "PIYUSH-GOYAL1"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "piyushgoyal11824@gmail.com"

setuptools.setup(
    name= REPO_NAME,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A small package for Cnn Classifier",
    long_description= long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir= {"" : "src"},
    packages= setuptools.find_packages(where="src")
)