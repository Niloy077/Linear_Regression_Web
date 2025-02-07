import matplotlib
matplotlib.use('Agg')  # Use non-GUI Agg backend
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import numpy as np
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Example simple model: Linear Regression y = 2x + 1
        x = np.linspace(0, 10, 100)  # Sample data points
        y = 2 * x + 1

        # Create a plot
        plt.figure(figsize=(6,4))
        plt.plot(x, y, label="y = 2x + 1")
        plt.title("Linear Regression: y = 2x + 1")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()

        # Save the plot to a file
        plot_filename = "plot.png"
        plot_path = os.path.join("static", plot_filename)
        plt.savefig(plot_path)
        plt.close()  # Close the plot to avoid memory leaks

        return render_template("index.html", plot_url=plot_filename)
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)
