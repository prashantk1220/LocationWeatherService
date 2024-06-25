from fastapi import FastAPI, HTTPException
from kafka_consumer import user_data


app = FastAPI()


@app.get("/user/{user_id}")
async def get_user_weather(user_id: str):
    if user_id not in user_data:
        raise HTTPException(status_code=404, detail="User not found")

    return user_data[user_id]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
