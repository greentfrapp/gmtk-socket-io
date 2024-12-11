import socketio
from fastapi import FastAPI

app = FastAPI()
sio = socketio.AsyncServer(cors_allowed_origins="*", async_mode="asgi")
# socket_app = socketio.ASGIApp(sio)
socketio_app = socketio.ASGIApp(sio, app)

# app.mount("/", socket_app)

room_id = "123"


@sio.event
async def connect(sid, env):
    await sio.enter_room(sid, room_id)
    print("New Client Connected to This id :" + " " + str(sid))


@sio.event
async def disconnect(sid):
    await sio.leave_room(sid, room_id)
    print("Client Disconnected: " + " " + str(sid))


@sio.event
async def message(sid, data):
    await sio.emit("message", data, room=room_id, skip_sid=sid)


@app.get("/")
async def root():
    return {"message": "Hello World"}
