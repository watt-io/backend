from fastapi import FastAPI


from views.serializer.to_json import build_toJson
from views import home_schemas


api = FastAPI()

@api.get("/", response_model=home_schemas.home)
async def home():
    msg = "Api connection successfully"
    return build_toJson(200,msg )
