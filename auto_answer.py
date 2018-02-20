# coding: utf-8
import sys
import time
import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

order = 0

class LoggingEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_modified(self, event):
        if (event.src_path).find("Session.txt") != -1:
            start_work()


def start_work():
    get_data()

def get_data():
    global order
    config_file = sys.path[0] + os.path.sep + "Session.txt"
    with open(config_file, 'r') as f:
        content = f.read()
        if content.__len__() > 3:           #防止读出为空
            try:
                data = json.loads(content)
                temp_order = data['data']['feeds'][0]['field']['question']['order']
                if  temp_order != order and temp_order != 0:
                    order = temp_order
                    print(order)
                    res = {}
                    res['content'] = data['data']['feeds'][0]['field']['question']['content']
                    res['options'] = data['data']['feeds'][0]['field']['question']['options']
                    return res
            except:
                pass


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()