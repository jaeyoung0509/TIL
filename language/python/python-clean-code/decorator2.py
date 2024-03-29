class DictQuery:
    def __init__(self,**kwargs):
        self._raw_query = kwargs
    
    def render(self) -> dict:
        return self._raw_query

class QueryEnhancer:
    def __init__(self, query:DictQuery) -> None:
        self.decorated = query

    def render(self):
        return self.decorated.render()

class RemoveEmpty(QueryEnhancer):
    def render(self):
        original =  super().render()
        return {k:v for k, v in original.items() if v}

class CaseIntensive(QueryEnhancer):
    def render(self):
        original = super().render()
        return {k:v for k, v in original.items()}