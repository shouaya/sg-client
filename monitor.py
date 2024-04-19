import asyncio
import socketio
import pyautogui

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')
    await sio.emit('chat message', {'response': 'hello'})

@sio.on('chat message')
async def on_message(data):
    print('message received with ', data)
    if "e" in data:
        target = getSgWinName('三國志')
        if target is None:
            print('can not find game 三國志')
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
    await sio.connect('http://127.0.0.1:3000')
    await sio.wait()

def getSgWinName(title):
    for x in pyautogui.getAllWindows():
        if x.title.startswith(title):
            return x
    return None
if __name__ == '__main__':
    target = getSgWinName('三國志')
    
    if target is None:
        print('can not find game 三國志')
        exit(1)
    target.maximize()
    target.resizeTo(900, 600)
    target.moveTo(0, 0)
    target.activate()
    #asyncio.run(main())