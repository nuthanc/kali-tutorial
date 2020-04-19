import os
from git import Repo

PATH_OF_GIT_REPO = os.getcwd() + "/.git"
commit_message = 'Enumerating SMB'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
    except Exception as e:
        print(e)

git_push()

# git_add_all = os.system("git add --all")
# git_commit = os.system(f"git commit -m 'Update {commit_message}'")
# git_push = os.system("git push origin master")
# print(f"`git push origin master` ran with {git_push} exit status")
