from asyncio import SubprocessProtocol, Future, subprocess
from json.decoder import JSONDecodeError
from typing import Dict
from enum import IntEnum
import functools
import asyncio
import json
import re

PATTERN = r'\*s\[== \"CMake Server\" ==\[\s*(.*)\s*\]== \"CMake Server\" ==]'
REGEX = re.compile(PATTERN, re.MULTILINE)

class Pipe(IntEnum):
    STDIN = 0
    STDOUT = 1
    STDERR = 2

class Protocol(SubprocessProtocol):
    transport = None
    promise: Future
    sources: Dict

    def __init__ (self, promise: Future):
        self.transport = None
        self.promise = promise
        self.sources = dict()
        super().__init__()

    def connection_made (self, transport):
        self.transport = transport

    def pipe_data_received (self, fd, data):
        if fd == Pipe.STDIN: return
        event = self.recv(data)
        print('received: ', event)
        # TODO: Consider requiring these 'receivers' be async?
        for receiver in self.sources.get(event['type'], []):
            receiver(event, self.stdout)

    def process_exited (self):
        code = self.transport.get_returncode()
        self.promise.set_result((code, None))

    def recv (self, data):
        match = REGEX.match(data.decode())
        if not match: return
        try: return json.loads(match.group(1))
        except JSONDecodeError: return

    def send (self, data):
        text = f'[== "CMake Server" ==[\n{json.dumps(data)}\n]== "CMake Server" ==]\n'
        self.stdout.write(text.encode())

    def pipe (self, fd: Pipe):
        return self.transport.get_pipe_transport(int(fd))

    @property
    def stdin (self): return self.pipe(Pipe.STDIN)

    @property
    def stdout (self): return self.pipe(Pipe.STDOUT)

    @property
    def stderr (self): return self.pipe(Pipe.STDERR)

# TODO: Take more args to pass to Protocol
async def run (loop=asyncio.get_event_loop(), protocol=Protocol):
    promise = Future(loop=asyncio.get_event_loop())
    factory = functools.partial(protocol, promise)
    args = ['cmake', '-E', 'server', '--experimental', '--debug']
    process = loop.subprocess_exec(factory, *args, stdin=subprocess.PIPE, stderr=None)
    print('Launching CMake Server')
    try: transport, protocol = await process
    except:
        transport.close()
        raise
    await promise
    return promise.result()