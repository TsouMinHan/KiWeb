from app.models import NewsDB, GalleryDB
from datetime import date

if __name__ == '__main__':
    a = GalleryDB()   
    z = a.delete_img()
    print(z)
