import smtplib
server=smtplib.SMTP('smtp.gmail.com')
server.starttls()
server.login('nameeth33@gmail.com','---------')
msg='hello'
server.sendmail('nameeth33@gmail.com','nameeth33@gmail.com',msg)
print(' send message')
server.quit()

