from scapy.all import *
import base64

packets = rdpcap("myNetworkTraffic.pcap")
packet_numbers = [5, 2, 21, 7, 11, 16, 8]

decoded_payloads = []
for i in packet_numbers:
    packet = packets[i-1]
    if Raw in packet:
        payload = packet[Raw].load
        try:
            decoded = base64.b64decode(payload).decode('utf-8', errors='replace')
            decoded_payloads.append(decoded)
            print(f"Packet {i} payload (decoded): {decoded}")
        except Exception as e:
            print(f"Error decoding payload from packet {i}: {e}")

# Concatenate all decoded payloads
final_payload = ''.join(decoded_payloads)
print("\nFinal Decoded Payload:", final_payload)
