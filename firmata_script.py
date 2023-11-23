from pyfirmata import Arduino, util
import time


def get_voltage(port, nplc=1):
    board = Arduino(port)
    it = util.Iterator(board)
    it.start()
    analog_0 = board.get_pin('a:0:i')
    result = []
    nplc = nplc
    while nplc > 0:
        time.sleep(0.5)
        val = analog_0.read()
        if val is None:
            print(val)
            continue
        voltage = round(float(val) * 5, 2)
        result.append(voltage)
        print(voltage)
        nplc -= 1
    return result


if __name__ == "__main__":
    get_voltage('/dev/ttyUSB0', 10)
