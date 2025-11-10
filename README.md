# 🩺 Healthcare Project

A simple Django-based CRUD app for managing patient records.

## 🩺 Project Overview

The **Healthcare Management System** is a Django-based CRUD (Create, Read, Update, Delete) web application designed to simplify the process of managing patient information.  
It allows healthcare staff to easily record, update, and view patient details such as name, age, and symptoms — all through a user-friendly interface.

This project demonstrates the use of Django’s powerful Model-View-Template (MVT) architecture, form handling, and authentication system to build a complete full-stack web solution.

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

## 📸 Screenshots

[Home Page]<img width="1270" height="420" alt="homepage" src="https://github.com/user-attachments/assets/856da1f2-0ec3-4356-ad66-d5d6786477bf" />
[Update Patient details page]<img width="1241" height="550" alt="updatepage" src="https://github.com/user-attachments/assets/b3462326-16e8-49d3-ae8d-1efc002da0f7" />
[Add patient details page]<img width="1194" height="521" alt="addpage" src="https://github.com/user-attachments/assets/87f3605c-dff8-44a2-b77d-f8607fef3940" />

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




