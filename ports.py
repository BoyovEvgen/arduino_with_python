
from serial.tools.list_ports import comports


def get_connected_ports():
    connected_ports = [elem.device for elem in comports()]
    print('Connected COM ports: ' + str(connected_ports))
    return connected_ports


if __name__ == "__main__":
    get_connected_ports()

