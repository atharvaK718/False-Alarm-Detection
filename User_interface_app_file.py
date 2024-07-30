from flask import Flask, jsonify, request
import joblib
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
import os
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# Path to the Excel file and model
excel_file = 'False_Alarm_Cases.xlsx'
model_file = 'trained_model.pkl'

@app.route('/train', methods=['GET'])
def train():
    try:
        # Check if the Excel file exists
        if not os.path.exists(excel_file):
            app.logger.error('Excel file not found.')
            return 'Excel file not found.', 404
        
        # Load data from Excel file
        df_train = pd.read_excel(excel_file)
        df_train = df_train.iloc[:, 1:8]
        X = df_train.iloc[:, 0:6]
        y = df_train['Spuriosity Index(0/1)']
        
        # Train the model
        classifier = GaussianNB()
        classifier.fit(X, y)
        joblib.dump(classifier, model_file)
        
        app.logger.info('Model has been trained and saved.')
        return 'Model has been trained and saved.'
    except Exception as e:
        app.logger.error(f'Error during training: {str(e)}')
        return 'Internal Server Error', 500

@app.route('/test', methods=['POST'])
def test():
    try:
        # Check if the model file exists
        if not os.path.exists(model_file):
            app.logger.error('Model not found. Train the model first.')
            return 'Model not found. Train the model first.', 404
        
        # Load the trained model
        clf = joblib.load(model_file)
        
        # Get JSON request data
        request_data = request.get_json()
        
        try:
            a = request_data['Ambient Temperature']
            b = request_data['Calibration']
            c = request_data['Unwanted substance deposition']
            d = request_data['Humidity']
            e = request_data['H2S Content']
            f = request_data['detected by']
        except KeyError as e:
            app.logger.error(f'Missing field in request data: {str(e)}')
            return jsonify({'error': f'Missing field in request data: {str(e)}'}), 400
        
        # Prepare data for prediction
        l = [a, b, c, d, e, f]
        narr = np.array(l).reshape(1, -1)
        df_test = pd.DataFrame(narr, columns=['Ambient Temperature', 'Calibration', 'Unwanted substance deposition',
                                              'Humidity', 'H2S Content', 'detected by'])
        
        # Make a prediction
        ypred = clf.predict(df_test)
        result = 'Danger' if ypred == 1 else 'No Danger'
        
        app.logger.info('Prediction made successfully.')
        return jsonify({'Recommendation': result})
    except Exception as e:
        app.logger.error(f'Error during prediction: {str(e)}')
        return 'Internal Server Error', 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
