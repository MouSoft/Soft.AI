# نقطة تشغيل API

from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "SoftAI API جاهزة"}
