#!/usr/bin/python                                                                            
                                                                                             
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController
from mininet.link import Link, TCLink
from mininet.cli import CLI 
from time import sleep
import os, os.path, argparse

# Parse cache number
parser = argparse.ArgumentParser(description="Cache Server")

parser.add_argument('--cachetype', '-c',
                    dest="cachetype",
                    type=int,
                    help="Type of cache: 0 -> No cache, 1 -> Original LFU, 2 -> Color-based Cache",
                    default=2)
# Export parameters
args = parser.parse_args()
cache_type = args.cachetype

cache_script = ("cache_no.py","cache_lfu.py","cache_color.py")

class RingTopo(Topo):
    def __init__(self, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)

        # Add switch
        switch0 = self.addSwitch('s0', protocols='OpenFlow13')
        switch1 = self.addSwitch('s1', protocols='OpenFlow13')
        switch2 = self.addSwitch('s2', protocols='OpenFlow13')
        switch3 = self.addSwitch('s3', protocols='OpenFlow13')
        switch4 = self.addSwitch('s4', protocols='OpenFlow13')
        switch5 = self.addSwitch('s5', protocols='OpenFlow13')
        switch6 = self.addSwitch('s6', protocols='OpenFlow13')
        switch7 = self.addSwitch('s7', protocols='OpenFlow13')
        switch8 = self.addSwitch('s8', protocols='OpenFlow13')
        switch9 = self.addSwitch('s9', protocols='OpenFlow13')
        switch10 = self.addSwitch('s10', protocols='OpenFlow13')
        switch11 = self.addSwitch('s11', protocols='OpenFlow13')
        switch12 = self.addSwitch('s12', protocols='OpenFlow13')
        switch13 = self.addSwitch('s13', protocols='OpenFlow13')
        switch14 = self.addSwitch('s14', protocols='OpenFlow13')
        switch15 = self.addSwitch('s15', protocols='OpenFlow13')
        switch16 = self.addSwitch('s16', protocols='OpenFlow13')
        switch17 = self.addSwitch('s17', protocols='OpenFlow13')
        switch18 = self.addSwitch('s18', protocols='OpenFlow13')
        switch19 = self.addSwitch('s19', protocols='OpenFlow13')
        switch20 = self.addSwitch('s20', protocols='OpenFlow13')
        switch21 = self.addSwitch('s21', protocols='OpenFlow13')
        switch22 = self.addSwitch('s22', protocols='OpenFlow13')
        switch23 = self.addSwitch('s23', protocols='OpenFlow13')
        switch24 = self.addSwitch('s24', protocols='OpenFlow13')
        switch25 = self.addSwitch('s25', protocols='OpenFlow13')
        switch26 = self.addSwitch('s26', protocols='OpenFlow13')
        switch27 = self.addSwitch('s27', protocols='OpenFlow13')
        switch28 = self.addSwitch('s28', protocols='OpenFlow13')
        switch29 = self.addSwitch('s29', protocols='OpenFlow13')
        switch30 = self.addSwitch('s30', protocols='OpenFlow13')
        switch31 = self.addSwitch('s31', protocols='OpenFlow13')
        switch32 = self.addSwitch('s32', protocols='OpenFlow13')
        switch33 = self.addSwitch('s33', protocols='OpenFlow13')
        switch34 = self.addSwitch('s34', protocols='OpenFlow13')
        switch35 = self.addSwitch('s35', protocols='OpenFlow13')
        switch36 = self.addSwitch('s36', protocols='OpenFlow13')
        switch37 = self.addSwitch('s37', protocols='OpenFlow13')
        switch38 = self.addSwitch('s38', protocols='OpenFlow13')
        switch39 = self.addSwitch('s39', protocols='OpenFlow13')
        switch40 = self.addSwitch('s40', protocols='OpenFlow13')
        switch41 = self.addSwitch('s41', protocols='OpenFlow13')
        switch42 = self.addSwitch('s42', protocols='OpenFlow13')
        switch43 = self.addSwitch('s43', protocols='OpenFlow13')
        switch44 = self.addSwitch('s44', protocols='OpenFlow13')
        switch45 = self.addSwitch('s45', protocols='OpenFlow13')
        switch46 = self.addSwitch('s46', protocols='OpenFlow13')
        switch47 = self.addSwitch('s47', protocols='OpenFlow13')
        switch48 = self.addSwitch('s48', protocols='OpenFlow13')
        switch49 = self.addSwitch('s49', protocols='OpenFlow13')
        switch51 = self.addSwitch('s51', protocols='OpenFlow13')
        switch52 = self.addSwitch('s52', protocols='OpenFlow13')
        switch56 = self.addSwitch('s56', protocols='OpenFlow13')
        switch60 = self.addSwitch('s60', protocols='OpenFlow13')
        switch64 = self.addSwitch('s64', protocols='OpenFlow13')
        
        # Add host
        host0 = self.addHost('h0', mac='00:00:00:00:00:01', ip='10.0.0.1/24' )
        host1 = self.addHost('h1', mac='00:00:00:00:00:02', ip='10.0.0.2/24' )
        host2 = self.addHost('h2', mac='00:00:00:00:00:03', ip='10.0.0.3/24' )
        host3 = self.addHost('h3', mac='00:00:00:00:00:04', ip='10.0.0.4/24' )
        host4 = self.addHost('h4', mac='00:00:00:00:00:05', ip='10.0.0.5/24' )
        host5 = self.addHost('h5', mac='00:00:00:00:00:06', ip='10.0.0.6/24' )
        host6 = self.addHost('h6', mac='00:00:00:00:00:07', ip='10.0.0.7/24' )
        host7 = self.addHost('h7', mac='00:00:00:00:00:08', ip='10.0.0.8/24' )
        host8 = self.addHost('h8', mac='00:00:00:00:00:09', ip='10.0.0.9/24' )
        host9 = self.addHost('h9', mac='00:00:00:00:00:10', ip='10.0.0.10/24' )
        host10 = self.addHost('h10', mac='00:00:00:00:00:11', ip='10.0.0.11/24' )
        host11 = self.addHost('h11', mac='00:00:00:00:00:12', ip='10.0.0.12/24' )
        host12 = self.addHost('h12', mac='00:00:00:00:00:13', ip='10.0.0.13/24' )
        host13 = self.addHost('h13', mac='00:00:00:00:00:14', ip='10.0.0.14/24' )
        host14 = self.addHost('h14', mac='00:00:00:00:00:15', ip='10.0.0.15/24' )
        host15 = self.addHost('h15', mac='00:00:00:00:00:16', ip='10.0.0.16/24' )
        host16 = self.addHost('h16', mac='00:00:00:00:00:17', ip='10.0.0.17/24' )
        host17 = self.addHost('h17', mac='00:00:00:00:00:18', ip='10.0.0.18/24' )
        host18 = self.addHost('h18', mac='00:00:00:00:00:19', ip='10.0.0.19/24' )
        host19 = self.addHost('h19', mac='00:00:00:00:00:20', ip='10.0.0.20/24' )
        host20 = self.addHost('h20', mac='00:00:00:00:00:21', ip='10.0.0.21/24' )
        host21 = self.addHost('h21', mac='00:00:00:00:00:22', ip='10.0.0.22/24' )
        host22 = self.addHost('h22', mac='00:00:00:00:00:23', ip='10.0.0.23/24' )
        host23 = self.addHost('h23', mac='00:00:00:00:00:24', ip='10.0.0.24/24' )
        host24 = self.addHost('h24', mac='00:00:00:00:00:25', ip='10.0.0.25/24' )
        host25 = self.addHost('h25', mac='00:00:00:00:00:26', ip='10.0.0.26/24' )
        host26 = self.addHost('h26', mac='00:00:00:00:00:27', ip='10.0.0.27/24' )
        host27 = self.addHost('h27', mac='00:00:00:00:00:28', ip='10.0.0.28/24' )
        host28 = self.addHost('h28', mac='00:00:00:00:00:29', ip='10.0.0.29/24' )
        host29 = self.addHost('h29', mac='00:00:00:00:00:30', ip='10.0.0.30/24' )
        host30 = self.addHost('h30', mac='00:00:00:00:00:31', ip='10.0.0.31/24' )
        host31 = self.addHost('h31', mac='00:00:00:00:00:32', ip='10.0.0.32/24' )
        host32 = self.addHost('h32', mac='00:00:00:00:00:33', ip='10.0.0.33/24' )
        host33 = self.addHost('h33', mac='00:00:00:00:00:34', ip='10.0.0.34/24' )
        host34 = self.addHost('h34', mac='00:00:00:00:00:35', ip='10.0.0.35/24' )
        host35 = self.addHost('h35', mac='00:00:00:00:00:36', ip='10.0.0.36/24' )
        host36 = self.addHost('h36', mac='00:00:00:00:00:37', ip='10.0.0.37/24' )
        host37 = self.addHost('h37', mac='00:00:00:00:00:38', ip='10.0.0.38/24' )
        host38 = self.addHost('h38', mac='00:00:00:00:00:39', ip='10.0.0.39/24' )
        host39 = self.addHost('h39', mac='00:00:00:00:00:40', ip='10.0.0.40/24' )
        host40 = self.addHost('h40', mac='00:00:00:00:00:41', ip='10.0.0.41/24' )
        host41 = self.addHost('h41', mac='00:00:00:00:00:42', ip='10.0.0.42/24' )
        host42 = self.addHost('h42', mac='00:00:00:00:00:43', ip='10.0.0.43/24' )
        host43 = self.addHost('h43', mac='00:00:00:00:00:44', ip='10.0.0.44/24' )
        host44 = self.addHost('h44', mac='00:00:00:00:00:45', ip='10.0.0.45/24' )
        host45 = self.addHost('h45', mac='00:00:00:00:00:46', ip='10.0.0.46/24' )
        host46 = self.addHost('h46', mac='00:00:00:00:00:47', ip='10.0.0.47/24' )
        host47 = self.addHost('h47', mac='00:00:00:00:00:48', ip='10.0.0.48/24' )
        host48 = self.addHost('h48', mac='00:00:00:00:00:49', ip='10.0.0.49/24' )
        host49 = self.addHost('h49', mac='00:00:00:00:00:50', ip='10.0.0.50/24' )
        host51 = self.addHost('h51', mac='00:00:00:00:00:52', ip='10.0.0.52/24' )
        host52 = self.addHost('h52', mac='00:00:00:00:00:53', ip='10.0.0.53/24' )
        host56 = self.addHost('h56', mac='00:00:00:00:00:57', ip='10.0.0.57/24' )
        host60 = self.addHost('h60', mac='00:00:00:00:00:61', ip='10.0.0.61/24' )
        host64 = self.addHost('h64', mac='00:00:00:00:00:65', ip='10.0.0.65/24' )

        # Add link
        self.addLink(switch0, switch3)
        self.addLink(switch4, switch2)
        self.addLink(switch2, switch3)
        self.addLink(switch8, switch2)
        self.addLink(switch3, switch5)
        self.addLink(switch3, switch12)
        self.addLink(switch1, switch12)
        self.addLink(switch7, switch1)
        self.addLink(switch9, switch12)
        self.addLink(switch1, switch6)
        self.addLink(switch5, switch10)
        self.addLink(switch9, switch11)
        self.addLink(switch6, switch16)
        self.addLink(switch13, switch15)
        self.addLink(switch15, switch16)
        self.addLink(switch10, switch19)
        self.addLink(switch11, switch14)
        self.addLink(switch15, switch18)
        self.addLink(switch14, switch17)
        self.addLink(switch19, switch20)
        self.addLink(switch18, switch20)
        self.addLink(switch17, switch20)
        self.addLink(switch18, switch21)
        self.addLink(switch21, switch20)
        self.addLink(switch20, switch25)
        self.addLink(switch27, switch21)
        self.addLink(switch25, switch23)
        self.addLink(switch25, switch22)
        self.addLink(switch23, switch24)
        self.addLink(switch26, switch27)
        self.addLink(switch32, switch27)
        self.addLink(switch26, switch24)
        self.addLink(switch28, switch22)
        self.addLink(switch29, switch24)
        self.addLink(switch29, switch26)
        self.addLink(switch33, switch32)
        self.addLink(switch28, switch31)
        self.addLink(switch36, switch29)
        self.addLink(switch33, switch35)
        self.addLink(switch35, switch36)
        self.addLink(switch37, switch31)
        self.addLink(switch30, switch36)
        self.addLink(switch40, switch35)
        self.addLink(switch30, switch37)
        self.addLink(switch48, switch37)
        self.addLink(switch30, switch39)
        self.addLink(switch34, switch40)
        self.addLink(switch44, switch39)
        self.addLink(switch44, switch34)
        self.addLink(switch41, switch44)
        self.addLink(switch34, switch41)
        self.addLink(switch41, switch48)
        self.addLink(switch48, switch51)
        self.addLink(switch38, switch48)
        self.addLink(switch43, switch41)
        self.addLink(switch52, switch38)
        self.addLink(switch43, switch52)
        self.addLink(switch38, switch47)
        self.addLink(switch56, switch43)
        self.addLink(switch45, switch47)
        self.addLink(switch45, switch56)
        self.addLink(switch56, switch42)
        self.addLink(switch45, switch60)
        self.addLink(switch60, switch42)
        self.addLink(switch51, switch60)
        self.addLink(switch51, switch42)
        self.addLink(switch64, switch42)
        self.addLink(switch51, switch49)
        self.addLink(switch64, switch46)
        self.addLink(switch49, switch46)

        self.addLink(host0, switch0)
        self.addLink(host1, switch1)
        self.addLink(host2, switch2)
        self.addLink(host3, switch3)
        self.addLink(host4, switch4)
        self.addLink(host5, switch5)
        self.addLink(host6, switch6)
        self.addLink(host7, switch7)
        self.addLink(host8, switch8)
        self.addLink(host9, switch9)
        self.addLink(host10, switch10)
        self.addLink(host11, switch11)
        self.addLink(host12, switch12)
        self.addLink(host13, switch13)
        self.addLink(host14, switch14)
        self.addLink(host15, switch15)
        self.addLink(host16, switch16)
        self.addLink(host17, switch17)
        self.addLink(host18, switch18)
        self.addLink(host19, switch19)
        self.addLink(host20, switch20)
        self.addLink(host21, switch21)
        self.addLink(host22, switch22)
        self.addLink(host23, switch23)
        self.addLink(host24, switch24)
        self.addLink(host25, switch25)
        self.addLink(host26, switch26)
        self.addLink(host27, switch27)
        self.addLink(host28, switch28)
        self.addLink(host29, switch29)
        self.addLink(host30, switch30)
        self.addLink(host31, switch31)
        self.addLink(host32, switch32)
        self.addLink(host33, switch33)
        self.addLink(host34, switch34)
        self.addLink(host35, switch35)
        self.addLink(host36, switch36)
        self.addLink(host37, switch37)
        self.addLink(host38, switch38)
        self.addLink(host39, switch39)
        self.addLink(host40, switch40)
        self.addLink(host41, switch41)
        self.addLink(host42, switch42)
        self.addLink(host43, switch43)
        self.addLink(host44, switch44)
        self.addLink(host45, switch45)
        self.addLink(host46, switch46)
        self.addLink(host47, switch47)
        self.addLink(host48, switch48)
        self.addLink(host49, switch49)
        self.addLink(host51, switch51)
        self.addLink(host52, switch52)
        self.addLink(host56, switch56)
        self.addLink(host60, switch60)
        self.addLink(host64, switch64)
        
        # Python's range(N) generates 0..N-1
        # for h in range(n):
        #     host = self.addHost('h%s' % (h + 1))
        #     self.addLink(host, switch)

