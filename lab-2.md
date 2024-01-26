# Cisco Packet Tracer (Cisco-PT): Establishing network connections using Hub, Switch
- Name : Harsh Vardhan Singh Chauhan
- Roll no : 2022BCD0044
- Batch no : 2
- IP address : `192.168.10.89`
- MAC : `f4:39:09:2b:c2:fc`
- Date : `Thursday 25 January 2024 02:51:49 PM IST`

# Exercise-1
### Aim : 
To establish a connection between devices through copper straight-through wire using a Hub (Hub-PT). Observe the working of the Hub using ping packets and by running the Packet tracer in Simulation mode. (Send ping packets using the Traffic generator from PC-A).
### Requirements : 
1) Cisco Packet Tracer 8.2.1
2) Three Windows PC or Linux PC, Each PC must Have One NIC cards.
3) RJ-45 Sockets – Copper straight-through Wire.
4) Class C IP Address using Static IP configuration.
### Physical Connection : 
![image](https://github.com/Harshtherocking/Computer-Networks-ICS-224/assets/65885345/eac3a4ef-d3e2-4335-8c8a-d72521de1eba)

### Observation : 
pinging PC-B from PC-A
```console
C:\>ping 192.168.1.2

Pinging 192.168.1.2 with 32 bytes of data:

Reply from 192.168.1.2: bytes=32 time=8ms TTL=128
Reply from 192.168.1.2: bytes=32 time=4ms TTL=128
Reply from 192.168.1.2: bytes=32 time=4ms TTL=128
Reply from 192.168.1.2: bytes=32 time=4ms TTL=128

Ping statistics for 192.168.1.2:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 4ms, Maximum = 8ms, Average = 5ms
```
pinging PC-C from PC-A
```console
C:\>ping 192.168.1.3

Pinging 192.168.1.3 with 32 bytes of data:

Reply from 192.168.1.3: bytes=32 time<1ms TTL=128
Reply from 192.168.1.3: bytes=32 time<1ms TTL=128
Reply from 192.168.1.3: bytes=32 time<1ms TTL=128
Reply from 192.168.1.3: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.1.3:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```
sending packets from PC-C to PC-A and recieving acknowledgement packets from PC-A to PC-C
![ex-1](https://github.com/Harshtherocking/Computer-Networks-ICS-224/assets/65885345/f25c4cbb-2e71-42db-aae6-a880a86d8e89)
arp command on PC-A
```console
C:\>arp -a
  Internet Address      Physical Address      Type
  192.168.1.2           0009.7c61.1896        dynamic
  192.168.1.4           0060.3e43.908d        dynamic
  192.168.1.5           0002.4ac2.b533        dynamic
```


# Exercise-2
### Aim : 
To create two networks having the below architecture. All devices both the network must be able to communicate with each other. Give the addressing in such a manner. 
Office → Printer, Laptop, PC connected through an IP-phone (i.e, IP-phone is connected to the switch)
Home → PC, Laptop.
### Requirements : 
1) Cisco Packet Tracer 8.2.1
2) Three Windows PC or Linux PC, Each PC must Have One NIC cards.
3) RJ-45 Sockets – Copper straight-through Wire.
4) Class C IP Address using Static IP configuration.
### Physical Connection : 
![image](https://github.com/Harshtherocking/Computer-Networks-ICS-224/assets/65885345/8f053f90-c60a-4936-990b-d17be8064bb8)
### Observation : 
pinging other devices from PC-A
```console
C:\>ping 192.168.1.2

Pinging 192.168.1.2 with 32 bytes of data:

Reply from 192.168.1.2: bytes=32 time<1ms TTL=128
Reply from 192.168.1.2: bytes=32 time<1ms TTL=128
Reply from 192.168.1.2: bytes=32 time<1ms TTL=128
Reply from 192.168.1.2: bytes=32 time=12ms TTL=128

Ping statistics for 192.168.1.2:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 12ms, Average = 3ms
```
```console
C:\>ping 192.168.1.5

Pinging 192.168.1.5 with 32 bytes of data:

Reply from 192.168.1.5: bytes=32 time<1ms TTL=128
Reply from 192.168.1.5: bytes=32 time<1ms TTL=128
Reply from 192.168.1.5: bytes=32 time<1ms TTL=128
Reply from 192.168.1.5: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.1.5:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```
```console
C:\>ping 192.168.1.4

Pinging 192.168.1.4 with 32 bytes of data:

Reply from 192.168.1.4: bytes=32 time<1ms TTL=128
Reply from 192.168.1.4: bytes=32 time<1ms TTL=128
Reply from 192.168.1.4: bytes=32 time<1ms TTL=128
Reply from 192.168.1.4: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.1.4:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```
sending packets from PC-A to Laptop-B and recieving acknowledgement packets from Laptop-B to PC-A
![ex-2](https://github.com/Harshtherocking/Computer-Networks-ICS-224/assets/65885345/aae0d149-0e9d-4612-afa8-d8db7309230e)

changing the gateway for Home and Office and sending packet from PC-A to Laptop-B and recieving acknowledgement packets from Laptop-B to PC-A
![ex-2_adv](https://github.com/Harshtherocking/Computer-Networks-ICS-224/assets/65885345/811c99ee-5fa1-4247-b596-694e71ca41e9)
