# 🩺 Healthcare Project

A simple Django-based CRUD app for managing patient records.

## 🚀 Features
- Add, edit, delete, and view patient records
- It will take patient symptoms and show some suggestions!
- Clean and responsive design
- Authentication system for secure access

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/healthcareproject.git
   cd healthcareproject


## 📸 Screenshots

[Home Page]<img width="1270" height="420" alt="homepage" src="https://github.com/user-attachments/assets/856da1f2-0ec3-4356-ad66-d5d6786477bf" />
[Update Patient details page]<img width="1241" height="550" alt="updatepage" src="https://github.com/user-attachments/assets/b3462326-16e8-49d3-ae8d-1efc002da0f7" />
[Add patient details page]<img width="1194" height="521" alt="addpage" src="https://github.com/user-attachments/assets/87f3605c-dff8-44a2-b77d-f8607fef3940" />

## 🗂️ Project Structure

healthcareproject/
│
├── crudapp/                     # Main Django app
│   ├── migrations/              # Database migration files
│   ├── templates/               # HTML templates
│   │   ├── add_patient.html
│   │   ├── edit_patient.html
│   │   ├── patient_list.html
│   │   └── login.html
│   ├── static/                  # CSS
│   │   └── style.css
│   │  
│   │   
│   │   
│   ├── forms.py                 # Django forms
│   ├── models.py                # Database models
│   ├── urls.py                  # App-level URL routing
│   ├── views.py                 # View logic
│   └── admin.py                 # Admin site setup
│
├── healthcareproject/           # Project configuration folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              # Main settings file
│   ├── urls.py                  # Root URL routing
│   └── wsgi.py
│
├── db.sqlite3                   # SQLite database file
├── manage.py                    # Django management script
├── requirements.txt             # List of dependencies
├── symptom_suggestions.csv      # Extra data file




