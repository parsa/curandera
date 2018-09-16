from typing import List, Text, Dict

class CacheType: pass

class CacheEntry:
    key: Text
    value: Text
    properties: Dict[Text, Text]
    type: CacheType

class Cache:
    entries: List[CacheEntry]