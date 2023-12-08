import setuptools

"""with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()"""

long_description = "A toy random generator project"

__version__ = "0.0.0"

REPO_NAME = "dre_random"
AUTHOR_USER_NAME = "sriram"
SRC_REPO = "dre_random"
AUTHOR_EMAIL = "sriramr244@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A toy random generator project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
