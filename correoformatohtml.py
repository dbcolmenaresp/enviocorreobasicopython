# Envio basico de correo electronico
# con archivo adjunto

# Bibliotecas importadas
import os
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Variables del mensaje
emailEmisor = "dbcolmenaresp@gmail.com"
emailClave = "tu clave"
emailReceptor = "nacarybenavidesdimas@gmail.com"
asunto = "Este es un correo enviado automaticamente con python"

cuerpoHTML = f"""
<html>
<body>
    <p>Hola <i>{emailReceptor}</i><br>
    Este es un <b>nuevo mensaje</b>
    </p>
</body>
</html>
"""

# Contenido del mensaje en HTML
mensajeHTML = MIMEText(cuerpoHTML, "html")

# Datos de configuracion del mensaje de correo
em = MIMEMultipart("alternative")
em['From'] = emailEmisor
em['To'] = emailReceptor
em['Subject'] = asunto
em.attach(mensajeHTML)


# Envio del mensaje
contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(emailEmisor,emailClave)
    smtp.sendmail(emailEmisor, emailReceptor, em.as_string())
