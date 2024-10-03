from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configura tu conexión a la base de datos
db_config = {
    "host": "bu05lnrbsbg3sfxjqy8u-mysql.services.clever-cloud.com",
    "user": "u6edweftcokchocx",
    "password": "6VP2sbN6WXyvalRAfXDI",
    "database": "bu05lnrbsbg3sfxjqy8u",
}


@app.route("/data", methods=["POST"])
def insert_data():
    if request.is_json:
        data = request.get_json()
        campo1 = data.get("campo1")
        campo2 = data.get("campo2")

        if campo1 is None:
            return jsonify({"status": "error", "message": "campo1 is required"}), 400
        if campo2 is None:
            return jsonify({"status": "error", "message": "campo2is required"}), 400

        # Aquí va tu lógica para insertar en la base de datos
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO consumos (ldr_value,pot_value) VALUES (%s,%s)", (campo1,campo2,)
            )
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"status": "success"}), 201
        except mysql.connector.Error as err:
            return jsonify({"status": "error", "message": str(err)}), 500
    else:
        return jsonify({"status": "error", "message": "Request must be JSON"}), 400


app.run(host="0.0.0.0", port=5000)
