# takes one python image called 3.8...
FROM python:3.8-slim-buster

#This line is like adding additional LEGO pieces or tools that are needed, which in this case is the AWS command line interface.
RUN apt update -y && apt install awscli -y
# creates one app directory where the model will be built
WORKDIR /app

# it copies all the code and puts it inside it
COPY . /app
# installs requirements
RUN pip install -r requirements.txt

# This is specifying how people should interact with your LEGO model, by running app.py with Python
CMD ["python3", "app.py"]