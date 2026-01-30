from fastapi import FastAPI
from routes.feature_flags import feature_flag_router

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}


app.include_router(feature_flag_router, tags=["Feature_Flags"], prefix="/feature_flags")