#!/usr/bin/python

"""
Custom topology for Mininet, generated by GraphML-Topo-to-Mininet-Network-Generator.
"""
import argparse
import os
import random
from multiprocessing import Process

from MaxiNet.Frontend import maxinet
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.node import Node
from mininet.node import OVSKernelSwitch
from mininet.node import OVSSwitch
from mininet.topo import Topo
from ryu.lib import dpid as dpid_lib

from utils.monitor import *

parser = argparse.ArgumentParser(description="Hedera tests")

parser.add_argument('--dir', '-d',
                    help="Directory to store outputs",
                    default="results")

parser.add_argument('--time', '-t',
                    dest="time",
                    type=int,
                    help="Duration of the experiment.",
                    default=60)

parser.add_argument('--hosts',
                    dest="nhosts",
                    type=int,
                    help="Number of hosts per switch.",
                    default=10)

parser.add_argument('--iperf',
                    dest="iperf",
                    help="Path to custom iperf",
                    default="iperf")

parser.add_argument('--traffic',
                    dest="traffic",
                    help="Traffic matrix to simulate",
                    default="random")

parser.add_argument('--flowsPerHost', '-n',
                    dest="fph",
                    type=int,
                    help="Only use this parameter with random traffic pattern",
                    default=5)

parser.add_argument('--Controller', '-ctl',
                    dest="controller",
                    help="Controller's IP",
                    default='127.0.0.1')

# Export parameters
args = parser.parse_args()
IPERF_PATH = args.iperf
CONTROLLER_IP = args.controller
nhosts = args.nhosts


