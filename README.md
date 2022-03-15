# flask-inference

- AWS EMR 의 Worker 노드에, Flask 기반의 Inference Application 구동

  ```
  
  # 루트를 사용하여 설치 진행
  sudo su -

  cd /home/hadoop
  yum install git -y
  
  # flask inference application 관련 repository
  git clone https://github.com/unhochoi/flask-inference-in-emr.git
  
  # model 및 scaler 관련 repository
  git clone https://github.com/kmu-bigdata/dos.git
  
  ./flask-inference-in-emr/start.sh
  ```
- main.service 구동 확인

  ```
  systemctl status main.service
  ```

- 구동 중인 Inference Application 에 Request
  ```
  curl \
  -H "Content-Type: application/json" \
  -X POST "http://마스터퍼블릭DNS:80/" \
  -d '{
    "lr": 97366,
    "lc": 33288,
    "rc": 5958,
    "ld": 0.00056263,
    "rd": 0.13,
    "lnnz": 1823595,
    "rnnz": 25785518
  }' 
  ```

- main.py 는 수정에 따라 실시간으로 반영됨

  ```
  vi /home/hadoop/flask-inference-in-emr/main.py
  ```
