from app import app
import urllib.request,json
from .models import news

News = news.News
Articles = news.Articles

api_key = app.config['NEWS_API_KEY']
# api_key = '707d93f2c8d541bfb51985f1570fce4c'
base_url = app.config['NEWS_API_BASE_URL']

def get_news(news):
    """
    Function to retrieve news sources list from the News api
    """

    get_news_url = base_url.format(news, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['news']:
            news_results_list = get_news_response['news']
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list):
    """
    Function that process the news results list and transforms them into a list of objects
    Args: sources_list: A list of dictionaries that contains news details
    Returns:
    news_results: a list of news sources objects
    """

    news_results = []
    for news_item in news_list:
        source_id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        news_object = News(source_id, name, description, url, category, language, country)
        news_results.append(news_object)

    return news_results


def get_articles(news):
    """
    Function to retrieve news sources list from the News api
    """

 
    get_articles_url = base_url.format(news, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)
    return articles_results


def process_articles_results(articles_list):
    """Function that process the results list and transforms them into a list of objects
    Args: articles_list: A list of dictionaries that contains news articles and links
    Returns:
    articles_results: a list of news articles objects"""

    articles_results = []
    for article_item in articles_list:
        source_id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        urlToImage = article_item.get('urlToImage')
        url = article_item.get('url')
        date = article_item.get('publishedAt')

        article_object = Articles(source_id, author, title, description, urlToImage, url, date)
        articles_results.append(article_object)
    return articles_results