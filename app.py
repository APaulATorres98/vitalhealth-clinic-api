from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            doctor TEXT NOT NULL,
            appointment_date TEXT NOT NULL
        )
    ''')
    cursor.execute("INSERT OR IGNORE INTO appointments (id, patient_name, doctor, appointment_date) VALUES (1, 'Juan Pérez', 'Dra. Gómez', '2026-09-10')")
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return jsonify({"message": "VitalHealth Clinic API v1.0"})

@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, patient_name, doctor, appointment_date FROM appointments")
    rows = cursor.fetchall()
    conn.close()
    
    appointments = [{"id": r[0], "patient": r[1], "doctor": r[2], "date": r[3]} for r in rows]
    return jsonify(appointments)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
