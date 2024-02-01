# Cisco Packet Tracer (Cisco-PT): Establishing network connections using Router and Switch
- Name : Harsh Vardhan Singh Chauhan
- Roll no : 2022BCD0044
- Batch no : 2
- Domain name : 
- IP address : `192.168.10.89`
- MAC : `f4:39:09:2b:c2:fc`
- Date : `Thursday 01 February 2024 03:15:11 PM IST`

# Excercise-1
### Aim :
To establish a connection between devices using switch and Router. Observe the working of the Hub using ping packets and by running the Packet tracer in Simulation mode. (Send ping packets using the Traffic generator from PC-A)
### Requirement :
1) Cisco Packet Tracer 8.2.1
2) Windows PCs must have One NIC cards. Routers, Switches
3) RJ-45 Sockets – Copper straight-through, cross-over Wire.
4) Class A & C IP Address using Static IP configuration.
### Physical Connection :
![image](https://github.com/Harshtherocking/Computer-Networks-ICS-224/assets/65885345/269ea192-a8af-4d74-a4d6-5f4f7f228b99)

### Observation :
ping from PC-A to other PC's
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
```console
C:\>ping 192.168.2.3

Pinging 192.168.2.3 with 32 bytes of data:

Request timed out.
Reply from 192.168.2.3: bytes=32 time<1ms TTL=127
Reply from 192.168.2.3: bytes=32 time<1ms TTL=127
Reply from 192.168.2.3: bytes=32 time<1ms TTL=127

Ping statistics for 192.168.2.3:
    Packets: Sent = 4, Received = 3, Lost = 1 (25% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms```
```
ARP command fot PC-A
```console
C:\>arp -a
  Internet Address      Physical Address      Type
  192.168.1.1           000a.4157.5a01        dynamic
  192.168.1.4           0006.2ad8.35b4        dynamic
```
packet transition from PC-A to PC-C
![1-c-ezgif com-video-to-gif-converter](https://github.com/Harshtherocking/Computer-Networks-ICS-224/assets/65885345/7e7e42b2-ce9c-4886-b129-f971d7396558)



# Excercise-2
### Aim : 
To establish a connection between two different networks connected between each other through switches and Routers . Add Static routing tables at the router. In Office and Home Network → PCs are connected to router through separate switches. Add at least two PCs in each network
### Requirement :
1) Cisco Packet Tracer 8.2.1
2) Windows PCs must have One NIC cards. Routers, Switches
3) RJ-45 Sockets – Copper straight-through, cross-over Wire.
4) Class A & C IP Address using Static IP configuration.
### Physical Connection :
![image](https://github.com/Harshtherocking/Computer-Networks-ICS-224/assets/65885345/6da5ca7d-54d6-47e7-afca-4d8f23d1c31b)
### Observation
ping from PC-A to other PC's
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
``` console
C:\>ping 192.168.2.4

Pinging 192.168.2.4 with 32 bytes of data:

Reply from 192.168.2.4: bytes=32 time=33ms TTL=126
Reply from 192.168.2.4: bytes=32 time=21ms TTL=126
Reply from 192.168.2.4: bytes=32 time=1ms TTL=126
Reply from 192.168.2.4: bytes=32 time=15ms TTL=126

Ping statistics for 192.168.2.4:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 33ms, Average = 17ms
```
ARP command for PC-A
```console
C:\>arp -a
  Internet Address      Physical Address      Type
  192.168.1.1           000a.419a.7e78        dynamic
  192.168.1.4           0001.9613.d1e8        dynamic
```
packet transition from PC-A to PC-D
![2-c-ezgif com-video-to-gif-converter](https://github.com/Harshtherocking/Computer-Networks-ICS-224/assets/65885345/6b2aad2e-788d-439d-b5e4-fbf634b206df)
