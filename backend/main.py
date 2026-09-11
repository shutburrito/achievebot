from fastapi import FastAPI # this imports fastapi, this makes api calls fast and easier
from fastapi.staticfiles import StaticFiles
import os
app = FastAPI(title="AchieveBot API") #this makes a fastapi app called AchieveBot API
@app.get("/health")
async def health_check(): #these lines listen to /health and return a response if the server is running
    return {"status": "ok"} 

app.mount("/",StaticFiles(directory="web",html=True),name="web") #this connects the frontend files to the backend
