#!/bin/bash

sudo yum update -y
sudo yum install git -y
sudo yum install python3-pip -y

sudo pip3 install virtualenv

# Git Clone 및 접근
cd ~
git clone https://github.com/unhochoi/flask-inference.git
cd flask-inference

# 가상 환경 생성
virtualenv venv
. venv/bin/activate

# 가상 환경 내부에 필요 Library 다운로드
pip3 install -r requirements.txt

# Main.service 실행
sudo cp main.service /etc/systemd/system/
sudo systemctl start main
sudo systemctl enable main
