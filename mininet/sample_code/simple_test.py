#!/usr/bin/python                                                                            
                                                                                             
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController
from mininet.link import Link, TCLink
from mininet.cli import CLI 
from time import sleep

class RingTopo(Topo):
    def __init__(self, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)

        # Add switch
        switch0 = self.addSwitch('s0', protocols='OpenFlow13')
        switch1 = self.addSwitch('s1', protocols='OpenFlow13')
        switch2 = self.addSwitch('s2', protocols='OpenFlow13')
        switch3 = self.addSwitch('s3', protocols='OpenFlow13')
        switch100 = self.addSwitch('s100', protocols='OpenFlow13')
        
        # Add host
        self.host0 = self.addHost('h0', mac='00:00:00:00:00:01', ip='10.0.0.1/24' )
        self.host1 = self.addHost('h1', mac='00:00:00:00:00:02', ip='10.0.0.2/24' )
        self.host2 = self.addHost('h2', mac='00:00:00:00:00:03', ip='10.0.0.3/24' )
        self.host3 = self.addHost('h3', mac='00:00:00:00:00:04', ip='10.0.0.4/24' )
        self.host100 = self.addHost('h100', mac='00:00:00:00:00:64', ip='10.0.0.101/24' )

        # Add link
        self.addLink(switch0, switch1)
        self.addLink(switch1, switch2)
        self.addLink(switch2, switch3)
        self.addLink(switch3, switch0)
        self.addLink(switch100, switch2)
        self.addLink(self.host0, switch0)
        self.addLink(self.host1, switch1)
        self.addLink(self.host2, switch2)
        self.addLink(self.host3, switch3)
        self.addLink(self.host100, switch100)
        
        # Python's range(N) generates 0..N-1
        # for h in range(n):
        #     host = self.addHost('h%s' % (h + 1))
        #     self.addLink(host, switch)

def simpleTest():
    topo = RingTopo()
    controller_ip = '127.0.0.1'
    net = Mininet(topo=topo, controller=lambda a: RemoteController(a, ip=controller_ip, port=6633), link=TCLink)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    sleep(5)
    net.pingAll()
    net.host0.cmd('python mininet/source/cache_algorithm/cache_color.py -i 0 &')
    net.host1.cmd('python mininet/source/cache_algorithm/cache_color.py -i 1 &')
    net.host2.cmd('python mininet/source/cache_algorithm/cache_color.py -i 2 &')
    net.host3.cmd('python mininet/source/cache_algorithm/cache_color.py -i 3 &')
    net.host100.cmd('python mininet/source/cache_algorithm/cache_color.py -i 100')
    sleep(2)
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()