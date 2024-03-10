# Envio basico de correo electronico

# Bibliotecas importadas
import os
from email.message import EmailMessage
import ssl
import smtplib

# Variables del mensaje
emailEmisor = "dbcolmenaresp@gmail.com"
emailClave = "clave de gmail"
emailReceptor = "nacarybenavidesdimas@gmail.com"
asunto = "Este es un correo enviado automaticamente con python"
cuerpo = """
Este es un correo enviado automaticamente de prueba
Por favor avise al momento de recibirlo
Gracias
"""

#
em = EmailMessage()
em['From'] = emailEmisor
em['To'] = emailReceptor
em['Subject'] = asunto
em.set_content(cuerpo)

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(emailEmisor,emailClave)
    smtp.sendmail(emailEmisor, emailReceptor, em.as_string())


