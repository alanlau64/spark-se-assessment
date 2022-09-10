web: gunicorn project.server:app
heroku ps:scale web=1
heroku config:set FLASK_APP=project.server
heroku config:set APP_SETTINGS="project.server.config.ProductionConfig"
release: echo $FLASK_APP
release: flask db init
release: flask db migrate
release: flask db upgrade


