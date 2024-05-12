import pandas
import datetime as dt
import random
import smtplib

password = 'gkoo jziv yvvm prcs'
provider = 'foratyhasan24@gmail.com'
now = dt.datetime.now()
births = (pandas.read_csv('birthdays.csv', )
          .query('month == @now.month and day == @now.day')
          .to_dict(orient="records"))
for birth in births:
    letter_name = f'letter_{random.choice(range(1, 4))}'
    with open(f'./letter_templates/{letter_name}.txt', 'r') as letter:
        name = birth.get('name')
        letter_template = letter.read()
        letter_template = letter_template.replace('[NAME]', name)
        header = f'Happy birthday {name}'
        email = birth.get('email')
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(user=provider, password=password)
            print(f'sending email to {name} ......')
            server.sendmail(
                from_addr=provider,
                to_addrs=email,
                msg=f'Subject:{header}\n\n{letter_template}\n'
            )
