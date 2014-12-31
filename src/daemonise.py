import daemon
import time

def do_something(uid):
    while True:
        with open("/tmp/current_time.txt", "w") as f:
            f.write(uid + ": The time is now " + time.ctime())
        time.sleep(5)

def run():
    with daemon.DaemonContext():
        do_something()

if __name__ == "__main__":
    run()