from client import app

while 1:
    data = app.recordAudio()
    app.jarvis(data)