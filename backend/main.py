from fastapi import FastAPI
from . import models
from .database import engine
from .controller import user, case, project, team_member, authendication
from fastapi.middleware.cors import CORSMiddleware
#import uvicorn
from fastapi_pagination import add_pagination


# On video 3:30
# TODO
# repository/delete problem

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authendication.router)
app.include_router(user.router)
app.include_router(case.router)
app.include_router(project.router)
app.include_router(team_member.router)



# app.router.redirect_slashes = False

origins = ["*"]
# origins = [
#   "http://localhost:3000",
#   "https://localhost:3000",
#   "http://localhost:3001",
#   "https://localhost:3001",
#   "http://www.bugflix.eu:3001",
#   "https://www.bugflix.eu:3001",
#   "http://www.bugflix.eu:8000",
#   "https://www.bugflix.eu:8000",
#   "http://127.0.0.1:8000",
#   "https://127.0.0.1:8000",
#   "http://localhost:8000",
#   "https://localhost:8000",
#   "http://185.237.15.246:3001",
#   "https://185.237.15.246:3001",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_pagination(app)
