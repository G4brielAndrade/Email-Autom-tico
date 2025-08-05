import smtplib
from email.mime.text import MIMEText

remetente = "@gmail.com"
senha ="" # use senha de app
destinatarios = ["email@gmail.com"]

mensagem = MIMEText("Olá! Esse é um e-mail enviado via script Python, Gabriel Andrade, criador😎")
mensagem["Subject"] = "automação de emails"
mensagem["From"] = remetente
mensagem["To"] = ", ".join(destinatarios)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
    servidor.login(remetente, senha)
    servidor.sendmail(remetente, destinatarios, mensagem.as_string())

print("E-mail enviado com sucesso!")
