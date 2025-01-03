from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os
import time

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.restart()

    def restart(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        self.process = subprocess.Popen(["python", self.script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"File changed: {event.src_path}. Restarting...")
            self.restart()

if __name__ == "__main__":
    script_to_watch = "main.py"  # Replace with your Kivy app file name
    handler = ReloadHandler(script_to_watch)
    observer = Observer()
    observer.schedule(handler, path=os.path.dirname(os.path.abspath(script_to_watch)), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    handler.process.terminate()
    observer.join()
