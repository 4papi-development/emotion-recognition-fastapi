# Run fastapi hello world
from fastapi import FastAPI, Request, File
import os
# model
import SER_RT
SER_RT.trainModel()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Get file from api example
@app.post("/uploadfile/")
async def create_upload_file(file: bytes = File(...)):
    return {"file_size": len(file)}


# Get file and predict emotion
@app.post("/predict")
async def predict_emotion(file: bytes = File(...)):
    # Get file from request
    file = file
    # Print it to filename as wav
    filename = "buff.wav"
    # Delete if exists
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, "wb") as f:
        f.write(file)

    # Predict emotion
    emotion = SER_RT.predictAudioAndGet(filename)
    # Return emotion
    return {"result":emotion}

# fastapi application run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Run uvicorn
