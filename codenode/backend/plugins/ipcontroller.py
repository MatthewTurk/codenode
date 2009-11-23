
import os

from codenode.backend.engine import EngineConfigurationBase

boot = """import threading, subprocess
from IPython.kernel.scripts import ipcontroller
from codenode.engine.server import EngineRPCServer
from codenode.engine.interpreter import IPControllerInterpreter
from codenode.engine import runtime
import time
import os
import sys
import socket

port = runtime.find_port()
runtime.ready_notification(port)

pid1 = subprocess.Popen("ipcontroller", shell=True).pid
time.sleep(5)

pid2 = subprocess.Popen("mpirun -np 4 ipengine --mpi=mpi4py", shell=True).pid
time.sleep(5)

namespace = runtime.build_namespace
server = EngineRPCServer(('localhost', port), IPControllerInterpreter, namespace)
server.serve_forever()
"""

print os.environ['PATH']

class IPController(EngineConfigurationBase):
    bin = 'python'
    args = ['-c', boot]
    env = os.environ
    path = '/tmp'


ipcontroller = IPController()

