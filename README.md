# 🖥️ Distributed System Monitor | Go & Python

Status: 🟢 Operacional
Arquitetura: Agente-Servidor (Client-Server)

## 📖 Sobre o Projeto
Este projeto foi desenvolvido para demonstrar a integração entre linguagens de alta performance (*Go) e linguagens de processamento rápido de dados (Python*). O objetivo é monitorar a saúde de servidores Debian em tempo real.

## 🛠️ Stack Técnica
- *Go (Agente):* Responsável pela coleta de baixo nível de CPU, RAM e Goroutines. Escolhido pela sua eficiência em concorrência.
- *Python/Flask (Server):* Atua como o cérebro da operação, recebendo métricas e simulando um sistema de alerta inteligente.
- *Ambiente:* Debian 12 Linux.

## 🚀 Como este projeto me torna um dev melhor?
1. *Concorrência:* Entendimento de como o Go gerencia threads leves.
2. *Interoperabilidade:* Comunicação entre diferentes stacks via protocolos HTTP/JSON.
3. *Linux Skills:* Gerenciamento de processos e ambiente via terminal puro.

---
Projeto desenvolvido para portfólio de entrada no mercado de tecnologia.

## 📖 Sobre o Projeto
Este é um monitor de performance distribuído, projetado para demonstrar a integração entre linguagens de alta performance (*Go) e processamento flexível de dados (Python/Flask*). O sistema coleta métricas críticas de servidores Linux em tempo real.

## 🛠️ Stack Técnica
* *Go (Agente):* Coleta de baixo nível de CPU, RAM e Goroutines. Escolhido pela alta eficiência em concorrência.
* *Python/Flask (Server):* Backend responsável por receber as métricas, processar alertas e servir os dados.
* *Arquitetura:* Agente-Servidor (Client-Server) via protocolos HTTP/JSON.

## 🚀 Como Executar

### 1. Servidor (Python)
```bash
# Navegue até a pasta do servidor
cd monitor-performance/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
