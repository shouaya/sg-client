import asyncio
import socketio
import pyautogui
import sys

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')
    await sio.emit('chat message', {'connect': 'hello', 'fid': sys.argv[3]})

@sio.on('chat message')
async def on_message(data):
    print('message received with ', data)
    if "e" in data:
        if data['tid'] != sys.argv[3]:
            return
        target = getSgWinName(sys.argv[1])
        if target is None:
            print('can not find game ' + sys.argv[1])
            exit(1)
        if target.left < 0:
            target.maximize()
            target.resizeTo(900, 600)
            target.moveTo(0, 0)
            target.activate()

        if data['e'] == 'c':
            if data['x'] > 20 and data['x'] < 880 and data['y'] < 580 and data['y'] > 20:
                pyautogui.click(data['x'], data['y'])
        else:
            if data['tx'] > 20 and data['tx'] < 880 and data['ty'] < 580 and data['ty'] > 20:
                pyautogui.moveTo(data['fx'], data['fy'], duration = 0)
                pyautogui.dragTo(data['tx'], data['ty'], duration = 1)

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    #await sio.connect('http://sg.weget.jp')
    await sio.connect(sys.argv[2])
    await sio.wait()

def getSgWinName(title):
    for x in pyautogui.getAllWindows():
        if x.title.startswith(title):
            return x
    return None
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('please input game_name server_url id')
        exit(1)
    target = getSgWinName(sys.argv[1])
    if target is None:
        print('can not find game ' + sys.argv[1])
        exit(1)
    target.maximize()
    target.resizeTo(900, 600)
    target.moveTo(0, 0)
    target.activate()
    asyncio.run(main())
#python monitor.py 三國志 http://127.0.0.1:3000 EGqG0NSZUmTdpo_xAAAN