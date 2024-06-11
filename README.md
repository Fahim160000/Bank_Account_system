# Bank_Account_System

Bank_Account_System is a web application built with Django that allows users to manage their bank accounts. Users can create accounts, view account details, update information, delete accounts, and perform transactions like deposits and withdrawals.

## Table of Contents

- [Features]
- [Installation]
- [Usage]
- [Project Structure]
- [Contributing]
- [License]

## Features

- User authentication (login, logout)
- Create, view, edit, and delete bank accounts
- Perform transactions (deposit, withdrawal)
- View transaction history
- Responsive and user-friendly interface

## Installation

### Prerequisites

- Python 3.x
- Django

### Steps

1. **Clone the repository:**

 ```bash
   git clone https://github.com/yourusername/Bank_Account_System.git
   cd Bank_Account_System
 ```

## Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:
```

``` bash
pip install -r requirements.txt
Apply migrations:
```

``` bash
python manage.py makemigrations
python manage.py migrate
Create a superuser:
```

``` bash
python manage.py createsuperuser
Run the development server:
```

``` bash
python manage.py runserver
```

## Visit the application:

Open your browser and go to http://127.0.0.1:8000/

# Usage
## User Authentication

- Navigate to /accounts/login/ to log in.
- Use the Django admin interface at /admin/ to manage accounts and transactions.

## Bank Account System

- After logging in, you can add a new account by clicking the "Add New Account" link.
- View an account's details by clicking on its name in the account list.
- Edit or delete an account from its detail view.

## Performing Transactions
- Add a new transaction (deposit or withdrawal) by clicking the "Add New Transaction" link.
- View a transaction's details by clicking on it in the transaction list.

## Project Structure

```bash
Bank_Account_System/
├── bank_account_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── accounts/
│           ├── account_list.html
│           ├── account_detail.html
│           ├── account_edit.html
│           └── account_create.html
├── transactions/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── transactions/
│           ├── transaction_list.html
│           ├── transaction_detail.html
│           └── transaction_create.html
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## Contributing
- Fork the repository.
- Create a new branch.
- Make your changes and commit them.
- Push your changes to your fork.
- Create a pull request.


