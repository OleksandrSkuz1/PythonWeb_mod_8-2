from faker import Faker
from connect_with_mongodb import connection
from models import Contact

# Підключення до MongoDB
connection()

# Ініціалізація Faker
fake = Faker()

def create_fake_contacts(num_contacts):
    contacts = []
    for _ in range(num_contacts):
        name = fake.name()
        email = fake.email()
        contact = Contact(full_name=name, email=email)
        contact.save()
        contacts.append(contact)
    return contacts

def send_messages(contacts):
    for contact in contacts:
        send_email(contact)

def send_email(contact):
    # Dummy email sending logic
    print(f"Sending email to {contact.email}")

    # Update contact status
    contact.email_sent = True
    contact.save()

if __name__ == "__main__":
    num_contacts = 10
    contacts = create_fake_contacts(num_contacts)
    send_messages(contacts)
