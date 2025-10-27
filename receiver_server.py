
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/data")
def get_data():
    return {"message": "Data received successfully!", "status": "OK"}

@app.post("/data")
async def post_data(request: Request):
    data = await request.json()
    print("📦 Received data:", data)
    return {"message": "Data received and logged", "data": data}
