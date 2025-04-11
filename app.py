from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Cargar modelo KMeans y StandardScaler
with open("Models/kmeans_model.pkl", "rb") as f:
    kmeans = pickle.load(f)

with open("Models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Diccionario para traducir número de cluster a categoría
cluster_labels = {
    0: "Principiante",
    1: "Avanzado",
    2: "Intermedio"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Obtener datos del formulario
            sex = float(request.form["Sex"])
            bodyweight = float(request.form["BodyweightKg"])
            squat = float(request.form["BestSquatKg"])
            bench = float(request.form["BestBenchKg"])
            deadlift = float(request.form["BestDeadliftKg"])
            total = float(request.form["TotalKg"])

            # Formar vector y escalarlo
            input_data = np.array([[sex, bodyweight, squat, bench, deadlift, total]])
            input_scaled = scaler.transform(input_data)

            # Predecir el cluster
            cluster = int(kmeans.predict(input_scaled)[0])
            label = cluster_labels.get(cluster, "Desconocido")

            return render_template("index.html", result=f"Clasificación asignada: {label}")
        except Exception as e:
            return render_template("index.html", result=f"Error al procesar los datos: {e}")

    return render_template("index.html", result=None)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)