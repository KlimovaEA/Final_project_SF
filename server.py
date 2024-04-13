from flask import Flask, request, jsonify
import pickle
import numpy as np

# загружаем модель из файла
with open('C:\\Users\\user\\Skillfactory\\IDE\\Final_projec\\Data\\web\\models\\best_rf_regressor_model.pkl', 'rb') as pkl_file:
    best_rf_regressor_model = pickle.load(pkl_file)

# создаём приложение
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    features = np.array(request.json)
    features = features.reshape(1, 15)
    prediction = np.round(best_rf_regressor_model.predict(features))
    return  jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    
    app.run('localhost', 5000)