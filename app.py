import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only, restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    file_name = __file__.split("\\")[-1].split(".")[0]
    uvicorn.run(f"{file_name}:app", host="127.0.0.1", port=8000, reload=True)


# http://127.0.0.1:8000
# http://127.0.0.1:8000/docs
