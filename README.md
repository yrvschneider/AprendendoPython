**** Configuração para quando não estiver configurado na maquina ****

git config --global user.name "nome de usuário do github"
git config --global user.email "email utilizado no github"
git init
git status
git add .
git commit -m "first commit"
git remote rm origin - Se der faltal erro origem existente
git remote add origin https://github.com/yrvschneider/AprendendoPython.git
git push -u origin main

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