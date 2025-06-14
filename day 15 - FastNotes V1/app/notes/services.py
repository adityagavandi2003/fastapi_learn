from app.db.config import async_session
from app.notes.models import Notes
from sqlalchemy import Select
from fastapi import  HTTPException


# create a note
async def create_note(title:str,content:str):
    async with async_session() as session:
        note = Notes(title=title,content=content)
        session.add(note)
        await session.commit()
        await session.refresh(note)
        return note
    
# read all notes 
async def get_notes():
    async with async_session() as session:
        stmt = Select(Notes)
        notes = await session.scalars(stmt)
        return notes.all()
    
# get note by id
async def get_note(id:int):
    async with async_session() as session:
        note = await session.get(Notes,id)
        if note is None:
            raise HTTPException(status_code=404,detail="Not found")
        return note
    
# update note
async def update_note(id:int,new_title:str,new_content:str):
    async with async_session() as session:
        note = await session.get(Notes,id)
        if note is None:
            raise HTTPException(status_code=404,detail="Not found")
        note.title = new_title
        note.content = new_content
        await session.commit()
        await session.refresh(note)
        return note

# patch note
async def patch_note(note_id: int, new_title: str | None = None, new_content: str | None = None):
    async with async_session() as session:
        note = await session.get(Notes, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Not found")

        if new_title is not None:
            note.title = new_title
        if new_content is not None:
            note.content = new_content

        await session.commit()
        await session.refresh(note)
        return note

    
# delete note
async def delete_note(id:int):
    async with async_session() as session:
        note = await session.get(Notes,id)
        if note is None:
            raise HTTPException(status_code=404, detail="Not found")
        await session.delete(note)
        await session.commit()
        return {"message":"deleted"}
