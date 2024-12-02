## Backend Setup (Django)

## Clone the repository

```bash
git clone <repo-url>
```

## Go to Repo Folder

```bash
cd <repo-folder>
```

## Create virtual environment

```bash
python -m venv .venv
```

## Activate virtual environment

### On Windows

```bash
source .venv/Scripts/activate
```

### On Linux/macOS

```bash
source .venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Go to Project folder

```bash
cd application_form
```

## Make database migrations

```bash
python manage.py makemigrations
```

## Apply database migrations

```bash
python manage.py migrate
```

## Create superuser

```bash
python manage.py createsuperuser
```

## Start the development server

```bash
python manage.py runserver
```

## Visit

[Application Form](http://127.0.0.1:8000/form/)
