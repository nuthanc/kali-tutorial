import os
from git import Repo

PATH_OF_GIT_REPO = os.getcwd() + "/.git"
commit_message = 'Update README'
repo = Repo(PATH_OF_GIT_REPO)

def git_push():
    try:
        repo.git.add(update=True)
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
    except Exception as e:
        print(e)

git_push()

