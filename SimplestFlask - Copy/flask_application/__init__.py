"""Initialize app."""
from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__,
                instance_relative_config=False)
    #app.config.from_object('config.Config')

    with app.app_context():

        # Import main Blueprint
        #from . import routes
        #app.register_blueprint(routes.main_bp)

        # Import Dash application
        from .dash_application import dash_app1
        app1 = dash_app1.Add_Dash(app)

        from .dash_application import dash_app2
        app2 = dash_app2.Add_Dash(app)

        from .dash_application import dash_app3
        app3 = dash_app3.Add_Dash(app)

        from .dash_application import dash_app4
        app4 = dash_app4.Add_Dash(app)

        return app
