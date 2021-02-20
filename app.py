# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:08:41 2021

@author: stone
"""
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from joblib import load
app = Flask(__name__)
model = pickle.load(open('xgb_model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('front_end.html')

sc1=load('stan_scaler.bin')
@app.route("/predict", methods=['POST'])
def predict():
    if request.method=='POST':
        #print('it has entered post')
        n_unsec = float(request.form['n_unsec'])
        age=float(request.form['age'])
        debt_ratio=float(request.form['debt_ratio'])
        income=float(request.form['income'])
        n_open_lines=int(request.form['n_open_lines'])
        n_90=int(request.form['n_90'])
        n_real=int(request.form['n_real'])
        n_60_89=int(request.form['n_60_89'])
        n_dep=int(request.form['n_dep'])
        n_30_59=int(request.form['n_30_59'])
        prediction=model.predict(sc1.transform(np.array([[n_unsec,age,n_30_59,debt_ratio,income,n_open_lines,n_90,n_real,n_60_89,n_dep]])))
        output=prediction[0]
        #print(output)
    
        
        if output==1:
            return render_template('front_end.html',prediction_texts="Customer will default")
        else:
            return render_template('front_end.html',prediction_texts="Customer won't default")
    else:
        return render_template('front_end.html')

if __name__=="__main__":
    app.run(debug=True)