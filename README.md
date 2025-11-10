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
│
├── healthcareproject/          
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              
│   ├── urls.py                  
│   └── wsgi.py
│
├── db.sqlite3                  
├── manage.py                   
├── requirements.txt             
├── symptom_suggestions.csv      




