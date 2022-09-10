web: gunicorn project.server:app
heroku ps:scale web=1
release: export FLASK_APP=project.server
release: export APP_SETTINGS="project.server.config.ProductionConfig"
release: flask db init
release: flask db migrate
release: flask db upgrade


