from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(title="AV-SIM Research Simulator v2")

@app.get("/")
def root():
    return FileResponse("templates/index.html")
