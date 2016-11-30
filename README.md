# IVikulin.com

This is a light and simple protfolio website. 
- It is responsive and optimized, so [Google PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/?url=ivikulin.com) gives **99/100** for both mobile and desktop versions. 
- The site uses a ssl certificate and supports HTTP/2. [SSL Server Test](https://www.ssllabs.com/ssltest/analyze.html?d=ivikulin.com) gives **A+** score.

###Live version
[IVikulin.com](https://IVikulin.com/)


## Used packages
### Pip
-django==1.10.3
-django-admin-sortable2==0.6.5
-django-ckeditor==5.1.1
-gunicorn==19.6.0
-pillow==3.4.2
-psycopg2==2.6.2
-redis==2.10.5
-sorl-thumbnail==12.3

### Npm

    "bootstrap": "^4.0.0-alpha.5",
    "fullpage.js": "^2.8.9",
    "iscroll": "^5.2.0",
    "jquery": "^3.1.1"

    "gulp": "^3.9.1",
    "gulp-autoprefixer": "^3.1.1",
    "gulp-browserify": "^0.5.1",
    "gulp-clean-css": "^2.0.12",
    "gulp-concat": "^2.6.0",
    "gulp-imagemin": "^3.1.1",
    "gulp-sass": "^2.3.2",
    "gulp-svg-sprite": "^1.3.6",
    "gulp-uglify": "^2.0.0"

    
## Project tree
```
├── configs
│	├── ssl
│	│   ├── dhparam.pem
│	│   ├── ivikulin_com_bundle.crt
│	│   ├── ivikulin.csr
│	│   ├── ivikulin.key
│	│   └── ivikulin.pass
│   ├── nginx.conf
│   └── supervisor.conf
├── djapps
│	├── general
│	│   ├── migrations
│	│   ├── __init__.py
│	│   ├── admin.py
│	│   ├── apps.py
│	│   ├── models.py
│	│   ├── tests.py
│	│   └── views.py
│	└── portfolio
│	    ├── migrations
│	    ├── __init__.py
│	    ├── admin.py
│	    ├── apps.py
│	    ├── models.py
│	    └── tests.py
├── djsettings
│   ├── __init__.py
│   ├── pil_engine.py
│   ├── private_settings.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── images
│   ├── card.jpg
│   ├── favicon.png
│   └── loader.svg
├── jsapps
│   └── main.js
├── logs
│   ├── django.log
│   ├── gunicorn.log
│   └── nginx.log
├── node_modules
├── public
│   ├── media
│   └── static
├── styles
│   └── main.scss
├── templates
│   ├── base.html
│   └── robots.txt
├── virtualenv -> /home/hosting/virtualenvs/django/
├── .gitignore
├── .pipconfig
├── gulpfile.js
├── manage.py
├── package.json
├── README.md
└── requirements.txt
```
