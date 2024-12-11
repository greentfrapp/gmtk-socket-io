import socketio
from aiohttp import web

sio = socketio.AsyncServer(cors_allowed_origins="*")
app = web.Application()
sio.attach(app)

room_id = "123"


@sio.event
async def connect(sid, environ):
    await sio.enter_room(sid, room_id)
    print("connect ", sid)


@sio.event
async def message(sid, data):
    await sio.emit("message", data, room=room_id, skip_sid=sid)


@sio.event
async def disconnect(sid):
    await sio.leave_room(sid, room_id)
    print("disconnect ", sid)


if __name__ == "__main__":
    web.run_app(app)
