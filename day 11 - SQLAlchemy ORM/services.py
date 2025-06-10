from sqlalchemy import asc, select
from db import engine,SessionLocal
from models import *

# insert and create user
def create_User(name:str,email:str):
    with SessionLocal() as session:
        user = Users(name=name,email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
# Insert or create post
def create_post(user_id:int,title:str,caption:str):
    with SessionLocal() as session:
        post = Post(user_id=user_id,title=title,caption=caption)
        session.add(post)
        session.commit()
        session.refresh(post)
        return post
    
# read user by id
def get_user_by_id(user_id: int):
    with SessionLocal() as session:
      user = session.get_one(Users, user_id)
      return user

# Read post by ID
def get_post_by_id(post_id:int):
    with SessionLocal() as session:
        smtm = select(Post).where(Post.post_id==post_id)
        post = session.scalars(smtm).one()
        return post

# Read All user
def get_all_users():
    with SessionLocal() as session:
        stmt = select(Users)
        users = session.scalars(stmt).all()
        return users
    
# Update user email
def update_user_email(user_id: int, new_email: str):
    with SessionLocal() as session:
       user = session.get(Users, user_id)
       if user:
          user.email = new_email
          session.commit()
       return user

# Read all posts for an user
def get_posts_by_user(user_id: int):
    with SessionLocal() as session:
       user = session.get(Users, user_id)
       posts = user.posts if user else []
       return posts

# Delete Post
def delete_post(post_id:int):
    with SessionLocal() as session:
        post = session.get(Post,post_id)
        if post:
            session.delete(post)
            session.commit()
            return f"Post deleted ({post_id})"

# Order by
def get_users_ordered_by_name():
    with SessionLocal() as session:
       stmt = select(Users).order_by(asc(Users.name))
       users = session.scalars(stmt).all()
       return users