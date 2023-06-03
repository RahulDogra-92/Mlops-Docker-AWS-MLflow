# slim-buster is light weighted linux based os system
FROM python:3.8-slim-buster 

# creating new folder
WORKDIR /flask-docker    

# I don't want to see wwarning/errors like "upgrade pip"
RUN python3 -m pip install --upgrade pip

# 1st one will copy files from local machine to container in flask-docker folder with the same name requirement.txt
COPY requirements.txt requirement.txt

# read contents inside requirement.txt and keep installing all packages
RUN pip3 install -r requirement.txt

# [1st dot] - copy all files from local to [2nd dot] - copy to working directory flask-docker
COPY . .

# final command to run flask application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

