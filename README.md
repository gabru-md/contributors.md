# contributors.md
Create Contributors.md for your project just by a simple program!

## **NOTE**:
### To create Contributors.md for any Repository it is must that the GITHUB USER should have PUSH ACCESS to the REPO.

## Introduction

A Good Organisation is the one which recognizes all of its contributors.

But it can be hectic at times creating a MARKDOWN file containing all the collaborators and their contributions to the project.

This is where the script comes to use.

It automatically generates a **simple yet cool** [**Contributors.MD**][Contributors.MD] for your Repository.

### [Skip to Usage][usage]

### Modules used are :
    OS
    SYS
    ARGPARSE
    PyGithub

### [PyGithub][PyGithub]
PyGithub is a Python (2 and 3) library to access the GitHub API v3. This library enables you to manage GitHub resources such as repositories, user profiles, and organizations in your Python applications.

Link to it [Here][PyGithub].

### OS Module
The `OS` module is used to iterate through the folders in your directory and to find the templates to render (`.rpy` files).

### SYS Module
The `SYS` module performs the `sys.exit(Error_Code)` function.

### ArgParse Module
The `ARGPARSE` module is used for parsing the commandline arguments for GitHub Authentication and name of Repository.

## Usage
    pip install PyGithub
    git clone https://github.com/gabru-md/contributors.md
    cd contributors.md
    python ./contrib.py -id GITHUB_USERNAME -pwd GITHUB_PASSWORD -repo REPO_NAME

#### The Repository Name must be in format `user/repo_name` or `org_name/repo_name`.

[Here][example] is an example of the Contributors.md that can be created.

Changes can be made to the `.rpy` files to add subsequent data to the file.

`Contributors.md` is generated inside the `rpy` folder.

[Contributors.MD]: https://github.com/gabru-md/contributors.md/blob/master/Contributors.md
[usage]: https://github.com/gabru-md/contributors.md#usage
[PyGithub]: https://github.com/PyGithub/PyGithub
[example]: https://github.com/nsITians/nsITians.github.io/blob/master/Contributors.md
