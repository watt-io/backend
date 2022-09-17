from fastapi import FastAPI


from views.serializer.to_json import build_toJson
from views import default_schemas


api = FastAPI()

@api.get("/", response_model=default_schemas.Base)
async def home():
    msg = "Api connection successfully"
    return build_toJson(200,msg)

@api.get("/v1/api/movies", response_model=default_schemas.Base)
async def get_all_movies():
    msg = "Return all movies here"
    return build_toJson(200, msg)

