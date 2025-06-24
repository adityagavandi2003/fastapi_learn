from sqlmodel import Field, SQLModel, Relationship

# relations


class UserAddressLink(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True , ondelete="CASCADE") # cascade
    address_id: int = Field(foreign_key="address.id", primary_key=True,ondelete="CASCADE") # cascade


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    email: str

    # relation attributes
    profile: "Profile" = Relationship(back_populates="user",cascade_delete=True)
    posts: list["Post"] = Relationship(back_populates="user",cascade_delete=True)
    address: list["Address"] = Relationship(
        back_populates="user", link_model=UserAddressLink,cascade_delete=True)

# One to One


class Profile(SQLModel, table=True):
    id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="user.id", unique=True, ondelete="CASCADE")
    bio: str
    user: "User" = Relationship(back_populates="profile")

# user.profile.bio
# profile.user.name


# One to Many
class Post(SQLModel, table=True):
    id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="user.id", ondelete="SET NULL", nullable=True)
    title: str
    content: str
    user: "User" = Relationship(back_populates="posts")

# user.posts
# post.user

# Many to Many
class Address(SQLModel, table=True):
    id: int = Field(primary_key=True)
    street: str
    city: str

    user: list["User"] = Relationship(back_populates="address", link_model=UserAddressLink,cascade_delete=True)

# user.address
# address.user 
