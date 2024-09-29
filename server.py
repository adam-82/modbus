from pyModbusTCP.server import ModbusServer, DataBank
import random
import time
import logging

logging.basicConfig()
logging.getLogger('pyModbusTCP.server').setLevel(logging.DEBUG)

host = '0.0.0.0'
port = 5020


class piDataBank(DataBank):
    def __init__(self):
        super().__init__()

    def get_holding_registers(self, address, number=1, srv_info=None):

        self._h_regs[0] = 50
        self._h_regs[1] = 100

        try:
            return[self._h_regs[i] for i in range(address, address+number)]
        except KeyError:
            return         


if __name__ == '__main__':
    Server = ModbusServer(host=host, port=port, data_bank=piDataBank())
    Server.start()
