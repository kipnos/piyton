import asyncio

class Client(asyncio.Protocol):
    TIMEOUT = 0.2
    event_list = []
    x = 0
    for i in range(10000):
        event_list.append('mesaj' + str(i))

    def __init__(self):
        self.client_tcp_timeout = None
        print(self.event_list)

    def connection_made(self, transport):
        print('Sunucuya bağlandı.')
        self.transport = transport
        self.client_tcp_timeout = loop.call_later(self.TIMEOUT, self.send_from_call_later)

    def data_received(self, data):
        self.data = format(data.decode())
        print('veri alındı: {}'.format(data.decode()))

    def send_from_call_later(self):
        self.msg = self.event_list[0].encode()
        self.msg = "mesaj" + str(self.x)
        self.transport.write(self.msg.encode())
        self.x = self.x + 1
        print('veri gönderildi: {}'.format(self.msg))
        print('veri silindi: {}'.format(self.event_list[0]))
        del self.event_list[0]
        #print(self.event_list)
        print('----------------------#-------------------')
        if len(self.event_list) > 0:
            self.client_tcp_timeout = loop.call_later(self.TIMEOUT, self.send_from_call_later)
        else:
            deneme = 'Tüm veriler sunucuya gönderildi.'
            self.transport.write(deneme.encode())

    def connection_lost(self, exc):
        print('Bağlantı koptu.')

loop = asyncio.get_event_loop()

coro = loop.create_connection(Client, '192.168.1.39', 8888)
client = loop.run_until_complete(coro)

loop.run_forever()