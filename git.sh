commit_message=`git diff|grep "###"|tr -d '+#'`
echo ${commit_message}

git add --all
git commit -m "${commit_message}"
git push origin master