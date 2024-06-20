from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the model
with open('XGBmodel.pkl', 'rb') as file:
    model = pickle.load(file)

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

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
