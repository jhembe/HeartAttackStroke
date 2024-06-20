from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the model
with open('XGBmodel.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the ideal values
ideal_values = {
    'age': 30,
    'sex':(0,1),
    'cp': 3,
    'trtbps': 120,
    'chol': 200,
    'fbs': (0,1),
    'restecg': 0,
    'thalachh': None,  # This will be calculated as 220 - age
    'exng': 0,
    'oldpeak': 0,
    'slp': 0,
    'caa': 0,
    'thall': 0
}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    required_features = [
        'age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 
        'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 
        'caa', 'thall'
    ]

    # Extracting features from the request
    try:
        features = [data[feature] for feature in required_features]
    except KeyError as e:
        return jsonify({'error': f'Missing feature: {str(e)}'}), 400
    
    # Convert features to a numpy array and reshape for prediction
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array).tolist()

    result = {'prediction': prediction}

    # If prediction is positive (1), determine the probable cause
    if prediction[0] == 1:
        deviations = {}
        for feature, value in zip(required_features, features):
            if feature == 'thalachh':
                ideal_value = 220 - data['age']
                if value != ideal_value:
                    deviations[feature] = value
            elif feature == 'fbs':
                if not (ideal_values[feature][0] <= value <= ideal_values[feature][1]):
                    deviations[feature] = value
            elif feature == 'trtbps' or feature == 'chol' or feature == 'age':
                if value >= ideal_values[feature]:
                    deviations[feature] = value
            else:
                if value != ideal_values[feature]:
                    deviations[feature] = value

        result['deviations'] = deviations

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
