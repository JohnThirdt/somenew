import socket
import logging

logger = logging.getLogger(__name__)
logging.basicConfig()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4, tcp

c = s.bind(('127.0.0.1', 8080))  # случшать "на адресе", порте
s.listen(5)  # количество соединений в очереди, если не успеваем обслуживать

s.setblocking(False)  # не блокироваться на .accept()
s.settimeout(1)  # после этого таймаута, бросается TimeoutError, если не было соединения

while True:
    try:
        client_socket = s.accept()  # ожидание подключения клиента
    except TimeoutError:
        continue
    client, (addr, port) = client_socket
    logger.warning(f"{addr} connected from port {port}")

    incoming = client.recv(500)  # получение данных от клиента
    
    content = ''
    
    client.send(content)
    client.close()  # это сигналит клиенту, что данные все отправлены; иначе "вечная загрузка"