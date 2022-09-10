web: gunicorn project.server:app
heroku ps:scale web=1
release: flask db init
release: flask db migrate
release: flask db upgrade


