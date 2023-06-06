# SRC IMPORTS
from File_Man import File_man
from listen_1 import Listen_

# BASE IMPORTS
import asyncio
import websockets
import subprocess

#all_clients = []


# OOP
class SnrokL_Node():
    def __init__(self, **kw):
        super(SnrokL_Node, self).__init__(**kw)
        # SRCS
        self.FM         = File_man()
        self.Li         = Listen_()


        # ThisClass
        self.addr       = "127.0.0.1"
        self.port       = 8081
        self.server     = None
        self.clients    = []

    async def send_msg(self, client, msg_: str):
        """
        Return MSG to client
        """
        print(f"\n-[SENDING]:[{msg_}]\n-[TO]:[{client}]")
        await client.send(msg_)

    async def handle_client(self, websocket, cl_id, msg_, path):
        try:
            print(f'\n~[ClientHandOff]:[{str(cl_id)}]:[{str(websocket)}]')
            print(f"\n~[FROM_CLIENT]:[{str(msg_)}]")
            if "cmd" in str(msg_):
                print(f"[$]:[{str(msg_)}]")
                cmd_ = str(msg_.split("$")[1])
                p = subprocess.Popen(cmd_, stdout=subprocess.PIPE, shell=True)
                out, err = p.communicate()
                ret_msg = str(cl_id) + "|:|" + str(out.decode())
            if "node" in str(msg_):
                print("Accessing-NODE")
                if "add-rule" in str(msg_):
                    print("[Adding Rule]")
                    # Append new rule to 'rules.txt'
                if "get_stream" in str(msg_):
                    print("Updating User - Collected Data")
                    # Read data from 'DATA' folder
                    # -> give options to choose which file to read

            await self.send_msg(websocket, ret_msg)
        except Exception as e:
            print(f"[E]:[HANDLE_CLIENT]:[{str(e)}]")

    async def new_client_conn(self, client_socket, path):
        """
        Identify New Client Connection
        """
        self.clients.append(client_socket)
        cl_id = len(self.clients)
        print(f"[+]:[NEW CLIENT CONNECTED]:[>{str(path)}<]")
        while True:
            msg_ = await client_socket.recv()
            print(f"[FROM_CLIENT]:[{str(msg_)}]")
            if "[CONN_REQ]" in str(msg_):
                print("[@]:[CONNECTION_REQUEST]")
                await RN.send_msg(client_socket, "[REQUEST_APPROVED]")
            else:
                await RN.handle_client(client_socket, cl_id, msg_, path)

    async def start_server(self):
        """
        Start Endless Server Loop
        """
        print("[WEB_SERVER_STARTED]")
        await websockets.serve(self.new_client_conn, 'localhost', 12345)


if __name__=="__main__":
    SN = SnrokL_Node()
    SN.event_loop = asyncio.get_event_loop()
    SN.event_loop.run_until_complete(SN.start_server())
    SN.event_loop.run_forever()






# NoOOP



SIS= """
 async def send_msg(msg_: str):
    for i, client in enumerate(all_clients):
        print(f'[TO]:[{str(i)}]:[{str(client)}]')
        await client.send(msg_)


async def new_client_conn(client_socket, path):
    all_clients.append(client_socket)
    while True:
        msg_ = await client_socket.recv()
        await send_msg('sis:'+msg_)

async def start_server():
    await websockets.serve(new_client_conn, '127.0.0.1', 8083)

if __name__=="__main__":
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_server())
    event_loop.run_forever()
"""