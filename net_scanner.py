import scapy.all as scapy


ip=input("Enter the target Network IP Address: ")
arp_request_packet=scapy.ARP(pdst=ip) # pdst meand Target Protocol Address(TPA)
arp_broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #broadcast MAC Address
combined_packet= arp_broadcast_packet/arp_request_packet  
(answered,unanswered)=scapy.srp(combined_packet,timeout=1)

IPs_MACs=[]

for sent,received in answered:
    IPs_MACs.append({'ip':received.psrc,'mac':received.hwsrc})# psrc means Sender Protocol Address(SPA), hwsrc means Sender Hardware Address(SHA)
print("IP"+" "*15+"MAC")
for host in IPs_MACs:
    print(f"{host['ip']:17}{host['mac']}")
