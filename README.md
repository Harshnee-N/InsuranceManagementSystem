# 🛡️ Insurance Management System

A web-based **Insurance Management System** developed using **Django**, **HTML**, **CSS**, and **SQLite**. The application enables customers to register, browse insurance policies, purchase policies, and submit insurance claims through a user-friendly interface. Administrators can manage policies and review customer claims.

---

## 📖 Project Overview

The Insurance Management System is designed to simplify the management of insurance services by providing an online platform for policy administration and claim processing.

The application supports customer registration, policy management, policy purchases, and claim submissions while maintaining secure user authentication using Django's built-in authentication system.

---

## ✨ Features

### Customer Management

- User Registration
- Secure Login & Logout
- Customer Profile Management

### Policy Management

- View available insurance policies
- Add insurance policies (Admin)
- Different policy categories:
  - Health Insurance
  - Life Insurance
  - Vehicle Insurance
  - Home Insurance

### Policy Purchase

- Buy insurance policies
- Prevent duplicate active policy purchases
- Track purchased policies

### Claim Management

- Submit insurance claims
- Track claim status
- Admin approval/rejection of claims

### Dashboard

- Customer Dashboard
- Administrator Dashboard
- View purchased policies
- View submitted claims

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Django | Web Framework |
| HTML5 | Frontend |
| CSS3 | Styling |
| SQLite | Database |
| Git | Version Control |
| GitHub | Repository Hosting |

---

## 📂 Project Structure

```
insurance_management_django/
│
├── insurance/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   └── migrations/
│
├── insurance_project/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🗄️ Database Design

The application consists of four main models:

- Customer
- Policy
- CustomerPolicy
- Claim

Relationships:

- A customer can purchase multiple policies.
- A policy can be purchased by multiple customers.
- Customers can submit claims for purchased policies.
- Each claim maintains its approval status.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Harshnee-N/InsuranceManagementSystem.git
```

### Navigate to Project

```bash
cd InsuranceManagementSystem
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## 👩‍💻 Author

**Harshnee N**

GitHub: https://github.com/Harshnee-N
