# Machine_Learning_Projects
Machine Learning First Project


1.[Github Account](https://github.com)

2.[Heroku Account](https://dashboard.heroku.com/login)

3.[VS Code IDE](https://code.visualstudio.com/download)

4.[GIT cli](https://git-scm.com/downloads)

5.[GIT Documentation](https://git-scm.com/docs/gittutorial)



creating conda environment
```
conda create -p venv python==3.7 -y

```

```
conda activate venv/
```

```
pip install -r requirnments.txt
```

To add files to git 
```
git add .
```
OR
```
git add <file_name>
```


>To ignore file or folder from git we can write name  of file/folder in .gitignore file


To check git status
```
git status
```

to check all version maintained by git

```
git log
```

To create version/commit all changes by git
```
git commit -m "message"

```

To check remote url
```
git remote -v
```

To send version/changes to gitHub
```
git push origin main
```


To set CI/CD pipeline in heroku we need 3 information


1.HEROKU_EMAIL = switch2dtsci@gmail.com

2.HEROKU_API_KEY = <-------->

3.HEROKU_APP_NAME = ml-regression-applica


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```

>Note: Image name for docker must be lowercase

to list docker images 
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 99ac5be0922b
```

To check running docker image
```
docker ps
```
To stop docker container
```
docker stop <container_id> 
```