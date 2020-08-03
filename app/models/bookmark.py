import json

class BookMark(object):
    def __init__(self,):
        self.file = 'app/static/doc/bookmark.json'

    def insert(self, doc: dict):
        record = self.get_record()
        record.update(doc)
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(record, f)
    
    def get_record(self,):
        with open(self.file, 'r', encoding='utf-8') as f:
            doc = json.load(f)
        return doc
    
    def delete(self, target):
        record = self.get_record()
        record.pop(target, None)

        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(record, f)