from library.daemon import Daemon
import time

class versioning(Daemon):
    def run(self):
        
        pass        
        
daemon = versioning('/tmp/versioning.pid')
daemon.run()