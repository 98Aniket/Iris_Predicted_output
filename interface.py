from flask import Flask,render_template,jsonify
from iris_data.utils import SpeciesPrediction


app = Flask(__name__)

@app.route('/')
def good_day():
    print("Aniket had written this API")
    return "Aniket had written this API"


@app.route('/Predict_result')
def get_Species():

    SepalLengthCm = 5.7
    SepalWidthCm  = 4.4
    PetalLengthCm = 1.5
    PetalWidthCm  = 0.4

    Species_pred = SpeciesPrediction(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    speices = Species_pred.get_predicted_species()

    return jsonify ({"Result" : f"Predicted Species is {speices}"})

if __name__ == "__main__":
    app.run()