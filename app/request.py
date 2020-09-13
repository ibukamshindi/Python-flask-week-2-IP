from app import app
import urllib.request,json
from .models import news

News = news.News
Articles = news.Articles

api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']