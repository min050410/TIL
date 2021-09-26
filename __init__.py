from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')

    #ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models #수정 #from zelda.models 

  	#Blueprint
    from zelda.views import main_views, comment_views, auth_views #수정 from zelda.views im
    app.register_blueprint(main_views.bp)
    app.register_blueprint(comment_views.bp)
    app.register_blueprint(auth_views.bp)
    
    #filter
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app


