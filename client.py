from pyModbusTCP.client import ModbusClient

slave_address = '0.0.0.0'
port = 5020 
unit_id = 1

modbus_client = ModbusClient(host=slave_address, port=port, unit_id=unit_id, auto_open=True)

if __name__ == '__main__':
    while True:
        regs = modbus_client.read_holding_registers(0,2)
        print(regs)


