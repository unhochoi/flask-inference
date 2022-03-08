# Import package
from flask import Flask, request
import json
import numpy as np
import tensorflow as tf
import pickle
from sklearn.preprocessing import MinMaxScaler

# Load Model
smsm_dnn_model = tf.keras.models.load_model('/home/hadoop/dos/dos/model/smsm_dnn_model')
smdm_dnn_model = tf.keras.models.load_model('/home/hadoop/dos/dos/model/smdm_dnn_model')

# Load Scaler
minmax_scaler = pickle.load(open('/home/hadoop/dos/dos/scaler/minmax_scaler.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def basic():
    # request를 json 형식으로 변수에 할당
    param = request.get_json()
    return "hello"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80 ,debug=True)
