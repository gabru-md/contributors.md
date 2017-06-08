# contributors.md
Create Contributors.md for your project just by a simple program!

## <strong>NOTE</strong> : 
### To create Contributors.md for any Repository<br> It is must that the GITHUB_USER should have PUSH-ACCESS to the REPO.

## Introduction

A Good Organisation is the one which recognizes all of its contributors.<br><br>But it can
be hectic at times creating a MARKDOWN file containing
all the collaborators<br>and their contributions to the project.<br><br>
This is where the script comes to use.<br><br>
It automatically generates a <strong>simple yet cool</strong>
<strong>[Contributors.MD](https://github.com/gabru-md/contributors.md/blob/master/Contributors.md)</strong> for your Repository

### [Skip to Usage](https://github.com/gabru-md/contributors.md#usage)
### Modules used are :
    OS
    SYS
    ARGPARSE
    PyGithub
    
### [PyGithub](https://github.com/PyGithub/PyGithub) 
  PyGitHub is a Python (2 and 3) library to access the GitHub API v3. This library enables you to manage GitHub resources such as repositories, user profiles, and organizations in your Python applications.
  <br>Link To it [Here](https://github.com/PyGithub/PyGithub)

### OS Module
  OS Module is used to iterate through the folders in your directory. And to find the templates to render (.rpy files).
 
### SYS Module
  SYS Module performs the sys.exit(Error_Code) function.

### ArgParse Module
  For parsing the commandline arguments for Github Authentication and name of Repository.

## Usage
    pip insatll PyGithub
    git clone https://github.com/gabru-md/contributors.md
    cd contributors.md
    python ./contrib.py -id GITHUB_USERNAME -pwd GITHUB_PASSWORD -repo REPO_NAME
    
#### The Repository Name must be in format user/repo_name or org_name/repo_name 

[Here](https://github.com/nsITians/nsITians.github.io/blob/master/Contributors.md)
is an example of the Contributors.md that can be created.

Changes can be made to the .rpy files to add subsequent data to the file.<br>

Contributors.md is generated inside the 'rpy' folder
