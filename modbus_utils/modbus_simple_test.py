import logging
import asyncio
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

FORMAT = (
    "%(asctime)-15s %(threadName)-15s "
    "%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s"
)
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

UNIT = 0x1


async def run_sync_client():
    """Run sync client."""

    client = ModbusClient(method="rtu", port="/dev/ttyUSB0", timeout=2,
            baudrate=9600)
    client.connect()

    rr = client.read_holding_registers(8206, 5, unit=UNIT)
    if not rr.isError():
        print(rr.registers)
    else:
        print("error: {}".format(rr))

    while(True):
        log.debug("====================================================")
        log.debug("Surrounding: {}".format(rr.registers[0]))
        log.debug("Table: {}".format(rr.registers[1]))
        log.debug("K-factor: {}".format(rr.registers[2]))
        log.debug("Feedback-factor: {}".format(rr.registers[3]))
        log.debug("Target temp: {}".format(rr.registers[4]))
        log.debug("====================================================")
        await asyncio.sleep(1)
    client.close()


async def main():
    await asyncio.gather(run_sync_client())

asyncio.run(main())