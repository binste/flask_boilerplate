from pathlib import Path
from typing import Union


class Config:
    def __init__(self, base_dir: Union[str, Path] = Path.cwd()):
        self.base_dir = base_dir if isinstance(base_dir, Path) else Path(base_dir)
        self.DEBUG = True
        self.TESTING = False
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(self.base_dir / "database.db")
        # Prevents caching of static files by browser. Useful for development
        self.SEND_FILE_MAX_AGE_DEFAULT = 0
