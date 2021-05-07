FROM python:3

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install cmake python3-opencv libopenblas-dev liblapack-dev -y

COPY requirements.txt ./
#RUN pip install face_recognition -vvv
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./run.py"]
