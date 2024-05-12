import smtplib

password = 'gkoo jziv yvvm prcs'
provider = 'foratyhasan24@gmail.com'
with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=provider, password=password)
    connection.sendmail(from_addr=provider, to_addrs='hasanforaty@gmail.com', msg=f"hello")
    connection.quit()
