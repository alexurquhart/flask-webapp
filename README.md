# flask-webapp
Starter template for a flask web app. Includes:

- [Flask-Security](https://pythonhosted.org/Flask-Security/)
- [Flask-Social](http://pythonhosted.org/Flask-Social/)
- [Flask-Migrate](http://flask-migrate.readthedocs.io/en/latest/)
- [Flask-DebugToolbar](http://flask-debugtoolbar.readthedocs.io/en/latest/)
- [Celery](http://docs.celeryproject.org/en/latest/index.html)

## Dependencies
- Redis
- PostgreSQL

## To install

```bash
> git clone https://github.com/alexurquhart/flask-webapp.git
> cd flask-webapp
> virtualenv env
> source environ
> pip install
> python manage.py db init
> python manage.py db migrate
> python manage.py db upgrade
```
Be sure to replace session secret, password salt, and database URI strings in `environ`

In a separate terminal, run the dummy `smtpd` instance so real e-mails don't get sent out for user registration, password reset, etc:
```bash
> python manage.py runmail
```

To run the development server:
```bash
> python manage.py runserver
```
