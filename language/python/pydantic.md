### immutable field & class 
```python
## immutable field
from pydantic import BaseModel, Field

class User(BaseModel):
    user_id: int = Field(..., allow_mutation=False)
    name: str

    class Config:
        validate_assignment = True


user = User(user_id=1, name='John')
user.user_id = 2  
# TypeError: "user_id" has allow_mutation set to False and cannot be assigned

# immutable class
class User(BaseModel):
    user_id: int
    name: str
    class Config:
        frozen = True
```

- domain entity dao는 immutable하게 만드는게 좋을것 같음
