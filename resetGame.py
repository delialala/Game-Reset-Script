import os
import signal
import subprocess
import time
from pynput import keyboard

path = 'D:\Games\Rune Factory 5\Rune Factory 5.exe'
p = subprocess.Popen([path])
runeId = p.pid

def on_activate_h():
    pass

def on_activate_i():
    global runeId

    print('<ctrl>+<alt>+i pressed')
    print(runeId)

    os.kill(runeId, signal.SIGTERM)
    time.sleep(1)

    print("har har har")
    p = subprocess.Popen([path])
    print(p.pid)
    
    runeId = p.pid

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+h': on_activate_h,
        '<ctrl>+<alt>+i': on_activate_i}) as h:
    h.join()