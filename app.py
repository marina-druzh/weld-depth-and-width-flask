from flask import Flask, render_template, request
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import pickle
# from joblib import load

app = Flask(__name__)
tree_model = pickle.load(open('tree_model.pkl', 'rb'))
# tree_model = load('tree_model.joblib')


@app.route(rule='/', methods=["GET", "POST"])
def predict():
    depth, width = "", ""
    if request.method == "POST":
        IW = request.form.get('IW')
        IF = request.form.get('IF')
        VW = request.form.get('VW')
        FP = request.form.get("FP")
        params = [[float(IW), float(IF), float(VW), float(FP)]]
        prediction = np.round(tree_model.predict(params), 2)
        depth, width = prediction[0]
    return render_template("index.html", depth=depth, width=width)


app.run()
