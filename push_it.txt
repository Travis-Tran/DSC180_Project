git add .

echo "commit msg"
read commit_msg
git commit -m "$commit_msg"

git push