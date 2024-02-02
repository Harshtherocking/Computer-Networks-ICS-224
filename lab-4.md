# Cisco Packet Tracer (Cisco-PT): Establishing network connections using Router
- Name : Harsh Vardhan Singh Chauhan
- Roll no : 2022BCD0044
- Batch no : 2
- IP address : `192.168.10.89`
- MAC : `f4:39:09:2b:c2:fc`
- Date : `Friday 02 February 2024 09:37:21 PM IST`

# Exercise-1
### Aim :
To establish the connection between three different networks: Office, Home and Club networks using Routers and switches.
Office: 192.168.1.xxx
Home: 192.168.2.yyy
Club: 192.168.3.www
### Requirements : 
1) Cisco Packet Tracer 8.2.1
2) Windows PCs must have One NIC cards. Routers, Switches
3) RJ-45 Sockets – Copper straight-through.
4) Serial DCE cable between Routers.
5) Class A & C IP Address using Static IP configuration.
### Physical Connection : 
![image](https://github.com/Harshtherocking/Computer-Networks-ICS-224/assets/65885345/76ca4df9-fea0-4ffc-9c37-33bef2ac9428)
### Observation :
ping from PC-A
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
```console
C:\>ping 192.168.2.2

Pinging 192.168.2.2 with 32 bytes of data:

Request timed out.
Reply from 192.168.2.2: bytes=32 time=2ms TTL=126
Reply from 192.168.2.2: bytes=32 time=2ms TTL=126
Reply from 192.168.2.2: bytes=32 time=1ms TTL=126

Ping statistics for 192.168.2.2:
    Packets: Sent = 4, Received = 3, Lost = 1 (25% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 2ms, Average = 1ms
```
```console
C:\>ping 192.168.3.3

Pinging 192.168.3.3 with 32 bytes of data:

Request timed out.
Reply from 192.168.3.3: bytes=32 time=2ms TTL=125
Reply from 192.168.3.3: bytes=32 time=2ms TTL=125
Reply from 192.168.3.3: bytes=32 time=2ms TTL=125

Ping statistics for 192.168.3.3:
    Packets: Sent = 4, Received = 3, Lost = 1 (25% loss),
Approximate round trip times in milli-seconds:
    Minimum = 2ms, Maximum = 2ms, Average = 2ms
```
message transition from PC-A to PC-F

![Screencastfrom02-02-24094942PMIST-ezgif com-video-to-gif-converter](https://github.com/Harshtherocking/Computer-Networks-ICS-224/assets/65885345/3dd28c56-2d8b-479a-8d53-a7e4dc834882)