class GeneratedTopo(Topo):
    "Internet Topology Zoo Specimen."

    def __init__(self, hps, sw_ip_fname, **opts):
        "Create a topology."

        # Initialize Topology
        Topo.__init__(self, **opts)
        self.nHosts = 1
        self.sw_ip = {}

        self.get_ip_based(fname=sw_ip_fname)

        # add nodes, switches first...
        NY54 = self.addSwitch('s1', cls=OVSKernelSwitch)
        CMBR = self.addSwitch('s2', cls=OVSKernelSwitch)
        CHCG = self.addSwitch('s3', cls=OVSKernelSwitch)
        CLEV = self.addSwitch('s4', cls=OVSKernelSwitch)
        RLGH = self.addSwitch('s5', cls=OVSKernelSwitch)
        ATLN = self.addSwitch('s6', cls=OVSKernelSwitch)
        PHLA = self.addSwitch('s7', cls=OVSKernelSwitch)
        WASH = self.addSwitch('s8', cls=OVSKernelSwitch)
        NSVL = self.addSwitch('s9', cls=OVSKernelSwitch)
        STLS = self.addSwitch('s10', cls=OVSKernelSwitch)
        NWOR = self.addSwitch('s11', cls=OVSKernelSwitch)
        HSTN = self.addSwitch('s12', cls=OVSKernelSwitch)
        SNAN = self.addSwitch('s13', cls=OVSKernelSwitch)
        DLLS = self.addSwitch('s14', cls=OVSKernelSwitch)
        ORLD = self.addSwitch('s15', cls=OVSKernelSwitch)
        DNVR = self.addSwitch('s16', cls=OVSKernelSwitch)
        KSCY = self.addSwitch('s17', cls=OVSKernelSwitch)
        SNFN = self.addSwitch('s18', cls=OVSKernelSwitch)
        SCRM = self.addSwitch('s19', cls=OVSKernelSwitch)
        PTLD = self.addSwitch('s20', cls=OVSKernelSwitch)
        STTL = self.addSwitch('s21', cls=OVSKernelSwitch)
        SLKC = self.addSwitch('s22', cls=OVSKernelSwitch)
        LA03 = self.addSwitch('s23', cls=OVSKernelSwitch)
        SNDG = self.addSwitch('s24', cls=OVSKernelSwitch)
        PHNX = self.addSwitch('s25', cls=OVSKernelSwitch)

        # ... and now hosts
        self.add_hosts(sw=NY54, nHosts=hps, sw_idx=1, sw_name='NY54')
        self.add_hosts(sw=CMBR, nHosts=hps, sw_idx=2, sw_name='CMBR')
        self.add_hosts(sw=CHCG, nHosts=hps, sw_idx=3, sw_name='CHCG')
        self.add_hosts(sw=CLEV, nHosts=hps, sw_idx=4, sw_name='CLEV')
        self.add_hosts(sw=RLGH, nHosts=hps, sw_idx=5, sw_name='RLGH')
        self.add_hosts(sw=ATLN, nHosts=hps, sw_idx=6, sw_name='ATLN')
        self.add_hosts(sw=PHLA, nHosts=hps, sw_idx=7, sw_name='PHLA')
        self.add_hosts(sw=WASH, nHosts=hps, sw_idx=8, sw_name='WASH')
        self.add_hosts(sw=NSVL, nHosts=hps, sw_idx=9, sw_name='NSVL')
        self.add_hosts(sw=STLS, nHosts=hps, sw_idx=10, sw_name='STLS')
        self.add_hosts(sw=NWOR, nHosts=hps, sw_idx=11, sw_name='NWOR')
        self.add_hosts(sw=HSTN, nHosts=hps, sw_idx=12, sw_name='HSTN')
        self.add_hosts(sw=SNAN, nHosts=hps, sw_idx=13, sw_name='SNAN')
        self.add_hosts(sw=DLLS, nHosts=hps, sw_idx=14, sw_name='DLLS')
        self.add_hosts(sw=ORLD, nHosts=hps, sw_idx=15, sw_name='ORLD')
        self.add_hosts(sw=DNVR, nHosts=hps, sw_idx=16, sw_name='DNVR')
        self.add_hosts(sw=KSCY, nHosts=hps, sw_idx=17, sw_name='KSCY')
        self.add_hosts(sw=SNFN, nHosts=hps, sw_idx=18, sw_name='SNFN')
        self.add_hosts(sw=SCRM, nHosts=hps, sw_idx=19, sw_name='SCRM')
        self.add_hosts(sw=PTLD, nHosts=hps, sw_idx=20, sw_name='PTLD')
        self.add_hosts(sw=STTL, nHosts=hps, sw_idx=21, sw_name='STTL')
        self.add_hosts(sw=SLKC, nHosts=hps, sw_idx=22, sw_name='SLKC')
        self.add_hosts(sw=LA03, nHosts=hps, sw_idx=23, sw_name='LA03')
        self.add_hosts(sw=SNDG, nHosts=hps, sw_idx=24, sw_name='SNDG')
        self.add_hosts(sw=PHNX, nHosts=hps, sw_idx=25, sw_name='PHNX')

        # add edges between switch and corresponding host

        # add edges between switches
        self.addLink(NY54, CMBR, bw=1000, delay='0.979030824185ms')
        self.addLink(NY54, CHCG, bw=1000, delay='0.806374975652ms')
        self.addLink(NY54, PHLA, bw=1000, delay='0.686192970166ms')
        self.addLink(NY54, WASH, bw=1000, delay='0.605826192092ms')
        self.addLink(CMBR, PHLA, bw=1000, delay='1.4018238197ms')
        self.addLink(CHCG, CLEV, bw=1000, delay='0.232315346482ms')
        self.addLink(CHCG, PHLA, bw=1000, delay='1.07297714274ms')
        self.addLink(CHCG, STLS, bw=1000, delay='1.12827896944ms')
        self.addLink(CHCG, DNVR, bw=1000, delay='1.35964770335ms')
        self.addLink(CHCG, KSCY, bw=1000, delay='1.5199778541ms')
        self.addLink(CHCG, SNFN, bw=1000, delay='0.620743405435ms')
        self.addLink(CHCG, STTL, bw=1000, delay='0.93027212534ms')
        self.addLink(CHCG, SLKC, bw=1000, delay='0.735621751348ms')
        self.addLink(CLEV, NSVL, bw=1000, delay='0.523419372248ms')
        self.addLink(CLEV, STLS, bw=1000, delay='1.00360290845ms')
        self.addLink(CLEV, PHLA, bw=1000, delay='0.882912133249ms')
        self.addLink(RLGH, ATLN, bw=1000, delay='1.1644489729ms')
        self.addLink(RLGH, WASH, bw=1000, delay='1.48176810502ms')
        self.addLink(ATLN, WASH, bw=1000, delay='0.557636936322ms')
        self.addLink(ATLN, NSVL, bw=1000, delay='1.32869749865ms')
        self.addLink(ATLN, STLS, bw=1000, delay='0.767705554748ms')
        self.addLink(ATLN, DLLS, bw=1000, delay='0.544782086448ms')
        self.addLink(ATLN, ORLD, bw=1000, delay='1.46119152532ms')
        self.addLink(PHLA, WASH, bw=1000, delay='0.372209320106ms')
        self.addLink(NSVL, STLS, bw=1000, delay='1.43250491305ms')
        self.addLink(NSVL, DLLS, bw=1000, delay='1.67698215288ms')
        self.addLink(STLS, DLLS, bw=1000, delay='0.256389964194ms')
        self.addLink(STLS, KSCY, bw=1000, delay='0.395511571791ms')
        self.addLink(STLS, LA03, bw=1000, delay='0.257085227363ms')
        self.addLink(NWOR, HSTN, bw=1000, delay='0.0952906633914ms')
        self.addLink(NWOR, DLLS, bw=1000, delay='1.60231329739ms')
        self.addLink(NWOR, ORLD, bw=1000, delay='0.692731063896ms')
        self.addLink(HSTN, SNAN, bw=1000, delay='0.284150653798ms')
        self.addLink(HSTN, DLLS, bw=1000, delay='1.65690128332ms')
        self.addLink(HSTN, ORLD, bw=1000, delay='0.731886304782ms')
        self.addLink(SNAN, PHNX, bw=1000, delay='1.34258627257ms')
        self.addLink(SNAN, DLLS, bw=1000, delay='1.50063532341ms')
        self.addLink(DLLS, DNVR, bw=1000, delay='0.251471593235ms')
        self.addLink(DLLS, KSCY, bw=1000, delay='0.18026026737ms')
        self.addLink(DLLS, SNFN, bw=1000, delay='0.74304274592ms')
        self.addLink(DLLS, LA03, bw=1000, delay='0.506439293357ms')
        self.addLink(DNVR, KSCY, bw=1000, delay='0.223328790403ms')
        self.addLink(DNVR, SNFN, bw=1000, delay='0.889017541903ms')
        self.addLink(DNVR, SLKC, bw=1000, delay='0.631898982721ms')
        self.addLink(KSCY, SNFN, bw=1000, delay='0.922778522233ms')
        self.addLink(SNFN, SCRM, bw=1000, delay='0.630352278097ms')
        self.addLink(SNFN, PTLD, bw=1000, delay='0.828572513655ms')
        self.addLink(SNFN, STTL, bw=1000, delay='1.54076081649ms')
        self.addLink(SNFN, SLKC, bw=1000, delay='0.621507502625ms')
        self.addLink(SNFN, LA03, bw=1000, delay='0.602936230151ms')
        self.addLink(SCRM, SLKC, bw=1000, delay='0.461350343644ms')
        self.addLink(PTLD, STTL, bw=1000, delay='1.17591515181ms')
        self.addLink(SLKC, LA03, bw=1000, delay='0.243225267023ms')
        self.addLink(LA03, SNDG, bw=1000, delay='0.681264950821ms')
        self.addLink(LA03, PHNX, bw=1000, delay='0.343709457969ms')
        self.addLink(SNDG, PHNX, bw=1000, delay='0.345064487693ms')

    def add_hosts(self, sw, nHosts, sw_idx, sw_name):

        for h in range(1, nHosts + 1):
            host_name = 'h%ds%d' % (h, sw_idx)
            ip_based = self.sw_ip[sw_name]
            de_ip_based = ip_based.split('.')

            host_ip = de_ip_based[0] + '.' + de_ip_based[1] + '.' + str(h) + '.2/24'
            defaultRoute = 'via ' + de_ip_based[0] + '.' + de_ip_based[1] + '.' + str(h) + '.1'

            h = self.addHost(host_name, ip=host_ip, defaultRoute=defaultRoute)
            self.addLink(h, sw, bw=100, delay='0.1ms')

            self.nHosts += 1

    def get_ip_based(self, fname):
        with open(fname, 'r') as f:
            for line in f:
                sw_name, ip_based = line.split(' ')
                self.sw_ip[sw_name] = ip_based


