from datetime import timedelta, datetime

import serial


def get_voltage(port, nplc=1):
    ser = serial.Serial(port=port, baudrate=9600)
    ser.reset_input_buffer()
    result = []
    time_start = datetime.now() + timedelta(milliseconds=10)
    nplc = nplc
    while nplc > 0:
        data = ser.readline()
        if time_start < datetime.now():
            voltage = float(data.decode().strip())
            result.append(voltage)
            print(voltage)
            nplc -= 1
    ser.close()
    return result


if __name__ == "__main__":
    get_voltage('/dev/ttyACM0', 10)


