from fastapi import FastAPI
from app.api.api_v1.api import api_router
from app.core.config import settings
from app.db.base_class import Base
from app.db.session import engine
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI(
    title=settings.PROJECT_NAME
)


# add this for handling Unprocessible entity erros (422) -> 400
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):

    return JSONResponse(status_code=400, content={"errors": "Invalid data"})


Base.metadata.create_all(bind=engine)



app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def home():
    return {"message": "Ok"}