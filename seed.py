from faker import Faker
from connect_with_mongodb import connection
from models import Contact

# Підключення до MongoDB
connection()

# Ініціалізація Faker
fake = Faker()

def seed_contacts(num_contacts):
    for _ in range(num_contacts):
        name = fake.name()
        email = fake.email()
        contact = Contact(full_name=name, email=email)
        contact.save()

if __name__ == "__main__":
    num_contacts = 10  # Кількість фейкових контактів
    seed_contacts(num_contacts)
    print("Seed completed successfully!")
