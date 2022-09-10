web: gunicorn project.server:app
heroku ps:scale web=1
heroku run flask db upgrade
