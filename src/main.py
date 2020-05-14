from threading import Thread
from utils import ROOT, prepare_start

from recorders.keyboard import KeyboardRecorder
from recorders.mouse import MouseRecorder
from interpreter import Interpreter
from controller import Controller


INITIAL_MESSAGE = '''
---------- WELCOME ----------
Type "R" to record your keyboard and mouse.
Type "P" to play your already saved record.
'''

def recordMirror():
    name = input("Record's name: ")

    try:
        record = open(ROOT.joinpath('src', 'mirrors', f'{name}.mirror'), 'a')
    except:
        print("---! Cannot create record file.")
        raise
    delay_information = [None]

    k_recorder = KeyboardRecorder(record, delay_information)
    k_thread = Thread(target=k_recorder.start)

    m_recorder = MouseRecorder(record, delay_information, k_thread.is_alive)
    m_thread = Thread(target=m_recorder.start)

    prepare_start()
    k_thread.start()
    m_thread.start()

def playMirror():
    name = input("Record's name: ")

    try:
        record = open(ROOT.joinpath('src', 'mirrors', f'{name}.mirror'), 'r')
    except:
        print("---! Cannot open record file.")
        raise 
    
    stream = Interpreter(record).get_stream()

    prepare_start()
    Controller(stream).start()

def main():
    print(INITIAL_MESSAGE)
    res = input('-> ').lower()

    if res == 'r': recordMirror()
    elif res == 'p': playMirror()
    else: quit()

if __name__ == "__main__":
    main()