
class News:
    """
    News class to define the news source object
    """

    def __init__(self, source_id, name, description, url, category, language, country):
        self.source_id = source_id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country