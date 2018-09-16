from typing import List
from pathlib import Path
from enum import Enum

class Change:
    MODIFY = 'change'
    RENAME = 'rename'

class Dirty: pass

class FileChange:
    path: Path
    change: Change