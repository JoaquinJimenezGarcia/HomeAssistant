FROM python:3

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install mpg321 gcc libportaudio2 portaudio19-dev python-all-dev python3-all-dev -y

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./run.py"]
