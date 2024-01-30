#!/usr/bin/env python3
"""4-app.py"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Babel Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Return user preferred locale"""
    url_locale = request.args.get('locale')
    if url_locale and url_locale in app.config['LANGUAGES']:
        return url_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """GET method for index.html"""
    from flask_babel import gettext as _
    return render_template('/3-index.html')


if __name__ == "__main__":
    app.run()
