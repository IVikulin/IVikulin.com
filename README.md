# IVikulin.com
This is a light and simple protfolio website, that based on Python/Django in back-end.
- It is responsive and optimized, so [Google PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/?url=ivikulin.com) gives **99/100** for both mobile and desktop versions. 
- The site uses a ssl certificate and supports HTTP/2. [SSL Server Test](https://www.ssllabs.com/ssltest/analyze.html?d=ivikulin.com) gives **A+** score for this site.

## Sorl thumbnail image optimization
For passing Google PageSpeed Insights, I extend [pil engine](https://github.com/IVikulin/IVikulin.com/blob/master/djsettings/pil_engine.py) by additional optimization through jpegoptim, gifsicle, optipng, etc.

## Used packages
### Local pip packages
- django 1.10
- django-admin-sortable2
- django-ckeditor
- gunicorn
- pillow
- psycopg2
- redis
- sorl-thumbnail

### Local npm packages
- bootstrap 4 
- jquery 3
- fullpage.js
- gulp
- gulp-autoprefixer
- gulp-browserify
- gulp-clean-css
- gulp-concat
- gulp-imagemin
- gulp-sass
- gulp-svg-sprite
- gulp-uglify


## Full project tree
```
├── configs
│   ├── ssl
│   │   ├── dhparam.pem
│   │   ├── ivikulin_com_bundle.crt
│   │   ├── ivikulin.csr
│   │   ├── ivikulin.key
│   │   └── ivikulin.pass
│   ├── nginx.conf
│   └── supervisor.conf
├── djapps
│   ├── general
│   │   ├── migrations
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   └── portfolio
│       ├── migrations
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       └── tests.py
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
├── public
│   ├── media
│   └── static
├── styles
│   └── main.scss
├── templates
│   ├── base.html
│   └── robots.txt
├── virtualenv -> /home/hosting/virtualenvs/django/
├── gulpfile.js
├── manage.py
├── package.json
├── README.md
└── requirements.txt
```
