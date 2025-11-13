# 🩺 Healthcare Project

A simple Django-based CRUD app for managing patient records.

## 🩺 Project Overview

The Healthcare Management System is a Django-based CRUD (Create, Read, Update, Delete) web application designed to get some suggestions for common health issues.
It allows user to easily enter required credentials such as name, age, and symptoms — all through a user-friendly interface. On the bases of symptom it will provide some suggestions.

---

### ⚙️ Core Features
- ➕ Add new patient records  
- ✏️ Edit existing records  
- ❌ Delete patient entries  
- 👀 View all patient details in a structured list  
- 🔐 User authentication (Login / Logout)  
- 💡 Optional feature: Symptom-based suggestions using CSV data
  
---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/healthcareproject.git
   cd healthcareproject

---



## 🗂️ Project Structure

healthcareproject/
│
├── crudapp/                     
│   ├── migrations/              
│   ├── templates/              
│   │   ├── add_patient.html
│   │   ├── edit_patient.html
│   │   ├── patient_list.html
│   │   └── login.html
│   │   └── registration.html
│   ├── static/                 
│   │   └── style.css 
│   ├── forms.py
│   ├── models.py                
│   ├── urls.py                  
│   ├── views.py                 
│   └── admin.py                 
├── healthcareproject/          
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              
│   ├── urls.py                  
│   └── wsgi.py
├── db.sqlite3                  
├── manage.py                             
├── symptom_suggestions.csv      




