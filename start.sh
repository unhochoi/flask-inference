#!/bin/bash

# 필요 패키지 다운로드
yum update -y
yum install python3-pip -y
pip3 install virtualenv

# venv 라는 이름의 가상 환경 생성
virtualenv venv
# venv 가상 환경 활성화
. venv/bin/activate

#python -m pip install --upgrade pip

# 가상 환경 내부에 필요 패키지 다운로드
pip3 install -r /home/hadoop/flask-inference-in-emr/requirements.txt

#sudo pip3 install tensorflow==2.5.0 --use-feature=2020-resolver

# Flask Application 실행
cp /home/hadoop/flask-inference-in-emr/main.service /etc/systemd/system/
systemctl daemon-reload
systemctl start main
systemctl enable main
systemctl status main
