import logging
from functools import wraps

logger =logging.getLogger(__name__)

class DBdriver:
    def __init__(self, dbstring):
        self.dbstring = dbstring
    
    def execute(self ,query):
        return f"{query} executed"

def inject_db_driver(function):
    @wraps(function)
    def wrapped(dbstring):
        return function(DBdriver(dbstring))

@inject_db_driver
def run_query(driver):
    return driver.execute("")