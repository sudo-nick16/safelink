from flask import Flask, jsonify, request
from flask_cors import CORS
import pickle
from utils.extract import extract_features_as_df
 
app = Flask(__name__, static_url_path="/", static_folder="extension")
CORS(app)
 
ai_file = open("ai/model.pickle", "rb")
ai_model = pickle.load(ai_file)

@app.route('/is-safe')
def is_url_safe():
    url = request.args.get("url")
    print("url: ", url)
    if url is None:
        return jsonify({ "error": "url missing in the parameters"}), 400

    features = extract_features_as_df(url)
    print("features: ", features)
    pred = ai_model.predict(features)
    print("pred: ", pred)
    
    if pred[0] == 0:
        return jsonify({ "safe": False, "msg": f"the provided url({url}) is not safe."}), 200
    else:
        return jsonify({ "safe": True, "msg": f"the provided url({url}) is safe."}), 200

 
if __name__ == '__main__':
    app.run("localhost", 3000)
