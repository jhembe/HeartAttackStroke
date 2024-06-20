from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app);

#load the model
with open('XGBmodel.pkl','rb') as file:
    model = pickle.load(file)
# model = pickle.load(open("XGBmodel.pkl","rb")) # open model in read mode

@app.route('/predict',methods=['POST'])
def predict():
    data = request.json
    # data = {
    #   'age': 60,
    #   'sex': 1,
    #   'cp': 3,
    #   'trtbps': 145,
    #   'chol': 233,
    #   'fbs': 1,
    #   'restecg': 0,
    #   'thalachh': 150,
    #   'exeng': 0,
    #   'oldpeak': 2.3,
    #   'slp': 0,
    #   'caa': 0,
    #   'thall': 1,
    #   'prediction': 1,
    # };
    required_features = [
        'age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 
        'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 
        'caa', 'thall'
    ]

    # extracting features from the request
    try:
        features = [data[feature] for feature in required_features]
    except KeyError as e:
        return jsonify({'error': f'Missing feature : {str(e)}'}),400
    
    # converty features to a numpy array and reshape for prediction 
    features_array = np.array(features).reshape(1,-1)
    prediction = model.predict(features_array)
    if(prediction == 1):
        result = "You may have a heart attack"
    elif result = "You do not have a heart attaco"

    print(prediction)

    return jsonify({'prediction':prediction})


predict()

if __name__ == '__main__':
    app.run(debug=True)
