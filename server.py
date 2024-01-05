from flask import Flask, jsonify, redirect, request
from flask_cors import CORS
import pickle
from utils.extract import extract_features_as_df
 
app = Flask(__name__, static_url_path="/", static_folder="extension")
CORS(app)
 
ai_file = open("ai/model.pickle", "rb")
ai_model = pickle.load(ai_file)

@app.route('/')
def open_ui():
    return redirect('/index.html')

@app.route('/is-safe')
def is_url_safe():
    url = request.args.get("url")
    if url is None:
        return jsonify({ "error": "url missing in the parameters"}), 400

    try:
        features = extract_features_as_df(url)
        pred = ai_model.predict(features)

        if pred[0] == 0:
            return jsonify({ "safe": False, "msg": f"the provided url({url}) is not safe."}), 200
        else:
            return jsonify({ "safe": True, "msg": f"the provided url({url}) is safe."}), 200
    except:
            return jsonify({ "error": "error while predicting." }), 500
