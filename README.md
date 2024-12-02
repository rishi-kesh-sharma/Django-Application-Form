## Backend Setup (Django)

```bash

# Clone the repository
git clone <repo-url>
cd <repo-folder>

# Create and activate a virtual environment
python -m venv .venv

# On Windows
source .venv\Scripts\activate

# On Linux/macOS
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Go to Project folder
cd application_form

# Make database migrations
python manage.py makemigrations

# Apply database migrations
python manage.py migrate

#Create superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver

```
