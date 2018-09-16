from typing import List, Text, Tuple, Any
from pathlib import Path
import shlex

# TODO: This is a code model

from .language import Language

class Define:
    key: Text
    value: Any

class Include:
    path: Path
    sys: bool

class FileGroup:
    language: Language
    defines: List[Define]
    includes: List[Include]
    sources: List[Path]
    flags: List[Text]