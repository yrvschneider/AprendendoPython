…or create a new repository on the command line

echo "# AprendendoPython" >> README.md

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/yrvschneider/AprendendoPython.git
git push -u origin main

…or push an existing repository from the command line
git remote add origin https://github.com/yrvschneider/AprendendoPython.git
git branch -M main
git push -u origin main