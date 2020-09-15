from flask import render_template,request,redirect,url_for
from .import main
from ..request import get_news, get_articles

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    new_News = get_news('news')
    title = 'Home - Welcome to the best News app'
    return render_template('index.html', title = title, new_News = new_News)

@main.route('/articles/<source_id>')
def source(source_id):
    """
    View for top story articles
    """
    
    source_and_articles = get_articles(source_id)
    return render_template('articles.html', source_and_articles=source_and_articles)


