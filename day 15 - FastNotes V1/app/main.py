from fastapi import FastAPI
from app.notes import services as note_services

app = FastAPI()

@app.get("/notes")
async def get_notes():
    notes =  await note_services.get_notes()
    return notes

@app.post("/create/note")
async def create_note(new_note:dict):
    note = await note_services.create_note(title=new_note["title"],content=new_note["content"])
    return note

@app.get("/notes/{note_id}")
async def get_note_id(id:int):
    note = await note_services.get_note(id)
    return note

@app.put("/update/note/{note_id}")
async def update_note(id:int,new_note:dict):
    new_title = new_note.get("title")
    new_content = new_note.get("content")
    note = await note_services.update_note(id,new_title,new_content)
    return note

@app.patch("/patch/note/{note_id}")
async def update_note(id:int,new_note:dict):
    new_title = new_note.get("title")
    new_content = new_note.get("content")
    note = await note_services.update_note(id,new_title,new_content)
    return note

@app.delete("/delete/note/{note_id}")
async def delete_note(id:int):
    response = await note_services.delete_note(id)
    return response