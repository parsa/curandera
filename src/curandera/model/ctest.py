from typing import List, Optional, Text, Dict
from pathlib import Path

class Test:
    name: Text
    command: Text
    properties: Dict[Text, Text]

class Project:
    name: Text
    tests: List[Test]

class Configuration:
    name: Optional[Text]
    project: List[Project]

class Info:
    configs: List[Configuration]