# HERE THE CODE DEFINITION OF THE TOPOLOGY ENDS

# the following code produces an executable script working with a remote controller
# and providing ssh access to the the mininet hosts from within the ubuntu vm
controller_ip = ''


def setupNetwork(hps, sw_ip_fname):
    topo = GeneratedTopo(hps=hps, sw_ip_fname=sw_ip_fname)
    print('*** Setup Maxinet Cluster')

    cluster = maxinet.Cluster()

    exp = maxinet.Experiment(cluster, topo, switch=OVSSwitch)
    exp.setup()

    print('*** Done setup Maxinet Cluster')

    return exp


def connectToRootNS(network, switch, ip, prefixLen, routes):
    "Connect hosts to root namespace via switch. Starts network."
    "network: Mininet() network object"
    "switch: switch to connect to root namespace"
    "ip: IP address for root namespace node"
    "prefixLen: IP address prefix length (e.g. 8, 16, 24)"
    "routes: host networks to route to"
    # Create a node in root namespace and link to switch 0
    root = Node('root', inNamespace=False)
    intf = TCLink(root, switch).intf1
    root.setIP(ip, prefixLen, intf)
    # Start network that now includes link to root namespace
    network.start()
    # Add routes from root ns to hosts
    for route in routes:
        root.cmd('route add -net ' + route + ' dev ' + str(intf))


