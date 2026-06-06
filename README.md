# 🔐 Secure Login System

A secure web-based authentication system developed using **Python Flask**, **MariaDB**, **SQLAlchemy**, and **bcrypt**. This project demonstrates modern authentication techniques, secure password storage, session management, and web security best practices.

---

## Project Overview

The Secure Login System is a cybersecurity-focused web application that allows users to register, authenticate, and manage sessions securely. The system implements password hashing using bcrypt and stores user credentials in a MariaDB database.

The primary objective of this project is to demonstrate secure authentication mechanisms while following secure coding principles and protecting against common web-based attacks.

---

## Objectives

* Implement secure user registration and login functionality.
* Store passwords securely using bcrypt hashing.
* Prevent duplicate account creation.
* Manage authenticated sessions securely.
* Demonstrate database integration using MariaDB.

---


## 📂 Project Structure

```text
SecureLoginSystem/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── static/
│   └── style.css
│
├── screenshots/
│
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
```

---


## Features

### 1. User Registration

* Create a new account using:

  * Username
  * Email Address
  * Password

### 2. User Authentication

* Secure login system
* Password verification using bcrypt
* Session-based authentication

### 3. Password Security

* Passwords are never stored in plain text
* bcrypt hashing implemented
* Strong password validation

### 4. Account Validation

* Duplicate username prevention
* Duplicate email prevention
* Input validation

### 5. Session Management

* Secure session creation
* Session-based user authentication
* Logout functionality

### 6. Flash Messages

* Login success notifications
* Registration success notifications
* Error handling messages
* Invalid credential alerts

### 7. Security Features

* Password Hashing (bcrypt)
* SQL Injection Protection
* Session Management
* Authentication & Authorization
* Secure Database Storage
* Input Validation

### 8. Database Integration

* MariaDB Database
* SQLAlchemy ORM
* Automated table creation


---

## Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Database

* MariaDB

### ORM

* SQLAlchemy

### Security

* bcrypt

---


## ⚙️ Installation Guide

### Clone Repository

```bash
git clone https://github.com/your-username/SecureLoginSystem.git

cd SecureLoginSystem
```

### Create Virtual Environment

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install flask flask_sqlalchemy pymysql bcrypt
```

---

## 🗄️ MariaDB Setup

### Start MariaDB

```bash
sudo systemctl start mariadb
```

### Login

```bash
sudo mariadb
```

### Create Database

```sql
CREATE DATABASE secure_login;
```

### Create User

```sql
CREATE USER 'flaskuser'@'localhost'
IDENTIFIED BY 'your_password';

GRANT ALL PRIVILEGES
ON secure_login.*
TO 'flaskuser'@'localhost';

FLUSH PRIVILEGES;
```

---

## Running the Application

```bash
python3 app.py
```

Output:

```text
* Running on http://127.0.0.1:5000
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🔑 Authentication Workflow

### Registration Process

```text
User Registration
       │
       ▼
Input Validation
       │
       ▼
Duplicate Check
       │
       ▼
Password Hashing
       │
       ▼
Store in MariaDB
```

### Login Process

```text
User Login
      │
      ▼
Retrieve User
      │
      ▼
Verify Password
      │
      ▼
Create Session
      │
      ▼
Dashboard Access
```

### Logout Process

```text
Logout
   │
   ▼
Destroy Session
   │
   ▼
Redirect To Login
```

---

## Security Implementation

### Password Hashing

Passwords are hashed using bcrypt before being stored in the database.

Example:

```python
hashed_password = bcrypt.hashpw(
    password.encode('utf-8'),
    bcrypt.gensalt()
)
```

### SQL Injection Protection

The project uses SQLAlchemy ORM, which automatically utilizes parameterized queries.

Example:

```python
User.query.filter_by(
    username=username
).first()
```

### Session Security

Authenticated users are tracked using Flask sessions.

Example:

```python
session['user'] = user.username
```

---


## 📊 Database Schema

### User Table

| Field      | Type     |
| ---------- | -------- |
| id         | Integer  |
| username   | String   |
| email      | String   |
| password   | String   |
| created_at | DateTime |

### Example Data

| id |     username     |                              email                             |
| -- | ---------------- | -------------------------------------------------------------- |
| 1  |   manjeetkumar   | [manjeetkumar123@gmail.com](mailto:manjeetkumar123@gmail.com)  |


---

## Future Enhancements

Potential improvements:

### Two-Factor Authentication (2FA)

* Google Authenticator
* Time-based OTP
* QR Code Integration

### Forgot Password

* Email Verification
* Password Reset Links

### Email Verification

* Verify accounts before activation

### Login Attempt Limiting

* Brute-force attack prevention
* Account lockout mechanism

### Role-Based Access Control

* Admin Dashboard
* User Dashboard


---

### Feedback

Contributions, suggestions, and feedback are always welcome. Feel free to open an issue or submit a pull request.

---

## About the Developer

**Manjeet Kumar** <br>
Cyber Security Engineering Student

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
