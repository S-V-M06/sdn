#!/usr/bin/env python3
"""
Mininet Topology for ARP Handling in SDN Networks
Creates a virtual network with switches and hosts to test ARP controller
"""

from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

def create_topology():
    """Create a simple SDN network topology with Mininet"""
    
    # Create network without built-in controller, use RemoteController
    net = Mininet(
        controller=RemoteController,
        switch=OVSKernelSwitch,
        link=TCLink,
        xterms=False,
        autoSetMacs=True,
        autoStaticArp=False  # Don't use static ARP - let dynamic ARP work
    )
    
    info("★ Creating SDN Network Topology for ARP Testing\n")
    
    # Add remote controller
    c0 = net.addController('c0', ip='127.0.0.1', port=6633)
    info("✓ Added RemoteController c0 (127.0.0.1:6633)\n")
    
    # Add switches
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, protocols='OpenFlow13')
    info("✓ Added Switch s1 (OpenFlow 1.3)\n")
    
    # Add hosts
    h1 = net.addHost('h1', ip='10.0.0.1', mac='00:00:00:00:00:01')
    h2 = net.addHost('h2', ip='10.0.0.2', mac='00:00:00:00:00:02')
    h3 = net.addHost('h3', ip='10.0.0.3', mac='00:00:00:00:00:03')
    info("✓ Added Hosts h1, h2, h3\n")
    
    # Add links
    net.addLink(h1, s1, bw=10)
    net.addLink(h2, s1, bw=10)
    net.addLink(h3, s1, bw=10)
    info("✓ Connected hosts to switch\n")
    
    # Start network
    net.start()
    info("\n")
    info("="*70 + "\n")
    info("★ MININET TOPOLOGY READY FOR ARP TESTING\n")
    info("="*70 + "\n")
    info("Network Details:\n")
    info(f"  Switch: s1 (OpenFlow 1.3 enabled)\n")
    info(f"  Hosts: h1 (10.0.0.1), h2 (10.0.0.2), h3 (10.0.0.3)\n")
    info(f"  Controller: RemoteController on 127.0.0.1:6633\n")
    info("\n")
    info("TO USE WITH ARP CONTROLLER:\n")
    info("  1. In another terminal, run: sudo -E python3 arp_controller.py\n")
    info("  2. Then test ARP commands below\n")
    info("\n")
    info("AVAILABLE COMMANDS IN CLI:\n")
    info("  h1 ping h2              - Test ARP with ping\n")
    info("  h1 arp -n               - View ARP table\n")
    info("  h1 arping 10.0.0.2      - Send ARP request\n")
    info("  h1 tcpdump -i h1-eth0 -n arp  - Capture ARP packets\n")
    info("  dump                    - Show topology\n")
    info("  links                   - Show all links\n")
    info("  net                     - Show network info\n")
    info("  h1 ifconfig             - Show interface config\n")
    info("  exit                    - Exit Mininet\n")
    info("="*70 + "\n\n")
    
    # Start CLI
    CLI(net)
    
    # Cleanup
    info("\nStopping network...\n")
    net.stop()
    info("✓ Network stopped\n")

if __name__ == '__main__':
    setLogLevel('info')
    create_topology()
    
    # Add switches
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, protocols='OpenFlow13')
    info("✓ Added Switch s1 (OpenFlow 1.3)\n")
    
    # Add hosts
    h1 = net.addHost('h1', ip='10.0.0.1', mac='00:00:00:00:00:01')
    h2 = net.addHost('h2', ip='10.0.0.2', mac='00:00:00:00:00:02')
    h3 = net.addHost('h3', ip='10.0.0.3', mac='00:00:00:00:00:03')
    info("✓ Added Hosts h1, h2, h3\n")
    
    # Add links
    net.addLink(h1, s1, bw=10)
    net.addLink(h2, s1, bw=10)
    net.addLink(h3, s1, bw=10)
    info("✓ Connected hosts to switch\n")
    
    # Start network
    net.start()
    info("\n")
    info("="*70 + "\n")
    info("★ MININET TOPOLOGY READY FOR ARP TESTING\n")
    info("="*70 + "\n")
    info("Network Details:\n")
    info(f"  Switch: s1 (OpenFlow 1.3 enabled)\n")
    info(f"  Hosts: h1 (10.0.0.1), h2 (10.0.0.2), h3 (10.0.0.3)\n")
    info(f"  Controller: RemoteController on 127.0.0.1:6633\n")
    info("\n")
    info("TO USE WITH ARP CONTROLLER:\n")
    info("  1. In another terminal, run: sudo -E python3 arp_controller.py\n")
    info("  2. Then run the commands below\n")
    info("\n")
    info("AVAILABLE COMMANDS IN CLI:\n")
    info("  h1 ping h2              - Test ARP with ping\n")
    info("  h1 arp -n               - View ARP table\n")
    info("  h1 arping 10.0.0.2      - Send ARP request\n")
    info("  h1 tcpdump -i h1-eth0 -n arp  - Capture ARP packets\n")
    info("  dump                    - Show topology\n")
    info("  links                   - Show all links\n")
    info("  net                     - Show network info\n")
    info("  h1 ifconfig             - Show interface config\n")
    info("  exit                    - Exit Mininet\n")
    info("="*70 + "\n\n")
    
    # Start CLI
    CLI(net)
    
    # Cleanup
    info("\nStopping network...\n")
    net.stop()
    info("✓ Network stopped\n")

if __name__ == '__main__':
    setLogLevel('info')
    create_topology()

if __name__ == '__main__':
    setLogLevel('info')
    create_topology()