def simpleTest():
    topo = RingTopo()
    controller_ip = '127.0.0.1'
    net = Mininet(topo=topo, controller=lambda a: RemoteController(a, ip=controller_ip, port=6633), link=TCLink)
    net.start()
    for host in net.hosts:
        for h in net.hosts:
            host.cmd("arp -s %s %s" % (h.IP(), h.MAC()))
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    #CLI(net)
    net.pingAll()
    net.pingAll()
    h0 = net.getNodeByName("h0")
    h1 = net.getNodeByName("h1")
    h2 = net.getNodeByName("h2")
    h3 = net.getNodeByName("h3")
    h4 = net.getNodeByName("h4")
    h5 = net.getNodeByName("h5")
    h6 = net.getNodeByName("h6")
    h7 = net.getNodeByName("h7")
    h8 = net.getNodeByName("h8")
    h9 = net.getNodeByName("h9")
    h10 = net.getNodeByName("h10")
    h11 = net.getNodeByName("h11")
    h12 = net.getNodeByName("h12")
    h13 = net.getNodeByName("h13")
    h14 = net.getNodeByName("h14")
    h15 = net.getNodeByName("h15")
    h16 = net.getNodeByName("h16")
    h17 = net.getNodeByName("h17")
    h18 = net.getNodeByName("h18")
    h19 = net.getNodeByName("h19")
    h20 = net.getNodeByName("h20")
    h21 = net.getNodeByName("h21")
    h22 = net.getNodeByName("h22")
    h23 = net.getNodeByName("h23")
    h24 = net.getNodeByName("h24")
    h25 = net.getNodeByName("h25")
    h26 = net.getNodeByName("h26")
    h27 = net.getNodeByName("h27")
    h28 = net.getNodeByName("h28")
    h29 = net.getNodeByName("h29")
    h30 = net.getNodeByName("h30")
    h31 = net.getNodeByName("h31")
    h32 = net.getNodeByName("h32")
    h33 = net.getNodeByName("h33")
    h34 = net.getNodeByName("h34")
    h35 = net.getNodeByName("h35")
    h36 = net.getNodeByName("h36")
    h37 = net.getNodeByName("h37")
    h38 = net.getNodeByName("h38")
    h39 = net.getNodeByName("h39")
    h40 = net.getNodeByName("h40")
    h41 = net.getNodeByName("h41")
    h42 = net.getNodeByName("h42")
    h43 = net.getNodeByName("h43")
    h44 = net.getNodeByName("h44")
    h45 = net.getNodeByName("h45")
    h46 = net.getNodeByName("h46")
    h47 = net.getNodeByName("h47")
    h48 = net.getNodeByName("h48")
    h49 = net.getNodeByName("h49")
    h51 = net.getNodeByName("h51")
    h52 = net.getNodeByName("h52")
    h56 = net.getNodeByName("h56")
    h60 = net.getNodeByName("h60")
    h64 = net.getNodeByName("h64")

    h0.cmd('python mininet/source/cache_algorithm/{} -i 0 >>/home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_0.txt &'.format(cache_script[cache_type]))
    h1.cmd('python mininet/source/cache_algorithm/{} -i 1 >>/home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_1.txt &'.format(cache_script[cache_type]))
    h2.cmd('python mininet/source/cache_algorithm/{} -i 2 >>/home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_2.txt &'.format(cache_script[cache_type]))
    h3.cmd('python mininet/source/cache_algorithm/{} -i 3 >>/home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_3.txt &'.format(cache_script[cache_type]))
    h4.cmd('python mininet/source/cache_algorithm/{} -i 4 >>/home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_4.txt &'.format(cache_script[cache_type]))
    h5.cmd('python mininet/source/cache_algorithm/{} -i 5 >>/home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_5.txt &'.format(cache_script[cache_type]))
    h6.cmd('python mininet/source/cache_algorithm/{} -i 6 >>/home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_6.txt &'.format(cache_script[cache_type]))
    h7.cmd('python mininet/source/cache_algorithm/{} -i 7 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_7.txt &'.format(cache_script[cache_type]))
    h8.cmd('python mininet/source/cache_algorithm/{} -i 8 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_8.txt &'.format(cache_script[cache_type]))
    h9.cmd('python mininet/source/cache_algorithm/{} -i 9 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_9.txt &'.format(cache_script[cache_type]))
    h10.cmd('python mininet/source/cache_algorithm/{} -i 10 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_10.txt &'.format(cache_script[cache_type]))
    h11.cmd('python mininet/source/cache_algorithm/{} -i 11 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_11.txt &'.format(cache_script[cache_type]))
    h12.cmd('python mininet/source/cache_algorithm/{} -i 12 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_12.txt &'.format(cache_script[cache_type]))
    h13.cmd('python mininet/source/cache_algorithm/{} -i 13 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_13.txt &'.format(cache_script[cache_type]))
    h14.cmd('python mininet/source/cache_algorithm/{} -i 14 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_14.txt &'.format(cache_script[cache_type]))
    h15.cmd('python mininet/source/cache_algorithm/{} -i 15 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_15.txt &'.format(cache_script[cache_type]))
    h16.cmd('python mininet/source/cache_algorithm/{} -i 16 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_16.txt &'.format(cache_script[cache_type]))
    h17.cmd('python mininet/source/cache_algorithm/{} -i 17 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_17.txt &'.format(cache_script[cache_type]))
    h18.cmd('python mininet/source/cache_algorithm/{} -i 18 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_18.txt &'.format(cache_script[cache_type]))
    h19.cmd('python mininet/source/cache_algorithm/{} -i 19 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_19.txt &'.format(cache_script[cache_type]))
    h20.cmd('python mininet/source/cache_algorithm/{} -i 20 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_20.txt &'.format(cache_script[cache_type]))
    h21.cmd('python mininet/source/cache_algorithm/{} -i 21 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_21.txt &'.format(cache_script[cache_type]))
    h22.cmd('python mininet/source/cache_algorithm/{} -i 22 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_22.txt &'.format(cache_script[cache_type]))
    h23.cmd('python mininet/source/cache_algorithm/{} -i 23 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_23.txt &'.format(cache_script[cache_type]))
    h24.cmd('python mininet/source/cache_algorithm/{} -i 24 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_24.txt &'.format(cache_script[cache_type]))
    h25.cmd('python mininet/source/cache_algorithm/{} -i 25 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_25.txt &'.format(cache_script[cache_type]))
    h26.cmd('python mininet/source/cache_algorithm/{} -i 26 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_26.txt &'.format(cache_script[cache_type]))
    h27.cmd('python mininet/source/cache_algorithm/{} -i 27 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_27.txt &'.format(cache_script[cache_type]))
    h28.cmd('python mininet/source/cache_algorithm/{} -i 28 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_28.txt &'.format(cache_script[cache_type]))
    h29.cmd('python mininet/source/cache_algorithm/{} -i 29 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_29.txt &'.format(cache_script[cache_type]))
    h30.cmd('python mininet/source/cache_algorithm/{} -i 30 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_30.txt &'.format(cache_script[cache_type]))
    h31.cmd('python mininet/source/cache_algorithm/{} -i 31 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_31.txt &'.format(cache_script[cache_type]))
    h32.cmd('python mininet/source/cache_algorithm/{} -i 32 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_32.txt &'.format(cache_script[cache_type]))
    h33.cmd('python mininet/source/cache_algorithm/{} -i 33 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_33.txt &'.format(cache_script[cache_type]))
    h34.cmd('python mininet/source/cache_algorithm/{} -i 34 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_34.txt &'.format(cache_script[cache_type]))
    h35.cmd('python mininet/source/cache_algorithm/{} -i 35 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_35.txt &'.format(cache_script[cache_type]))
    h36.cmd('python mininet/source/cache_algorithm/{} -i 36 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_36.txt &'.format(cache_script[cache_type]))
    h37.cmd('python mininet/source/cache_algorithm/{} -i 37 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_37.txt &'.format(cache_script[cache_type]))
    h38.cmd('python mininet/source/cache_algorithm/{} -i 38 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_38.txt &'.format(cache_script[cache_type]))
    h39.cmd('python mininet/source/cache_algorithm/{} -i 39 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_39.txt &'.format(cache_script[cache_type]))
    h40.cmd('python mininet/source/cache_algorithm/{} -i 40 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_40.txt &'.format(cache_script[cache_type]))
    h41.cmd('python mininet/source/cache_algorithm/{} -i 41 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_41.txt &'.format(cache_script[cache_type]))
    h42.cmd('python mininet/source/cache_algorithm/{} -i 42 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_42.txt &'.format(cache_script[cache_type]))
    h43.cmd('python mininet/source/cache_algorithm/{} -i 43 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_43.txt &'.format(cache_script[cache_type]))
    h44.cmd('python mininet/source/cache_algorithm/{} -i 44 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_44.txt &'.format(cache_script[cache_type]))
    h45.cmd('python mininet/source/cache_algorithm/{} -i 45 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_45.txt &'.format(cache_script[cache_type]))
    h46.cmd('python mininet/source/cache_algorithm/{} -i 46 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_46.txt &'.format(cache_script[cache_type]))
    h47.cmd('python mininet/source/cache_algorithm/{} -i 47 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_47.txt &'.format(cache_script[cache_type]))
    h48.cmd('python mininet/source/cache_algorithm/{} -i 48 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_48.txt &'.format(cache_script[cache_type]))
    h49.cmd('python mininet/source/cache_algorithm/{} -i 49 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_49.txt &'.format(cache_script[cache_type]))
    h51.cmd('python mininet/source/cache_algorithm/{} -i 51 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_51.txt &'.format(cache_script[cache_type]))
    h52.cmd('python mininet/source/cache_algorithm/{} -i 52 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_52.txt &'.format(cache_script[cache_type]))
    h56.cmd('python mininet/source/cache_algorithm/{} -i 56 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_56.txt &'.format(cache_script[cache_type]))
    h60.cmd('python mininet/source/cache_algorithm/{} -i 60 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_60.txt &'.format(cache_script[cache_type]))
    h64.cmd('python mininet/source/cache_algorithm/{} -i 64 >> /home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/log/log_console_64.txt &'.format(cache_script[cache_type]))
    
    DIR = '/home/hpcc/workspace/telco_cdn_mininet/mininet/source/cache_algorithm/result'
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    timer = 0
    while True:
        numfile = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        if (numfile >= 54):
            print("All servers are finished: {}".format(numfile))
            break
        print("Number of servers are finished: {} after {} seconds".format(numfile, timer))
        timer += 1
        sleep(1)
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()