def get_host_name(index, hps):
    sw_id = int(index / hps) + 1
    return 'h%ds%d' % (index % hps + 1, sw_id)


def compute_random(nHosts):
    matrix = []
    for ind in range(nHosts):
        dst = random.randint(0, nHosts - 1)
        while dst == ind:
            dst = random.randint(0, nHosts - 1)
        matrix.append(dst)
    return matrix


def compute_randbij(nHosts):
    matrix = range(0, nHosts)
    random.shuffle(matrix)
    return matrix


def addMatrixToFlow(flowToCreate, matrix):
    for i in range(len(matrix)):
        flowToCreate.append((i, matrix[i]))


def wait_listening(client, server, tcp_port):
    "Wait until server is listening on port"
    if not 'telnet' in client.cmd('which telnet'):
        raise Exception('Could not find telnet')
    cmd = ('sh -c "echo A | telnet -e A %s %s"' % (server.IP(), tcp_port))
    while 'Connected' not in client.cmd(cmd):
        print '|--- Wait for the tcp port listening on', server
        sleep(.5)


def start_tcpprobe():
    os.system("rmmod tcp_probe 1>/dev/null 2>&1; modprobe tcp_probe")
    Popen("cat /proc/net/tcpprobe >/dev/null", shell=True)


def stop_tcpprobe():
    os.system("killall -9 cat; rmmod tcp_probe 1>/dev/null 2>&1")


