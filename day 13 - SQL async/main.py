from models import create_table,drop_tables
import asyncio
from services import * 

async def main():
    # create tables
    await create_table()
    # drop tables
    # await drop_tables()

    # create data
    # await create_user("aditya","aditya@gmail.com")
    # await create_user("raj","raj@gmail.com")

    # get user by id
    # print(await get_userby_id(1))

    # get all users
    # print(await get_all_user())

    # update user email
    # await update_user_email(1,"aditya@yahoo.com")
    # delete user
    # await delete_user(2)

asyncio.run(main())