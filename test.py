from app.models import NewsDB, GalleryDB, MainDB
from datetime import date

if __name__ == '__main__':
    a = MainDB()   
    z = a.get_record("News")
    print(len(z))
