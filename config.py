import secrets
from pathlib import Path

base_dir = Path.cwd()

class Config(object):
    TEMPLATES_AUTO_RELOAD = True
    SECRET_KEY = secrets.token_hex()

    DB = Path(base_dir.parent, "db.db")