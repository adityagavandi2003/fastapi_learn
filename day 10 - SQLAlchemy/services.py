from db import engine
from tables import user, posts
from sqlalchemy import insert, select, text, update, delete, asc, desc, func


# Insert or Create User
def create_user(name: str, email: str):
  with engine.connect() as conn:
    stmt = insert(user).values(name=name, email=email)
    conn.execute(stmt)
    conn.commit()

# Insert or Create Post
def create_post(user_id: int, title: str, content: str):
    with engine.connect() as conn:
        stmt = insert(posts).values(user_id=user_id, title=title, content=content)
        conn.execute(stmt)
        conn.commit()

# Get Single User by ID
def get_user_by_id(user_id: int):
   with engine.connect() as conn:
        stmt = select(user).where(user.c.id == user_id)
        result = conn.execute(stmt).first()
        return result
   
# Get All Users
def get_all_users():
   with engine.connect() as conn:
        stmt = select(user)
        result = conn.execute(stmt).fetchall()
        return result
   
# Get Post by User
def get_posts_by_user(user_id: int):
   with engine.connect() as conn:
        stmt = select(posts).where(posts.c.user_id == user_id)
        result = conn.execute(stmt).fetchall()
        return result
   
# Update User Email
def update_user_email(user_id: int, new_email: str):
   with engine.connect() as conn:
        stmt = update(user).where(user.c.id == user_id).values(email=new_email)
        conn.execute(stmt)
        conn.commit()

# Delete Post
def delete_post(post_id: int):
   with engine.connect() as conn:
        stmt = delete(posts).where(posts.c.id == post_id)
        conn.execute(stmt)
        conn.commit()


# Get All Users Ordered by Name (A-Z)
def get_users_ordered_by_name():
    with engine.connect() as conn:
        stmt = select(user).order_by(asc(user.c.name))
        result = conn.execute(stmt).fetchall()
        return result

# Get All Posts Ordered by Latest
def get_posts_latest_first():
    with engine.connect() as conn:
        stmt = select(posts).order_by(desc(posts.c.id))
        result = conn.execute(stmt).fetchall()
        return result
    
# Group Posts by User (Count how many posts each user has)
def get_post_count_per_user():
    with engine.connect() as conn:
        stmt = select(
            posts.c.user_id,
            func.count(posts.c.id).label("total_posts")
        ).group_by(posts.c.user_id)
        result = conn.execute(stmt).fetchall()
        return result
    
# Join Users and Posts (List all posts with author names)
def get_posts_with_author():
    with engine.connect() as conn:
        stmt = select(
           posts.c.id,
           posts.c.title,
           user.c.name.label("author_name")
        ).join(user, posts.c.user_id == user.c.id)
        result = conn.execute(stmt).fetchall()
        return result
    
# Using RAW SQL (Insert)
def raw_sql_insert():
  with engine.connect() as conn:
    stmt = text("""
                INSERT INTO users (name, email)
                VALUES (:name, :email)
                """)
    conn.execute(stmt, {"name": "aditya", "email":"aditya@example.com"})
    conn.commit()

# Using RAW SQL (SELECT)
def raw_sql_example():
    with engine.connect() as conn:
        stmt = text("SELECT * FROM users WHERE email = :email")
        result = conn.execute(stmt, {"email": "aditya@example.com"}).first()
        return result