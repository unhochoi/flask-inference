# flask-inference

- AWS EMR 환경에서, Flask 기반의 Inference Application 구동
- AWS EMR 생성 시, Master device 의 EBS 볼륨 크기는 20GB로 설정 (Tensorflow 용량으로 인해)

  ```
  cd /home/hadoop
  sudo yum install git -y
  git clone https://github.com/unhochoi/flask-inference.git
  cd flask-inference
  ./start.sh
  ```

- 구동 중인 Inference Application 에 Request
  ```
  curl http://127.0.0.1:80/ 
  ```
