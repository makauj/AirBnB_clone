"""initialize folder"""

from models.engine.file_storage import FileStorage # type: ignore

storage = FileStorage()
storage.reload()
