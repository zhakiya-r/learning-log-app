# Learning Log

Learning Log is a web application built with Django that allows users to create topics and keep notes about what they are learning. Each user can register, log in, and manage their own learning records.

## Features

* User registration and authentication
* Login and logout functionality
* Create, edit, and manage topics
* Add and edit entries for each topic
* User-specific data access
* Responsive design using Bootstrap 5

## Technologies Used

* Python
* Django
* Bootstrap 5
* SQLite (development)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/zhakiya-r/learning-log-app.git
cd learning-log-app
```

2. Create and activate a virtual environment:

```bash
python -m venv ll_env
source ll_env/bin/activate   # Linux/macOS
ll_env\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Open your browser and visit:

```
http://127.0.0.1:8000/
```

## Project Structure

* `learning_log/` – project configuration
* `learning_logs/` – main application
* `accounts/` – account authentication and registration
* `manage.py` – Django management script

## Future Improvements

* User profile pages
* Search functionality
* File uploads
* Dark mode support

## License

This project was created for educational purposes.
