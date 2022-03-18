# Import package
from flask import Flask, request, jsonify
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

@app.route('/', methods=['POST'])
def inference():
    # request를 json 형식으로 변수에 할당
    param = request.get_json()

    # Preprocess features from events
    lr = param["lr"]
    lc = param["lc"]
    rc = param["rc"]
    ld = param["ld"]
    rd = param["rd"]
    lnnz = param["lnnz"]
    rnnz = param["rnnz"]

    # Create input feature to use as model input
    input_feature = np.array([[lr,lc,rc,ld,rd,lnnz,rnnz]])
    
    # Apply minmax scaler to input_feature
    input_feature_scaler = minmax_scaler.transform(input_feature)

    # Generate model-specific predictions for input feature
    smsm_dnn_result = smsm_dnn_model.predict(input_feature_scaler)
    smdm_dnn_result = smdm_dnn_model.predict(input_feature_scaler)

    # If sm*dm is better than sm*sm
    if (smdm_dnn_result[0] <= smsm_dnn_result[0]):
        return "smdm"
    # If sm*sm is better than sm*dm
    else:
        return "smsm"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80 ,debug=True)


# # Import package
# from flask import Flask, request, jsonify
# import json
# import numpy as np
# import tensorflow as tf
# import pickle
# from sklearn.preprocessing import MinMaxScaler
# import time

# start = time.time()

# # Load Model
# smsm_dnn_model = tf.keras.models.load_model('/home/hadoop/dos/dos/model/smsm_dnn_model')
# smdm_dnn_model = tf.keras.models.load_model('/home/hadoop/dos/dos/model/smdm_dnn_model')

# # Load Scaler
# minmax_scaler = pickle.load(open('/home/hadoop/dos/dos/scaler/minmax_scaler.pkl','rb'))

# load_model_time = time.time() - start

# app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def inference():
    
#     start = time.time()

#     # request를 json 형식으로 변수에 할당
#     param = request.get_json()

#     # Preprocess features from events
#     lr = param["lr"]
#     lc = param["lc"]
#     rc = param["rc"]
#     ld = param["ld"]
#     rd = param["rd"]
#     lnnz = param["lnnz"]
#     rnnz = param["rnnz"]

#     # Create input feature to use as model input
#     input_feature = np.array([[lr,lc,rc,ld,rd,lnnz,rnnz]])
    
#     # Apply minmax scaler to input_feature
#     input_feature_scaler = minmax_scaler.transform(input_feature)

#     preprocess_data_time = time.time() - start

#     start = time.time()

#     # Generate model-specific predictions for input feature
#     smsm_dnn_result = smsm_dnn_model.predict(input_feature_scaler)
#     smdm_dnn_result = smdm_dnn_model.predict(input_feature_scaler)

#     model_predict_time = time.time() - start

#     # If sm*dm is better than sm*sm
#     if (smdm_dnn_result[0] <= smsm_dnn_result[0]):
#         optim_method = "smdm"
#     # If sm*sm is better than sm*dm
#     else:
#         optim_method = "smsm"

#     result = "load_model_time(ms):" + str(int(load_model_time*1000)) + "\preprocess_data_time(ms):" + str(int(preprocess_data_time*1000)) + "\model_predict_time(ms) : " + str(int(model_predict_time*1000)) + "\\result:" + str(optim_method) 

#     return result

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80 ,debug=True)

