# 📧 Envio Automático de E-mails com Python

Este projeto permite enviar e-mails de forma automatizada usando **Python** e o servidor SMTP do Gmail.  
Ele suporta **vários destinatários**, personalização de mensagens e armazenamento seguro de credenciais via `.env`.

---

## 🚀 Funcionalidades
- Envio de e-mails via Gmail usando **SMTP seguro (SSL)**.
- Suporte para **múltiplos destinatários**.
- Armazenamento de credenciais em **arquivo `.env`** para segurança.
- Fácil de adaptar para anexos ou mensagens HTML.

---

## 📦 Requisitos
- Python 3.8 ou superior
- Conta do Gmail com **senha de aplicativo**
- Bibliotecas Python:
  ```bash
  pip install python-dotenv
  
🔑 Criando a Senha de App no Gmail
Acesse Segurança da Conta Google.
Ative a Verificação em duas etapas.
Vá em Senhas de app.
Escolha E-mail e nomeie como Python.
Copie a senha gerada (16 caracteres) e guarde.

EMAIL_USER=seuemail@gmail.com
EMAIL_PASS=sua-senha-de-app

import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

remetente = os.getenv("EMAIL_USER")
senha = os.getenv("EMAIL_PASS")

# Lista de destinatários
destinatarios = ["pessoa1@example.com", "pessoa2@example.com"]

mensagem = MIMEText("Olá! Este é um e-mail enviado via Python 😎")
mensagem["Subject"] = "Teste de Automação"
mensagem["From"] = remetente
mensagem["To"] = ", ".join(destinatarios)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
    servidor.login(remetente, senha)
    servidor.sendmail(remetente, destinatarios, mensagem.as_string())

print("E-mail enviado com sucesso!")

.env

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

# Carrega variáveis
load_dotenv()
remetente = os.getenv("EMAIL_USER")
senha = os.getenv("EMAIL_PASS")
destinatarios = ["pessoa1@example.com", "pessoa2@example.com"]

# Cria mensagem multipart
mensagem = MIMEMultipart()
mensagem["From"] = remetente
mensagem["To"] = ", ".join(destinatarios)
mensagem["Subject"] = "Relatório com Anexo"

# Corpo em HTML
html = """
<h2>Relatório Semanal 📊</h2>
<p>Segue o relatório em anexo.</p>
<p><b>Data:</b> 05/08/2025</p>
"""
mensagem.attach(MIMEText(html, "html"))

# Adicionando anexo
arquivo = "relatorio.pdf"  # nome do arquivo local
with open(arquivo, "rb") as f:
    parte = MIMEBase("application", "octet-stream")
    parte.set_payload(f.read())
encoders.encode_base64(parte)
parte.add_header(
    "Content-Disposition",
    f"attachment; filename={os.path.basename(arquivo)}"
)
mensagem.attach(parte)

# Envia e-mail
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
    servidor.login(remetente, senha)
    servidor.sendmail(remetente, destinatarios, mensagem.as_string())

print("E-mail HTML com anexo enviado com sucesso!")

📌 Melhorias Futuras
Ler lista de destinatários de arquivo .csv
Agendar envio automático com schedule
Integrar com planilhas do Google Sheets

👨‍💻 Autor
Desenvolvido por Gabriel Andrade
