# Attendance Management System

A complete production-ready Django 5 application for managing student attendance with Bootstrap 5, Chart.js, and PythonAnywhere deployment support.

## Features

- **Authentication & Authorization**: Custom user model with role-based access (Admin, Teacher, Student)
- **Academic Management**: Department, Classroom, and Subject management
- **Attendance Tracking**: Bulk attendance marking with individual modifications
- **Reporting**: Student, Subject, and Classroom attendance reports
- **Analytics**: Attendance percentage calculations and visualizations
- **Warnings**: Automatic alerts for low attendance and consecutive absences
- **Responsive UI**: Bootstrap 5 design with Charts.js visualizations

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/attendance_system.git
cd attendance_system
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
cp .env.example .env
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 8. Run Development Server
```bash
python manage.py runserver
```

Access the application at `http://localhost:8000`

## Project Structure

```
attendance_system/
├── accounts/              # User authentication & management
├── academics/             # Department, Classroom, Subject
├── students/              # Student & Teacher profiles
├── attendance/            # Attendance tracking
├── reports/               # Report generation & export
├── dashboard/             # Dashboard views
├── templates/             # HTML templates
├── static/                # CSS, JS, Images
├── manage.py              # Django management
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

## Technologies Used

- **Backend**: Django 5.0
- **Frontend**: Bootstrap 5, Chart.js
- **Database**: SQLite (can be upgraded to PostgreSQL)
- **Deployment**: PythonAnywhere
- **Export**: ReportLab (PDF), OpenPyXL (Excel)

## License

MIT License

## Support

For issues and questions, please create an issue on GitHub.