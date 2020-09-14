from flask import render_template
from app import app
from .request import get_news, get_articles

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    new_News = get_news('news')
    title = 'Home - Welcome to the best News app'
    return render_template('index.html', title = title, news = new_News)

