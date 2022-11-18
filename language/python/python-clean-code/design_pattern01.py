class GitFetcher:
    _current_tag = None

    def __init__(self,tag):
        self._current_tag = tag

    @property
    def current_tag(self):
        if self._current_name is None:
            raise AttributeError("tag is not initialized")
        return self._current_tag   

    
    @current_tag.setter
    def current_tag(self,new_tag):
        self.__class__.current_tag = new_tag

    def pull(self):
        return self.current_tag

        