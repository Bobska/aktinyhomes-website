# A&K Tiny Homes Website

A Django web application replicating the Aktiny Homes website (aktinyhomes.co.nz) - a New Zealand-based tiny homes business specializing in custom-built affordable tiny homes.

## Features

- **Responsive Design**: Mobile-friendly website that works on all devices
- **Image Gallery**: Showcase of tiny home designs and construction photos
- **Layout Options**: Information about different tiny home sizes and designs
- **Blog System**: Content management for news and updates
- **FAQ Section**: Frequently asked questions about tiny homes
- **Contact Integration**: Direct email contact functionality
- **Admin Panel**: Django admin interface for content management

## Project Structure

```
aktinyhomes/
├── aktinyhomes/         # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/                # Main Django app
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   ├── urls.py          # URL patterns
│   ├── admin.py         # Admin configuration
│   └── templates/       # HTML templates
├── static/              # Static files (CSS, JS, images)
│   ├── css/
│   └── js/
└── manage.py           # Django management script
```

## Models

- **TinyHomeLayout**: Different tiny home designs and sizes
- **TinyHomeImage**: Image gallery with featured images
- **BlogPost**: Blog articles and news
- **FAQ**: Frequently asked questions

## Installation

1. Ensure Python 3.10+ is installed
2. Install dependencies:
   ```bash
   pip install django pillow requests
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Visit `http://localhost:8000` to view the website
- Access the admin panel at `http://localhost:8000/admin` (requires superuser account)
- Add content through the admin panel or directly in the templates

## Pages

- **Home**: Main landing page with hero section and image gallery
- **Layouts**: Information about different tiny home designs
- **Blog**: News and articles about tiny homes
- **FAQs**: Frequently asked questions
- **Red Tape**: Regulatory information
- **Privacy Policy**: Privacy and data protection information
- **Terms & Conditions**: Terms of service

## Customization

The website is built with Django best practices and can be easily customized:

- Modify templates in `main/templates/main/`
- Update styles in `static/css/style.css`
- Add functionality in `main/views.py`
- Extend models in `main/models.py`

## Contact

For questions about A&K Tiny Homes, contact: akmotorhomes@outlook.com

## License

This project is for educational purposes, replicating the Aktiny Homes website design and content.
