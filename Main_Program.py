import C_Serial_Server as Server
import time

S_TS = Server.Serial_Listener_Server("COM20", 9600)
S_TS.start()

time.sleep(2)
while 1:
    # Do something
    time.sleep(1)
