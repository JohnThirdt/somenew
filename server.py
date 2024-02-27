import socket
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level = logging.INFO)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 10000))
while True:
    message, (ip, port) = s.recvfrom(500)
    logger.info(f"{ip}: {message.decode()}")



