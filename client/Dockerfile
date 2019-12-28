FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

COPY . .

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install python-pyaudio -y
RUN apt-get install libasound-dev portaudio19-dev libportaudiocpp0 -y
RUN apt-get install alsa-utils -y

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./run.py"]