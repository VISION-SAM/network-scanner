#!/usr/bin/env python

import scapy.all as scapy

def scan_network(ip):
    pass

# Get input from user
ip = input("Enter the Network IP address/cidr: ")

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return  clients_list

def print_result(result_list):
    print("IP\t\t\tMAC Address\n--------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

# Call the function with the input values
scan_network(ip)
# Capture input the network ip from user.

scan_result = scan(ip)
# broadcast arp request and scan result.

print_result(scan_result)
# Finaly print the scanned result.






