#Python
import json
from datetime import date, datetime
from uuid import UUID
from typing import Optional, List
#Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field
#FastAPI
from fastapi import FastAPI,status,Body


app = FastAPI()

#Models
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
class UserLogin(UserBase):
    password: str = Field(
    ..., 
    min_length=8,
    max_length=64
    )
class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_day: Optional[date]= Field(default=None)
class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        max_length=256,
        min_length=1
        )
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)
class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )
# Paths Operations

## Users

### Signup a new user
@app.post(
    path="/signup",
    response_model=User,
    status_code = status.HTTP_201_CREATED,
    summary="Signup a new user",  
    tags=["Users"]
    )
def signup(user: UserRegister = Body(...)):
    """
    Signup a new user

    This path operation register a user in the app

    Parameters:
        - Resquest bodu parameter
            - user: UserRegister
    Returns a json with the basic information:
        -   user_id: UUID
        -   email: EmailStr
        -   first_name: str
        -   last_name: str
        -   birth_day: datetime
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_day"] = str (user_dict["birth_day"])   
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user

### Login a User
@app.post(
    path="/login",
    response_model=User,
    status_code = status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
    )
def login():
    pass

### Show all users
@app.get(
    path="/users",
    response_model=List[User],
    status_code = status.HTTP_200_OK,
    summary="Show all users",   
    tags=["Users"]
    )
def show_all_users():
    """
    This path Operation shows all users in the app

    Parameters:
        -

    Returns a json list with all users in the app, with the following keys
        -   user_id: UUID
        -   email: EmailStr
        -   first_name: str
        -   last_name: str
        -   birth_day: datetime  
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results
### show a user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code = status.HTTP_200_OK,
    summary="show a user",   
    tags=["Users"]
    )
def show_a_user():
    pass

### Delete a user
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code = status.HTTP_200_OK,
    summary="Delete a user" ,  
    tags=["Users"]
    )
def delete_a_user():
    pass

### Update a user
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code = status.HTTP_200_OK,
    summary="Update a user" ,  
    tags=["Users"]
    )
def update_a_user():
    pass

##Tweets

### Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code = status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
    )
def home():
    return {"Twitter API: Working"}

### Post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code = status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
    )
def post():
    pass

### Show a tweet
@app.post(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code = status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
    )
def show_a_tweet():
    pass

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code = status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
    )
def delete_a_tweet():
    pass

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code = status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
    )
def update_a_tweet():
    pass

