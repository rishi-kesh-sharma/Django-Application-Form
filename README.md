## Backend Setup (Django)

# Clone the repository

```bash
git clone <repo-url>
cd <repo-folder>
```

# Create and activate a virtual environment

```bash
python -m venv .venv

# On Windows
source .venv\Scripts\activate

# On Linux/macOS
source .venv/bin/activate
```

# Install dependencies

```bash
pip install -r requirements.txt
```

# Go to Project folder

```bash
cd application_form
```

# Make database migrations

```bash
python manage.py makemigrations
```

# Apply database migrations

```bash
python manage.py migrate
```

# Create superuser

```bash
python manage.py createsuperuser
```

# Start the development server

```bash
python manage.py runserver
```
