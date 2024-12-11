import socketio
from fastapi import FastAPI

app = FastAPI()
sio = socketio.AsyncServer(cors_allowed_origins="*", async_mode="asgi")
# socket_app = socketio.ASGIApp(sio)
socketio_app = socketio.ASGIApp(sio, app)

# app.mount("/", socket_app)


@sio.event
async def connect(sid, env):
    print("New Client Connected to This id :" + " " + str(sid))


@sio.event
async def disconnect(sid):
    print("Client Disconnected: " + " " + str(sid))


@app.get("/")
async def root():
    return {"message": "Hello World"}
