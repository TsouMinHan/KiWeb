from app.models import NewsDB
from datetime import date

if __name__ == '__main__':
    a = NewsDB()   
    a.update_seen(1)

