import asyncio

class TcpConnector(asyncio.Transport):
    def connection_made(self, transport: asyncio.Transport):
       transport.close()
    def connection_lost(self, exc):
        pass



async def try_connet(ip, port): 
    loop = asyncio.get_running_loop()
    await asyncio.wait_for(loop.create_connection(TcpConnector, ip, port), 10)
    return port

async def main():
    ip = '127.0.0.1'
    portrange = (138, 1000)

    loop = asyncio.get_running_loop()

    corutines = []

    def callback (corutine):
        corutines.remove(corutine)
        print(corutine.result())


    for port in range (*portrange):
        corutines.append(loop.create_task(try_connet(ip, port)))
        corutines[-1].add_done_callback(callback)

    while (len(corutines))>0:
        await asyncio.sleep(1)


asyncio.run(main())