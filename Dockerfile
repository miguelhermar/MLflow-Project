# takes one python image called 3.8...
FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
# creates one app directory
WORKDIR /app

# it copies all the code and puts it inside it
COPY . /app
# installs requirements
RUN pip install -r requirements.txt

# launches app.py
CMD ["python3", "app.py"]