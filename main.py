from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from data_models import UserData
from kafka_consumer import user_data


app = FastAPI()


@app.get("/user/{user_id}")
async def get_user_weather(user_id: int) -> UserData:
    if user_id not in user_data:
        raise HTTPException(status_code=404, detail="User not found")

    return UserData(**user_data[user_id])


@app.get("/")
async def docs_redirect():
    response = RedirectResponse(url='/docs')
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
