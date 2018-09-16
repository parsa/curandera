from typing import Text, List, Optional, TypeVar
from pathlib import Path

from .language import Language
from .group import FileGroup
from .type import Type

Version = TypeVar('Version')

class Target:
    name: Text
    type: Type
    target: Path # ANNOTATE: fullName (artifact output)
    generated: bool
    install: Optional[List[Path]] # ANNOTATE (combination of hasInstallRule/installPaths)
    artifacts: List[Path]
    # XXX: Possibly move linker info into another subclass
    # start-linker settings
    language: Language
    libraries: List[Path] # Needs to be shlex'd
    flags: List[Text] # Both linkFlags and linkLanguageFlags
    framework: Path # macOS only
    # end-linker settings
    sysroot: Path
    groups: List[FileGroup]

class Project:
    name: Text
    cmake: Version
    install: bool
    source: Path
    build: Path
    targets: List[Target]

class Configuration:
    name: Optional[Text]
    projects: List[Project]