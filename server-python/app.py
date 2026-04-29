from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/report', methods=['POST'])
def receive_report():
    data = request.json
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    # Simulação de lógica de alerta (nível sênior)
    if data['ram'] > 500: # Exemplo: alerta se RAM > 500MB
        status_msg = "[ALERTA: ALTO USO]"
    else:
        status_msg = "[NORMAL]"

    print(f"[{timestamp}] {status_msg} RAM: {data['ram']}MB | Threads: {data['threads']}")
    
    return jsonify({"status": "received", "server_time": timestamp}), 200

if __name__ == '__main__':
    print("🔥 Servidor Python aguardando métricas na porta 5000...")
    app.run(port=5000)
