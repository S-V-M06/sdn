#!/usr/bin/env python3
"""
ARP Controller for SDN Networks
Handles ARP request/reply processing using packet interception
"""

from scapy.all import sniff, Ether, ARP, sendp, conf, get_if_hwaddr
from scapy.arch import get_if_list
import logging
import threading
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class ARPController:
    """
    SDN-style Controller for ARP packet handling
    - Intercepts ARP packets
    - Generates ARP responses
    - Enables host discovery
    - Validates communication
    """
    
    def __init__(self, interface=None):
        """Initialize the ARP Controller"""
        self.interface = interface or conf.iface
        self.arp_table = {}  # IP to MAC mapping
        self.mac_to_port = {}  # MAC to interface mapping
        self.running = False
        logger.info(f"ARP Controller Initialized on interface: {self.interface}")
        
        # Verify interface exists
        if self.interface not in get_if_list():
            logger.error(f"Interface {self.interface} not found!")
            logger.info(f"Available interfaces: {get_if_list()}")
            sys.exit(1)

    def packet_callback(self, pkt):
        """Callback function to process ARP packets"""
        if ARP in pkt:
            arp_layer = pkt[ARP]
            
            if arp_layer.op == 1:  # ARP Request
                self.handle_arp_request(pkt, arp_layer)
            elif arp_layer.op == 2:  # ARP Reply
                self.handle_arp_reply(pkt, arp_layer)

    def handle_arp_request(self, pkt, arp_layer):
        """Handle incoming ARP request"""
        src_ip = arp_layer.psrc
        src_mac = arp_layer.hwsrc
        dst_ip = arp_layer.pdst
        
        logger.info(f"[ARP REQUEST] {src_ip} ({src_mac}) -> {dst_ip}")
        
        # Learn the mapping
        self.arp_table[src_ip] = src_mac
        
        # Generate ARP reply
        self.send_arp_reply(src_mac, src_ip, dst_ip)

    def handle_arp_reply(self, pkt, arp_layer):
        """Handle incoming ARP reply"""
        src_ip = arp_layer.psrc
        src_mac = arp_layer.hwsrc
        
        logger.info(f"[ARP REPLY] {src_ip} -> {src_mac}")
        
        # Learn the mapping
        self.arp_table[src_ip] = src_mac

    def send_arp_reply(self, src_mac, src_ip, dst_ip):
        """Generate and send ARP reply"""
        try:
            # Get our MAC address
            our_mac = get_if_hwaddr(self.interface)
            
            # Create ARP reply packet
            arp_reply = Ether(dst=src_mac)/ARP(
                op="is-at",
                hwsrc=our_mac,
                psrc=dst_ip,
                hwdst=src_mac,
                pdst=src_ip
            )
            
            # Send the reply
            sendp(arp_reply, iface=self.interface, verbose=False)
            logger.info(f"[ARP REPLY SENT] {our_mac} -> {src_mac}")
        except Exception as e:
            logger.error(f"Error sending ARP reply: {e}")

    def start(self):
        """Start the ARP controller"""
        self.running = True
        logger.info(f"Starting ARP Controller on {self.interface}...")
        print(f"\n{'='*60}")
        print(f"ARP Controller is running on {self.interface}")
        print(f"Press Ctrl+C to stop")
        print(f"{'='*60}\n")
        
        try:
            # Start sniffing for ARP packets
            sniff(
                prn=self.packet_callback,
                filter="arp",
                iface=self.interface,
                store=False,
                stop_filter=lambda x: not self.running
            )
        except KeyboardInterrupt:
            self.stop()
        except PermissionError:
            logger.error("Error: This program requires root/sudo privileges!")
            sys.exit(1)
        except Exception as e:
            logger.error(f"Error: {e}")
            sys.exit(1)

    def stop(self):
        """Stop the ARP controller"""
        self.running = False
        logger.info("Stopping ARP Controller...")
        print("\n" + "="*60)
        print("ARP Controller stopped")
        print("="*60)
        
        # Print ARP table
        if self.arp_table:
            logger.info("\n=== Learned ARP Mappings ===")
            for ip, mac in sorted(self.arp_table.items()):
                logger.info(f"  {ip:15} -> {mac}")
        else:
            logger.info("No entries in ARP table")

    def print_arp_table(self):
        """Print current ARP table"""
        if self.arp_table:
            logger.info("\n=== Current ARP Table ===")
            for ip, mac in sorted(self.arp_table.items()):
                logger.info(f"  {ip:15} -> {mac}")
        else:
            logger.info("ARP Table is empty")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='ARP Controller for SDN Networks')
    parser.add_argument('--interface', '-i', help='Network interface to use')
    
    args = parser.parse_args()
    
    controller = ARPController(interface=args.interface)
    controller.start()


if __name__ == '__main__':
    main()
