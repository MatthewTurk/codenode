
import os

from codenode.backend.engine import EngineConfigurationBase

boot = """import threading
from IPython.kernel.scripts import ipcontroller
from codenode.backend.kernel.engine.server import EngineIPythonRPCServer
from codenode.backend.kernel.engine.python.interpreter import IPControllerInterpreter
from codenode.backend.kernel.engine.python.runtime import build_namespace
namespace = build_namespace
import os
import sys
import socket
s = socket.socket()
s.bind(('',0))
port = s.getsockname()[1]
s.close()
del s
server = EngineRPCServer(('localhost', port), Interpreter, namespace)
sys.stdout.write('port:%s' % str(port))

ipct = threading.Thread(target = ipcontroller.start_controller)
ipct.start()

# Now we spawn our mpirun tasks
def spawn_ipengine():
    os.system("mpirun -np 4 ipengine") # we assume ipengine is in the path
ipe = threading.Thread(target = spawn_ipengine)
ipe.start()

server.serve_forever()
"""

print os.environ['PATH']

class IPController(EngineConfigurationBase):
    bin = 'python'
    args = ['-c', boot]
    env = os.environ
    path = '/tmp'


ipcontroller = IPController()

