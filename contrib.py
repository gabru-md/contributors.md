"""
@Author : Manish Devgan
@Github : https://github.com/gabru-md
@Language : Python 2.7
"""

import os
import sys
import argparse
from github import Github

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
    parser = argparse.ArgumentParser(description='To create collaborators for the repository\nYou must have push access to the repository.\nWithout push access this will not work!')

    parser.add_argument('-id', type=str,
                        help='ID or Username for Github',required=True)
    parser.add_argument('-pwd',type=str,help='Password for Github',required=True)

    parser.add_argument('-repo', type=str,help='Name of the Repository\nIf repository in id then type only the REPO_NAME\nIf repository in Organisation type: ORG_NAME/REPO_NAME',required=True)
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

uid = args.id
pwd = args.pwd
repository = args.repo


g = Github(uid,pwd)
repo = g.get_repo(repository)
try:
    collaborators = repo.get_collaborators()

    members = []
    names = []
    for member in collaborators:
            members.append(str(member.login))
            names.append(g.get_user(str(member.login)).name)
except Exception as e:
    sys.exit(e)

cwd = os.getcwd()

list_dir = os.listdir(cwd)

folder = 'rpy'

if folder in list_dir:
    os.chdir(os.getcwd() + "/" + folder)

cwd = os.getcwd()

with open('head.rpy', 'r') as content_file:
    head = content_file.read()


with open('foot.rpy', 'r') as content_file:
    foot = content_file.read()

uid = '<%= id %>'
repo = '<%= repo %>'
name = '<%= name %>'
replace = {repo:repository,uid:members,name:names}
collaborators = replace[uid]

with open('Contributors.md', 'w') as outfile:
    outfile.write(head)
    for i in range(len(replace[uid])):
        with open('myfile.rpy') as infile:
            for line in infile:
                for src, target in replace.iteritems():
                    if src == repo:
                        line = line.replace(src, target)
                    elif src == uid:
                        line = line.replace(src,collaborators[i])
                    elif src == name:
                        line = line.replace(src,names[i])
                outfile.write(line)
    outfile.write(foot)


sys.exit("Contributors.MD created!")