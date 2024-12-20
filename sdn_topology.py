#!/usr/bin/env python

from mininet.net import Mininet
from mininet.topo import Topo
# from mininet.node import Controller, RemoteController, OVSController
# from mininet.node import CPULimitedHost, Host, Node
# from mininet.node import OVSKernelSwitch, UserSwitch
# from mininet.node import IVSSwitch
# from mininet.cli import CLI
# from mininet.log import setLogLevel, info
# from mininet.link import TCLink, Intf
# from subprocess import call

class Project ( Topo ):
    def __init__( net ):
        Topo.__init__( net )

        print( '*** Add switches\n')
        s1 = net.addSwitch('s1')
        s2 = net.addSwitch('s2')
        s3 = net.addSwitch('s3')
        
        print( '*** Add hosts\n')
        h1 = net.addHost('h1')
        h2 = net.addHost('h2')
        h3 = net.addHost('h3')
        h4 = net.addHost('h4')
        h5 = net.addHost('h5')
        h6 = net.addHost('h6')
        h7 = net.addHost('h7')
        h8 = net.addHost('h8')
        h9 = net.addHost('h9')
        h10 = net.addHost('h10')
        h11 = net.addHost('h11')
        h12 = net.addHost('h12')
        h13 = net.addHost('h13')
        h14 = net.addHost('h14')
        h15 = net.addHost('h15')
        h16 = net.addHost('h16')
        h17 = net.addHost('h17')
        h18 = net.addHost('h18')
        h19 = net.addHost('h19')
        h20 = net.addHost('h20')
        
        print( '*** Add links\n')
        net.addLink(s1, h1, bw=1)
        net.addLink(s1, h2, bw=1)
        net.addLink(s1, h3, bw=1)
        net.addLink(s1, h4, bw=1)
        net.addLink(s1, h5, bw=1)
        net.addLink(s1, h6, bw=1)
        net.addLink(s1, h7, bw=1)
        net.addLink(s2, h8, bw=1)
        net.addLink(s2, h9, bw=1)
        net.addLink(s2, h10, bw=1)
        net.addLink(s2, h11, bw=1)
        net.addLink(s2, h12, bw=1)
        net.addLink(s2, h13, bw=1)
        net.addLink(s2, h14, bw=1)
        net.addLink(s3, h15, bw=1)
        net.addLink(s3, h16, bw=1)
        net.addLink(s3, h17, bw=1)
        net.addLink(s3, h18, bw=1)
        net.addLink(s3, h20, bw=1)
        net.addLink(s3, h19, bw=1)
        net.addLink(s1, s2, bw=1)
        net.addLink(s2, s3, bw=1)
        net.addLink(s1, s3, bw=1)
        
        print('*** Post configure switches and hosts\n')

topos = {'project': (lambda: Project())}
