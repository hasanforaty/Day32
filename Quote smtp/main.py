import smtplib
import datetime as dt
import random

password = 'gkoo jziv yvvm prcs'
provider = 'foratyhasan24@gmail.com'
with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=provider, password=password)
    with open('quotes.txt', mode='r') as file:
        quotes = file.readlines()
        now = dt.datetime.now()
        if now.weekday() == 0:
            quote = random.choice(quotes)
            connection.sendmail(
                from_addr=provider,
                to_addrs='hasanforaty@gmail.com',
                msg=f'Subject:Monday Motivation\n\n{quote}\n'
            )
