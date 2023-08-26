import signal

def handlers(signum, frame):
    print("Ctrl-c Detected, exiting process")
    exit(1)

signal.signal(signal.SIGINT, handlers)

while True:
    this = input("Hello: ")

