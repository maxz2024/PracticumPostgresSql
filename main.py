import models
from fastapi import FastAPI
from controllers import user, film, author, genre

app = FastAPI(title="Онлайн кинотератр", version="1.1.0")
app.include_router(user.router)
app.include_router(author.router)
app.include_router(film.router)
app.include_router(genre.router)

import uvicorn

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



