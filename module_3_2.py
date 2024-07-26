def send_email(message=1, recipient="we", sender = "university.help@gmail.com"):
    if (recipient.find('@') or sender.find('@')) !=-1:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    else:
        print('Good')
    print(recipient.find('@') != -1)
print(send_email())