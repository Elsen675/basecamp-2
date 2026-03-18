# Welcome to My Basecamp 2
***

## Task
Building a project management web application with attachments, threads, and messages functionality, hosted in the cloud.

## Description
MyBasecamp 2 is a follow-up to MyBasecamp 1. It is built with Django and extends the original project with new features. Users can create projects, add attachments in various formats (png, jpg, pdf, txt), create discussion threads (admin only), and post messages within threads. The application is hosted on Railway with a PostgreSQL database.

## Installation
1. Make sure you have Python 3.10+ installed on your machine.
2. Clone the repository:
```bash
git clone https://github.com/Elsen675/basecamp-2.git
```
3. Navigate to the project directory:
```bash
cd basecamp-2
```
4. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```
5. Install dependencies:
```bash
pip install -r requirements.txt
```
6. Run migrations:
```bash
python manage.py migrate
```
7. Start the development server:
```bash
python manage.py runserver
```

## Usage
```
https://web-production-953dc.up.railway.app
```
Register an account, create a project, add attachments, create threads and post messages.

## Features
- User registration and authentication
- Project creation and management
- File attachments (png, jpg, pdf, txt)
- Discussion threads (admin only)
- Messages within threads
- Cloud hosted on Railway with PostgreSQL

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>