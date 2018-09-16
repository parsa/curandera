from typing import List
from pathlib import Path

class Inputs:
    temporary: List[Path] # Will not survive a "make clean"
    files: List[Path]
    cmake: List[Path] # cmake installation files
    source: Path # Root CMakeLists.txt directory
    root: Path # CMake Root directory