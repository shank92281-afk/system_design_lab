from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI Docker receiver is live!"}

@app.post("/trigger")
async def trigger(request: Request):
    data = await request.json()
    print("🔔 Received trigger:", data)
    return {"status": "success", "data": data}