def run_expt(maxinet_exp, flowsToCreate, hps):
    "Run experiment"

    seconds = args.time

    tcp_port = 5001

    udp_port = 5002

    # Start receivers
    dstSet = set([p[1] for p in flowsToCreate])
    for dest_index in dstSet:
        dest_host_name = get_host_name(dest_index, hps)
        dst_node = maxinet_exp.get_node(dest_host_name)

        dst_node.cmd('%s -s -p %s > /dev/null &' % (IPERF_PATH, tcp_port))
        dst_node.cmd('%s -s -u -p %s > /dev/null &' % (IPERF_PATH, udp_port))

    for src_index, dest_index in flowsToCreate:

        src_name = get_host_name(src_index, hps)
        dst_name = get_host_name(dest_index, hps)

        src_node = maxinet_exp.get_node(src_name)
        dst_node = maxinet_exp.get_node(dst_name)

        if not 'telnet' in src_node.cmd('which telnet'):
            raise Exception('Could not find telnet')
        cmd = ('sh -c "echo A | telnet -e A %s %s"' % (dst_node.IP(), tcp_port))

        i = 0

        while 'Connected' not in src_node.cmd(cmd):
            print '|--- Wait for the tcp port listening on %s' % dst_name
            sleep(.5)
            i+=1
            if i > 2:
                break

        if i > 2:
            print('Cannt connect to host %s from %s' %(dst_name, src_name))
            print src_node.cmd('ping -c 200 %s' % dst_node.IP())
        else:
            print('Host %s is on' % dst_name)

    print "Listeners waiting"

    # Start the bandwidth and cwnd monitors in t1he background
    # monitor = Process(target=monitor_devs_ng, args=('%s/bwm.txt' % args.dir, 1.0))
    # monitor.start()
    #
    # start_tcpprobe()

    # Start the senders
    for src_index, dest_index in flowsToCreate:

        if random.uniform(0, 1) < 0.7:
            #  Send udp flow
            flow_time = random.randint(1, 5)
            maxinet_exp.get(get_host_name(src_index, hps)).cmd('%s -c %s -p %s -t %d -i 1 -ycu > /dev/null &' %
                                                               (IPERF_PATH,
                                                                maxinet_exp.get(get_host_name(dest_index, hps)).IP(),
                                                                udp_port,
                                                                flow_time))
        else:
            flow_time = random.randint(10, seconds)
            maxinet_exp.get(get_host_name(src_index, hps)).cmd('%s -c %s -p %s -t %d -i 1 -yc > /dev/null &' %
                                                               (IPERF_PATH,
                                                                maxinet_exp.get(get_host_name(dest_index, hps)).IP(),
                                                                tcp_port,
                                                                flow_time))

    print "Senders sending"

    for i in range(seconds):
        print "%d s elapsed" % i
        sleep(1)

    print "Ending experiment"
    os.system('killall -9 ' + IPERF_PATH)

    # Shut down monitors
    print "Waiting for monitor to stop"
    # monitor.terminate()
    # os.system('killall -9 bwm-ng')
    # stop_tcpprobe()


def start_controller(controller):
    cmd = 'sudo ryu-manager --observe-links %s' % controller

    Popen(cmd, shell=True)

    print('*** Waiting for starting Ryu Controllers')
    sleep(10)


