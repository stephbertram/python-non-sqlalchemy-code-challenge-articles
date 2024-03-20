class Article:
    
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)
        
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        elif not 5 <= len(title) <= 50:
            raise ValueError("Title must be within 5 <= title <= 50.")
        elif hasattr(self, "title"):
            raise AttributeError("Title cannot be reset.")
        else:
            self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class.")
        else:
            self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine class.")
        else:
            self._magazine = magazine
    
    def __repr__(self):
        return f"Article(author={self.author.name}, magazine={self.magazine.name}, title={self.title})"


class Author:
    
    all = []
    
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        elif not len(name) > 0:
            raise ValueError("Name must be longer than 0 characters.")
        elif hasattr(self, "name"):
            raise AttributeError("Name cannot be reset.")
        else:
            self._name = name
    
    # Returns a list of all the articles the author has written
    def articles(self):
        return [article for article in Article.all if article.author == self]

    # Returns a unique list of magazines for which the author has contributed to
    def magazines(self):
        return list({article.magazine for article in self.articles()})

    # Creates and returns a new Article instance and associates it with that author, the magazine provided
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    # Returns a unique list of strings with the categories of the magazines the author has contributed to
    def topic_areas(self):
        # if self.magazines():
        return list({magazine.category for magazine in self.magazines()}) or None
        # else:
        #     return None

    def __repr__(self):
        return f"Author(name={self.name})"



class Magazine:
    
    all = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        elif not 2 <= len(name) <= 16:
            raise ValueError("Name must be within 2 <= name <= 16.")
        else:
            self._name = name
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise TypeError("Category must be a string.")
        elif not len(category) > 0:
            raise ValueError("Category must be longer than 0 characters.")
        else:
            self._category = category

    # Returns a list of all the articles the magazine has published
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # Returns a unique list of authors who have written for this magazine
    def contributors(self):
        return list({article.author for article in self.articles()})

    # Returns a list of the titles strings of all articles written for that magazine
    def article_titles(self):
        # if articles:=self.articles():
        return [article.title for article in self.articles()] or None
        # else:
        #   return None

    # Returns a list of authors who have written more than 2 articles for the magazine
    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
                if article.author in author_count:
                    author_count[article.author] += 1
                else:
                    author_count[article.author] = 1
            
        # Filter authors who have written more than 2 articles
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        
        return contributing_authors or None
        
    def __repr__(self):
        return f"Magazine(name={self.name}, category={self.category})"

    @classmethod
    def top_publisher(cls):
        if Article.all:
            return max(cls.all, key=lambda magazine: len(magazine.articles()), default=None)




# # TESTING
    
# author_1 = Author("Carry Bradshaw")
# author_2 = Author("Stephanie Bertram")
# magazine_1 = Magazine("Vogue", "Fashion")
# magazine_2 = Magazine("AD", "Architecture")
# magazine_3 = Magazine("GQ", "Fashion")
# magazine_4 = Magazine("Sunset", "Lifestyle")
# Article(author_1, magazine_1, "How to wear a tutu with style") # Carrie Bradshaw, Vogue
# Article(author_1, magazine_1, "Style article 2") # Carrie Bradshaw, Vogue
# Article(author_1, magazine_1, "Style article 3") # Carrie Bradshaw, Vogue
# Article(author_1, magazine_3, "How to wear a tutu with style") # Carrie Bradshaw, GQ
# Article(author_2, magazine_2, "2023 Eccentric Design Trends") #Nathaniel Hawthorne, AD

# print("Articles:", author_1.articles())
# print("Magazines:", author_1.magazines())
# print("Topic Areas:", author_1.topic_areas())
# print("Contributors:", magazine_2.contributors())
# print("Article Titles:", magazine_2.article_titles())
# print("Article Titles:", magazine_4.article_titles())
# print("Contributing Authors:", magazine_1.contributing_authors())