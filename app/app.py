from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the saved model
print(" Loading saved model for Flask app...")
model_data = joblib.load("model/savedmodel.pth")
model = model_data["model"]

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Placeholder response for assignment
    return "Prediction Placeholder — Model is Loaded Successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