def start_network(exp, fname, nHps):
    # start_controller(controller)
    try:
        print('*** Network start')
        sleep(5)
        set_default_gw(fname, nHps)
        # CLI(network)

        nHosts = len(exp.hosts)

        print('|--- Number of hosts: %d' % nHosts)

        flowsToCreate = []
        for fcount in range(args.fph):
            if args.traffic.startswith('random'):
                matrix = compute_random(nHosts=nHosts)
            elif args.traffic.startswith('randbij'):
                matrix = compute_randbij(nHosts=nHosts)
            else:
                raise Exception('Unrecognized traffic type')
            print "Running with matrix", matrix
            addMatrixToFlow(flowsToCreate, matrix)

        # src_list = []
        # dst_list = []
        # port_list = []
        # for _ in range(1, 30):
        #
        #     p = random.randint(15000, 16000)
        #     while p in port_list:
        #         p = random.randint(15000, 16000)
        #     port_list.append(p)
        #
        #     i = random.randint(0, nHosts - 1)
        #     while i in src_list:
        #         i = random.randint(0, nHosts - 1)
        #     src_list.append(i)
        #
        #     j = random.randint(0, nHosts - 1)
        #     while j in dst_list:
        #         j = random.randint(0, nHosts - 1)
        #
        #     dst_list.append(j)
        #     if i == j:
        #         continue
        #     src = exp.get_node(get_host_name(i, nHps))
        #
        #     dst = exp.get_node(get_host_name(j, nHps))
        #
        #     if src is None or dst is None:
        #         print('Can not get src %d of dst %d' % (i, j))
        #         continue
        #     dst.cmd('ITGLog >> /dev/null &')
        #     dst.cmd('ITGRecv -l /home/anle/itg_recv_log_%s &' % (dst.IP()))
        #     sleep(2)
        #
        #     print('start ITG from %s to %s' % (src.IP(), dst.IP()))
        #     src.cmd('ITGLog >> /dev/null &')
        #     src.cmd('ITGSend -l /home/anle/itg_sender_log_%s-%s -O 1000 -t 50000 -rp %d -a %s &' %
        #             (src.IP(), dst.IP(), p, dst.IP()))

        # for src_index, dest_index in flowsToCreate:
        #
        #     if random.uniform(0, 1) < 0.7:
        #         #  Send udp flow
        #
        #         src_name = get_host_name(src_index, nHps)
        #         src_node = exp.get_node(src_name)
        #
        #         dst_name = get_host_name(dest_index, nHps)
        #         dst_node = exp.get_node(dst_name)
        #
        #         print src_node.cmd('ping -c 100 %s > /home/anle/ping_from_%s_to_%s &' %
        #                      (dst_node.IP(), src_name, dst_name))
        #         sleep(2)

        # print('sleep 50')
        # sleep(50)
        # run_expt(maxinet_exp=exp, flowsToCreate=flowsToCreate, hps=nHps)

        src_index = 1
        src_node = exp.get_node(get_host_name(src_index, nHps))
        src_name = get_host_name(src_index, hps)

        tcp_port = 5001
        for _ in range(2, 50):
            dst_index = random.randint(2, nHosts-1)


            dst_name = get_host_name(dst_index, hps)

            dst_node = exp.get_node(dst_name)
            dst_node.cmd('%s -s -p %s > /dev/null &' % (IPERF_PATH, tcp_port))
            if not 'telnet' in src_node.cmd('which telnet'):
                raise Exception('Could not find telnet')
            cmd = ('sh -c "echo A | telnet -e A %s %s"' % (dst_node.IP(), tcp_port))

            i = 0

            while 'Connected' not in src_node.cmd(cmd):
                print '|--- Wait for the tcp port listening on %s' % dst_name
                sleep(.5)
                i += 1
                if i > 2:
                    break

            if i > 2:
                print('Cannt connect to host %s from %s' % (dst_name, src_name))
            else:
                print('Host %s is on' % dst_name)

        sleep(10)

        exp.stop()
    finally:
        exp.stop()
        print('*** Stop maxinet')


def set_default_gw(fname, nHps):
    with open(fname, 'r') as f:

        sw_dpid = 1

        for line in f:
            sw, ip_based = line.split(' ')

            de_ip_based = ip_based.split('.')
            for h in range(1, nHps + 1):
                defaultRoute = de_ip_based[0] + '.' + de_ip_based[1] + '.' + str(h) + '.1'

                rest_cmd = 'curl -X POST -d ' + '\'{"address":"%s/24"}\'' % defaultRoute + ' http://%s:8080/router/%s' % (
                    CONTROLLER_IP, dpid_lib.dpid_to_str(sw_dpid))

                print(rest_cmd)

                Popen(rest_cmd, shell=True)
                sleep(0.5)

            sw_dpid += 1


if __name__ == '__main__':
    setLogLevel('info')
    # setLogLevel('debug')
    hps = nhosts

    sw_ip_based_fname = 'topo_graphml/Att_IP_list'

    maxinet_exp = setupNetwork(hps, sw_ip_fname=sw_ip_based_fname)

    try:
        start_network(exp=maxinet_exp, fname=sw_ip_based_fname, nHps=hps)
    except KeyboardInterrupt:
        maxinet_exp.stop()
