# Free Courses Directory

A Django website that lists free online courses. Each course has a card with a title, description, image and a link to the course.

## Features

- Home page and a free-courses page with course cards
- Course detail page
- About page
- Add a course from a form with an image upload
- Small JSON endpoint to add courses from a script, so the list can be filled automatically
- Custom 404 and 500 pages
- Ready to deploy on Vercel (`vercel.json`)

## Pages and endpoints

| Path | What it does |
| --- | --- |
| `/` | Home page |
| `/free-courses/` | All courses |
| `/course/<id>/` | One course |
| `/aboutus/` | About page |
| `/create-course/` | Form to add a course |
| `/CourseView/api/` | POST JSON `{"title": "...", "link": "..."}` to add a course |

## Built with

- Python 3, Django 4.2
- Pillow for course images
- SQLite
- Vercel (`@vercel/python`)

## Run it locally

```bash
git clone https://github.com/hamzakhalem/courses_website.git
cd courses_website
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install django pillow
export DJANGO_SECRET_KEY="any-long-random-string"   # PowerShell: $env:DJANGO_SECRET_KEY="..."
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000. `DEBUG` is off in `freecourses/settings.py` for deployment; set it to `True` while developing so Django serves the static files.

## Project structure

```
freecourses/   Project settings, root URLs and WSGI entry for Vercel
newfreeapp/    Course model, form, views and templates
```
