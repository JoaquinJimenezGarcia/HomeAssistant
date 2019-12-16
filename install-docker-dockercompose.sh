!#/bin/bash

curl -sSL https://get.docker.com | sh
sudo usermod -aG docker pi
sudo apt-get install libffi-dev libssl-dev -y
sudo apt-get install -y python python-pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && sudo python3 get-pip.py
sudo pip3 install docker-compose

 