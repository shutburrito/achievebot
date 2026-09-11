import os
from dotenv import load_dotenv #allows the program to access the .env folder for variables
load_dotenv() #loads .env 
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN") #these get the variables from the .env, but gives the defaults if it cant find it
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")