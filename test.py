from app.models import NewsDB, GalleryDB, MainDB, LogDB
from datetime import date

if __name__ == '__main__':
    a = LogDB()   
    z = a.get_log()
    print(z)
