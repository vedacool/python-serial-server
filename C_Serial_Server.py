import time
import threading
from threading import Event
import B_Serial_Support as serialCOMMH


class Serial_Listener_Server(threading.Thread):
    def __init__(self, Comm_Port, Baud_Rate):
        threading.Thread.__init__(self)
        self.server = None
        self.Comm_Port = Comm_Port
        self.Baud_Rate = Baud_Rate
        self.stop_threads = Event()

    def Init_Server(self):
        print "[C_Serial_Server] Init_Server Start ... ... ..."
        while True:
            try:
                self.server = serialCOMMH.initialize(self.Comm_Port, self.Baud_Rate)
                print "[C_Serial_Server] Init_Server Start SUCCESS..."
                break
            except:
                print "[ERROR] [C_Serial_Server] Init_Server Start FAIL (Wrong PORT assignment)..."
                time.sleep(1)

    def run(self):
        self.Init_Server()
        self.Packet_Receive_Interface()

    def stop(self):
        self.stop_threads.set()

    def Packet_Receive_Interface(self):
        while not self.stop_threads.is_set():
            data_R = serialCOMMH.receive()
            if len(data_R) < 0 or data_R == None:
                print "[ERROR] [C_Serial_Server] Packet_Receive_Interface Wrong packet size"
                continue
            # Processing data start here
            print "[C_Serial_Server] Packet_Receive_Interface DATA = ", data_R  # Printing received data
            # Processing data end here

if __name__ == '__main__':
    S_TS = Serial_Listener_Server("COM12", 9600)
    S_TS.start()
