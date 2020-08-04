from flask_login import UserMixin
from pathlib import Path
import sqlite3

from app.baha_img import BahaImg
from config import Config
from app import login

@login.user_loader
def load_user(id):
    return User()

class User(UserMixin):
    def __init__(self):
        self.username = "kimo"
        self.password = "321qasdew"
        self.id = 1
    
    def check_password(self, pwd):
        if pwd == self.password:
            return True
        return False

class NewsContent:
    def __init__(self, id, title, link):
        self.id = id
        self.title = title
        self.link = link

class DBHandler:
    def __init__(self):
        self.db_name = f"{Config.DB}"

    def __enter__(self):
        self.start_database()
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        self.close_database()
    
    def start_database(self,):
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()

    def close_database(self,):
        """shut down connect to DB
        """
        self.conn.close()

class NewsDB:  
    def __init__(self):
        self.db = DBHandler()
        self.table_name = "News"

    def get_record(self, date):
        with self.db:
            sql = f"SELECT DISTINCT website FROM {self.table_name}"
            self.db.cur.execute(sql)
            
            rows = self.db.cur.fetchall()
            website_ls = [ row[0] for row in rows]
            dc = {}

            for website in website_ls:
                sql = f"""
                    SELECT id, title, link FROM {self.table_name}
                    WHERE date='{date}' and website='{website}';
                """

                self.db.cur.execute(sql)            
                rows = self.db.cur.fetchall()

                dc[website] = [NewsContent(row[0], row[1], row[2]) for row in rows]
        return dc

    def update_seen(self, id):
        with self.db:
            sql = f"""UPDATE {self.table_name}
                SET seen=1
                WHERE id={id}
            """
            self.db.cur.execute(sql)
            self.db.conn.commit()

class GalleryDB:  
    def __init__(self):
        self.db = DBHandler()
        self.table_name = "img"
        self.number_of_img = 20

    def get_img_ls(self):
        with self.db:
            sql = f"""
                SELECT img_url
                FROM {self.table_name}
                LIMIT {self.number_of_img};
            """

            self.db.cur.execute(sql)

            rows = self.db.cur.fetchall()
            
        ls = [row[0] for row in rows]

        return ls

    def delete_img(self, img_ls):
        with self.db:
            for img in img_ls:
                sql = f"""
                    DELETE FROM {self.table_name}
                    WHERE img_url='{img}'
                """

                self.db.cur.execute(sql)
            self.db.conn.commit()

class BahaImgListDB:  
    def __init__(self):
        self.db = DBHandler()
        self.table_name = "baha_img_list"

    def add(self, url):
        with self.db:
            a = BahaImg(url)
            a.run()
            title = a.title.replace("'", "\"")
            
            sql = f"""
                INSERT INTO {self.table_name} (title, url) VALUES 
                ('{title}', '{url}');
            """

            self.db.cur.execute(sql)
            self.db.conn.commit()

    def get_record(self):
        """
        :return ls: list of Content.
        """
        with self.db:
            sql = f"""
                SELECT url FROM {self.table_name}
            """

            self.db.cur.execute(sql)

            rows = self.db.cur.fetchall()
            
        ls = [row[0] for row in rows]

        return ls

if __name__ == "__main__":
    m = Main_DB()
    m.create_table()