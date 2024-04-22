from connect_with_mongodb import connection
from models import Contact

# Підключення до MongoDB
connection()

def process_messages():
    # Отримання невідправлених контактів
    contacts = Contact.objects(email_sent=False)

    # Відправка повідомлень
    for contact in contacts:
        send_email(contact)

def send_email(contact):
    # Dummy email sending logic
    print(f"Sending email to {contact.email}")

    # Оновлення статусу відправки
    contact.email_sent = True
    contact.save()

if __name__ == "__main__":
    process_messages()

