#!/usr/bin/env python
# -*- coding: utf-8 -*-


######################################## 
"""LIBRARIES"""
import sys
import subprocess
import smtplib
from subprocess import check_output
######################################## 

######################################## 
"""LOAD ARGS"""

neoSub="subjet del correo"




######################################## 
"""EMAIL SETTINGS"""
sender = 'emailaccountc@gmail.com'
receivers = ['hkeyland@gmail.com']
header= """From: NAMESENDER <emailaccountc@gmail.com>
To: <hkeyland@gmail.com>
Subject: Curso nuevo- """+neoSub


message = """
Resultados del anlisis realizado

"""

info=message
body=header+info


##START SERVER
"""SIMPLE"""
#server = smtplib.SMTP('localhost')
#server.sendmail(sender, receivers, body)
#server.quit()
"""GMAIL"""
username = 'emailaccountc@gmail.com'
password = 'PASSWORD*****'
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(sender, receivers, body)
server.quit()
