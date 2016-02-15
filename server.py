import asyncio

class Server(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('bağlantı geldi {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        print('veri alındı: {}'.format(data.decode()))

        #self.transport.write(data)

loop = asyncio.get_event_loop()
coro = loop.create_server(Server, 'localhost', 8888)
server = loop.run_until_complete(coro)

print('sunucu başlatıldı {}'.format(server.sockets[0].getsockname()))

try:
    loop.run_forever()
except KeyboardInterrupt:
    print("elveda")
finally:
    server.close()
    loop.close()