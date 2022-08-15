l=[
    {'number':1,'title':'a','city':'arak'},
    {'number':2,'title':'b','city':'tehran'},
    {'number':3,'title':'c','city':'karaj'},
]

context = ''
for i in l :
    msg +=f"* شماره نیاز: {i['number']} -- عنوان: {i['title']} -- شهر: {i['city']} \n"



from email.message import EmailMessage

contacts = ['YourAddress@gmail.com', 'test@example.com']

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = "EMAIL_ADDRESS"
msg['To'] = contacts

msg.set_content(context)


# smtp.send_message(msg)