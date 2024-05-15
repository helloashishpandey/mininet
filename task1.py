from mininet.node import Controller, OVSKernelAP
from mininet.log import setLogLevel
from mininet.wifi.cli import CLI_wifi
from mininet.wifi.net import Mininet_wifi
from mininet.wifi.node import OVSKernelAP
from mininet.wifi.wmediumdConnector import WmediumdStarter

def topology():
    "Create a network."
    net = Mininet_wifi(controller=Controller, accessPoint=OVSKernelAP, wmediumd_mode=1, wmediumd_log_level=0,
                       topo='linear', switch=OVSKernelAP, link=wmediumd, enable_interference=True)
    
    print("*** Creating nodes")
    # Access Points
    ap1 = net.addAccessPoint('ap1', ssid='studentID', mode='g', channel='1', failMode='standalone')
    ap2 = net.addAccessPoint('ap2', ssid='studentID', mode='g', channel='6', failMode='standalone')
    ap3 = net.addAccessPoint('ap3', ssid='studentID', mode='g', channel='11', failMode='standalone')
    # Stations
    sta1 = net.addStation('sta1', ip='192.168.1.1/24')
    sta2 = net.addStation('sta2', ip='192.168.1.2/24')
    sta3 = net.addStation('sta3', ip='192.168.1.3/24')
    sta4 = net.addStation('sta4', ip='192.168.1.4/24')
    sta5 = net.addStation('sta5', ip='192.168.1.5/24')
    # Switches
    s1 = net.addSwitch('s1')

    print("*** Creating links")
    net.addLink(ap1, s1)
    net.addLink(ap2, s1)
    net.addLink(ap3, s1)
    net.addLink(s1, sta1)
    net.addLink(s1, sta2)
    net.addLink(s1, sta3)
    net.addLink(s1, sta4)
    net.addLink(s1, sta5)

    print("*** Starting network")
    net.build()
    c1.start()

    print("*** Starting controllers")
    net.start()
    
    print("*** Mobility")
    net.plotGraph(max_x=200, max_y=200)
    net.startMobility(time=0)
    net.mobility(sta1, 'start', time=10, position='10.0,20.0')
    net.mobility(sta1, 'stop', time=20, position='50.0,20.0')
    # Add mobility for other stations in a similar manner
    net.stopMobility(time=30)

    print("*** Running CLI")
    CLI_wifi(net)

    print("*** Stopping network")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
