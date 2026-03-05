from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    symptom = request.form["symptom"]

    if symptom.lower() == "fever":
        disease = "Possible Flu"
    elif symptom.lower() == "headache":
        disease = "Possible Migraine"
    else:
        disease = "Consult a doctor"

    return f"Predicted result: {disease}"

if __name__ == "__main__":
    app.run(debug=True)