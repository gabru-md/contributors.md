"""
@Author : Manish Devgan
@Github : https://github.com/gabru-md
@Language : Python 2.7
"""

import os
import sys
import argparse
from github import Github

TEMPLATE_FOLDER = 'rpy'
DEFAULT_NAME = 'None'

"""

Generate Contributors.MD for your repository.

Modules used are :
    OS
    SYS
    ARGPARSE
    PyGithub

PyGithub is an Organisation on Github
that provides with a Python module to
integrate the code with GITHUB's API.

A very special thanks to them for creating
the module.

The Link to which is : https://github.com/PyGithub

"""

def get_args():
    parser = argparse.ArgumentParser(description=(
        'To create collaborators for the repository you must have push access '
        'to the repository. Without push access this will not work!'
    ))
    parser.add_argument('-id', type=str,
                        help='ID or Username for Github', required=True)
    parser.add_argument('-pwd', type=str, help='Password for Github',
                        required=True)
    parser.add_argument('-repo', type=str, help=(
        'Name of the Repository. If repository in id then type only the '
        'REPO_NAME. If repository in Organisation type: ORG_NAME/REPO_NAME.'
    ), required=True)
    args = parser.parse_args()
    return args

"""

A Good Organisation is the one which
recognizes all of its contributors. But it can
be hectic at times creating a MARKDOWN file containing
all the collaborators.

This is where the script comes to use.

It automatically generates a simple yet cool
Contributors.MD for your Repository.
The documentation / How to use can be found
here : https://github.com/gabru-md/contributors.md#readme

"""

args = get_args()
g = Github(args.id, args.pwd)
repo = g.get_repo(args.repo)
members = []
names = []
for member in repo.get_collaborators():
    login = str(member.login)
    members.append(login)
    names.append(g.get_user(login).name)

if TEMPLATE_FOLDER in os.listdir(os.getcwd()):
    os.chdir(os.path.join(os.getcwd(), TEMPLATE_FOLDER))

with open('head.rpy', 'r') as content_file:
    head = content_file.read()

with open('foot.rpy', 'r') as content_file:
    foot = content_file.read()

with open('Contributors.md', 'w') as outfile:
    outfile.write(head)
    with open('myfile.rpy') as infile:
        for member, name in zip(members, names):
            replace = {
                '<%= repo %>': args.repo,
                '<%= id %>': member,
                '<%= name %>': name if name is not None else DEFAULT_NAME,
            }
            for line in infile:
                for src, target in replace.iteritems():
                    line = line.replace(src, target)
                outfile.write(line)
            infile.seek(0)
    outfile.write(foot)

sys.stdout.write("Contributors.MD created!\n")
sys.exit()
