#!/bin/bash

# 필요 패키지 다운로드
sudo yum update -y
sudo yum install git -y
sudo yum install python3-pip -y
sudo pip3 install virtualenv

# Git Clone 및 접근
cd ~
git clone https://github.com/unhochoi/flask-inference.git
cd flask-inference

# venv 라는 이름의 가상 환경 생성
virtualenv venv
# venv 가상 환경 활성화
. venv/bin/activate

# 가상 환경 내부에 필요 패키지 다운로드
pip3 install -r requirements.txt

# Flask Application 실행
sudo cp main.service /etc/systemd/system/
sudo systemctl start main
sudo systemctl enable main
