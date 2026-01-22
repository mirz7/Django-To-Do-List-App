# Django-To-Do-List-App
# Django To-Do List App 📝

A full-featured, responsive To-Do List web application built with Django, designed to help users organize and manage their daily tasks efficiently.

## 🎥 Demo Video

>https://github.com/user-attachments/assets/275190d6-0169-4fcd-aa54-16836744cc4f

## ✨ Features

- **User Authentication**
  - User registration and login system
  - Secure password management
  - Session-based authentication

- **Task Management**
  - Create, read, update, and delete tasks (CRUD operations)
  - Mark tasks as complete/incomplete
  - Task priority levels
  - Due date tracking
  - Task categories/tags

- **User Interface**
  - Clean and intuitive design
  - Responsive layout for mobile and desktop
  - Real-time task updates
  - Search and filter functionality

- **Data Persistence**
  - SQLite database (default)
  - Easy migration to PostgreSQL/MySQL for production

## 🛠️ Technologies Used

- **Backend**: Django 4.x
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (development) / PostgreSQL (production-ready)
- **Authentication**: Django's built-in authentication system
- **Styling**: Custom CSS with responsive design

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)
- Git

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mirz7/Django-To-Do-List-App.git
cd Django-To-Do-List-App
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install Django manually:

```bash
pip install django
```

### 4. Database Setup

```bash
# Navigate to the project directory containing manage.py
cd todolist

# Run migrations
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 6. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📁 Project Structure

```
Django-To-Do-List-App/
│
├── todolist/                 # Main project directory
│   ├── manage.py            # Django management script
│   ├── todolist/            # Project configuration
│   │   ├── settings.py      # Project settings
│   │   ├── urls.py          # URL routing
│   │   └── wsgi.py          # WSGI configuration
│   │
│   ├── tasks/               # Tasks app (assumed)
│   │   ├── models.py        # Database models
│   │   ├── views.py         # View functions
│   │   ├── urls.py          # App URLs
│   │   ├── forms.py         # Forms
│   │   └── templates/       # HTML templates
│   │
│   ├── static/              # Static files (CSS, JS, images)
│   └── media/               # User uploaded files
│
└── README.md                # Project documentation
```

## 💻 Usage

### User Registration & Login

1. Navigate to the registration page
2. Create a new account with username and password
3. Log in with your credentials

### Managing Tasks

1. **Add Task**: Click on "Add Task" button and fill in the details
2. **Edit Task**: Click the edit icon next to any task
3. **Delete Task**: Click the delete icon to remove a task
4. **Mark Complete**: Check the checkbox to mark tasks as done
5. **Filter Tasks**: Use the filter options to view specific tasks

### Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/` with your superuser credentials to:
- Manage users
- View all tasks
- Perform administrative actions

## 🎨 Customization

### Changing the Theme

Modify the CSS files in the `static/css/` directory to customize colors, fonts, and layout.

### Adding New Features

1. Create new models in `models.py`
2. Add corresponding views in `views.py`
3. Create templates in the `templates/` directory
4. Update URL patterns in `urls.py`

## 🗄️ Database Configuration

### For Production (PostgreSQL)

Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🚢 Deployment

### Preparing for Production

1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS`
3. Set up static files serving
4. Use environment variables for sensitive data

### Deployment Platforms

- **Heroku**: Follow [Django Heroku deployment guide](https://devcenter.heroku.com/articles/django-app-configuration)
- **PythonAnywhere**: Follow [PythonAnywhere Django tutorial](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)
- **AWS/DigitalOcean**: Use Gunicorn + Nginx setup

## 🧪 Testing

Run tests using Django's testing framework:

```bash
python manage.py test
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**mirz7**

- GitHub: [@mirz7](https://github.com/mirz7)
- Repository: [Django-To-Do-List-App](https://github.com/mirz7/Django-To-Do-List-App)

## 🙏 Acknowledgments

- Django Documentation
- Django Community
- Open Source Contributors

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/mirz7/Django-To-Do-List-App/issues) page
2. Create a new issue with detailed description
3. Contact the repository owner

## 🔮 Future Enhancements

- [ ] Task collaboration and sharing
- [ ] Email notifications for due tasks
- [ ] Mobile app version
- [ ] Task statistics and analytics
- [ ] Dark mode toggle
- [ ] Export tasks to PDF/CSV
- [ ] Integration with calendar apps
- [ ] Recurring tasks functionality

---


**Made with ❤️ using Django**

