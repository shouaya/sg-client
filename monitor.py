import asyncio
import socketio
import pyautogui
import sys
import urllib.parse

sio = socketio.AsyncClient()

gameName = '三國志'
webServer = 'http://127.0.0.1:3000'
myID = 'test'

@sio.event
async def connect():
    print('connection established')
    await sio.emit('chat message', {'connect': 'hello', 'fid': myID})

@sio.on('chat message')
async def on_message(data):
    print('message received with ', data)
    if "e" in data:
        if data['tid'] != myID:
            return
        target = getSgWinName(gameName)
        if target is None:
            print('can not find game ' + gameName)
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
    await sio.connect(webServer)
    await sio.wait()

def getSgWinName(title):
    for x in pyautogui.getAllWindows():
        if x.title.startswith(title):
            return x
    return None
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('url not found')
        exit(1)
    if not sys.argv[1].startswith('weget'):
        print('unkown url')
        exit(1)
    argstr = urllib.parse.unquote(sys.argv[1].strip("weget://?"))    
    args = argstr.split(" ")
    print(args)
    if len(args) != 3:
        print('please input game_name server_url id')
        exit(1)
    gameName = args[0]
    webServer = args[1]
    myID = args[2]

    target = getSgWinName(gameName)
    if target is None:
        print('can not find game ' + gameName)
        exit(1)
    target.maximize()
    target.resizeTo(900, 600)
    target.moveTo(0, 0)
    target.activate()
    asyncio.run(main())
#python monitor.py 三國志 http://127.0.0.1:3000 EGqG0NSZUmTdpo_xAAAN
#python monitor.py weget://%E4%B8%89%E5%9C%8B%E5%BF%97%20http%3A%2F%2F127.0.0.1%3A3000%20EGqG0NSZUmTdpo_xAAAN/