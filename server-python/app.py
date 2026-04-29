import logging
import redis
import json
from flask import Flask, request, render_template_string
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
db = redis.Redis(host='redis', port=6379, decode_responses=True)

# Dashboard em HTML/CSS para o vídeo
HTML_DASHBOARD = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Monitor de Performance Sênior</title>
    <meta http-equiv="refresh" content="3">
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f172a; color: #f8fafc; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .container { background: #1e293b; padding: 2rem; border-radius: 1rem; box-shadow: 0 10px 25px rgba(0,0,0,0.5); border: 1px solid #334155; }
        h1 { color: #38bdf8; margin-bottom: 1.5rem; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .card { background: #334155; padding: 1.5rem; border-radius: 0.5rem; text-align: center; min-width: 150px; }
        .label { font-size: 0.875rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em; }
        .value { font-size: 2.5rem; font-weight: bold; color: #22c55e; margin-top: 0.5rem; }
        .footer { margin-top: 2rem; font-size: 0.75rem; color: #64748b; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Monitor em Tempo Real</h1>
        <div class="grid">
            <div class="card">
                <div class="label">Memória RAM</div>
                <div class="value">{{ ram }} MB</div>
            </div>
            <div class="card">
                <div class="label">Goroutines</div>
                <div class="value">{{ threads }}</div>
            </div>
        </div>
        <div class="footer">Última atualização: {{ time }} | Debian 12 Server</div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    data = db.get("last_metrics")
    if data:
        m = json.loads(data)
        return render_template_string(HTML_DASHBOARD, ram=m['ram'], threads=m['threads'], time=m.get('time'))
    return "<h1>Aguardando dados do agente Go...</h1>"

@app.route('/report', methods=['POST'])
def report():
    data = request.json
    data['time'] = datetime.now().strftime("%H:%M:%S")
    db.set("last_metrics", json.dumps(data))
    logger.info(f"Dados Recebidos: {data}")
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
