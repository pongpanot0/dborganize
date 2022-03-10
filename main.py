from database import models
from database.database import engine
from fastapi import FastAPI
import uvicorn
from routes import user,organization,organizationsetting,systemtheme,systemlangaue,user_assign_role,roles,assets

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)



@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(user.router)
app.include_router(organization.router)
app.include_router(organizationsetting.router)
app.include_router(systemtheme.router)
app.include_router(systemlangaue.router)
app.include_router(user_assign_role.router)
app.include_router(roles.router)
app.include_router(assets.router)
models.Base.metadata.create_all(engine)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", debug=True, port=8001, log_level="debug")
