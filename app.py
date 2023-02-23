from os.path import isfile
from fastapi import Response, FastAPI, Request  
from mimetypes import guess_type
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="build")

app = FastAPI()
# Fronted Mounting (Prod/staging fail without them)
app.mount("/static", StaticFiles(directory="./build/static"), name="static")
app.mount("/public", StaticFiles(directory="./build"), name="public")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
)

@app.get("/main.js")
@app.get("/universal_support.js")
@app.get("/universal_dm.js")
async def get_universal_dm_js():
    filename = "./build/static/js/main.js"
            
    if not isfile(filename):
        return Response(status_code=404)

    with open(filename) as f:
        content = f.read()

    content_type, _ = guess_type(filename)
    return Response(content, media_type=content_type)

@app.get("/main.css")
@app.get("/universal_support.css")
@app.get("/universal_dm.css")
async def get_universal_dm_css():
    filename = "./build/static/css/main.css"

    if not isfile(filename):
        return Response(status_code=404)

    with open(filename) as f:
        content = f.read()

    content_type, _ = guess_type(filename)
    return Response(content, media_type=content_type)

# Handles serving of app
@app.api_route("/{path_name:path}", methods=["GET"], include_in_schema=False)
def serve_app(request: Request, response: Response):
    response.headers["Cache-Control"] = "s-maxage=3600"
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8081)