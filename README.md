# Contacts Manager (Django CRUD Application)

A simple web application built with Django that allows users to manage contacts with basic CRUD (Create, Read, Update, Delete) operations.

This project is developed as part of a **Web Developer CRUD Assignment**.

---

## 🚀 Features

### Must Have
- Add a new contact
- View a list of contacts
- View single contact details
- Edit an existing contact
- Soft delete a contact
- Form validation:
  - Required fields
  - Valid email format
  - Phone number length (10–15 digits)
- Clean and simple UI (table + form)
- Clear error messages (e.g. duplicate email)
- Data persistence using SQLite database

### Bonus Implemented
- Search contacts by name or email
- Unit tests (basic)

---

## 🛠️ Tech Stack

- Python 3
- Django 5
- SQLite
- HTML, Bootstrap (UI)

---

## 📂 Project Structure

contacts_manager/
├── manage.py
├── contacts_manager/
├── contacts/
├── templates/
│ └── contacts/
├── static/
├── README.md
└── requirements.txt

Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/contacts-manager.git
cd contacts-manager

2️⃣ Create a Virtual Environment
python -m venv venv

venv\Scripts\activate

3️⃣ Install Dependencies
pip install django

4️⃣ Run Database Migrations
python manage.py migrate

5️⃣ Create Superuser (Optional)
python manage.py createsuperuser

▶️ Run Instructions
python manage.py runserver
Open in Browser
http://127.0.0.1:8000/

🧪 Run Tests
python manage.py test
