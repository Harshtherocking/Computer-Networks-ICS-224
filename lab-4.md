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

ARP command for PC-A
```console
C:\>arp  -a
  Internet Address      Physical Address      Type
  192.168.1.1           0040.0ba5.0b44        dynamic
  192.168.1.3           0000.0c6e.2c0d        dynamic
```
`Mac address for PC-F is not visible in ARP command of PC-A. Only PC-B and Router-0 MAC addresses are visible`

IP Route for Router-0
```console
Router>enable
Router#show ip route
Codes: C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

C    10.0.0.0/8 is directly connected, Serial2/0
C    192.168.1.0/24 is directly connected, FastEthernet0/0
S    192.168.2.0/24 [1/0] via 10.0.0.2
S    192.168.3.0/24 [1/0] via 10.0.0.2
```
IP Route for Router-1
```console
Router>enable
Router#show ip route
Codes: C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

C    10.0.0.0/8 is directly connected, Serial2/0
C    11.0.0.0/8 is directly connected, Serial3/0
S    192.168.1.0/24 [1/0] via 10.0.0.1
C    192.168.2.0/24 is directly connected, FastEthernet0/0
S    192.168.3.0/24 [1/0] via 11.0.0.2
```
IP Route for Router-2
```console
Router>enable 
Router#show ip route
Codes: C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

C    11.0.0.0/8 is directly connected, Serial2/0
S    192.168.1.0/24 [1/0] via 11.0.0.1
S    192.168.2.0/24 [1/0] via 11.0.0.1
C    192.168.3.0/24 is directly connected, FastEthernet0/0
```
Table 
| SOURCE | DESTINATION | ONE-WAY LATENCY | ROUND TRIP TIME |
| ------ | ----------- | --------------- | --------------- |
| PC-A   | PC-F        | 0.015 sec       | 0.027 sec       |
| PC-A   | PC-D        | 0.010 sec       | 0.017 sec       |
| PC-C   | PC-B        | 0.012 sec       | 0.021 sec       |
| PC-C   | PC-E        | 0.014 sec       | 0.027 sec       |
| PC-E   | PC-B        | 0.014 sec       | 0.026 sec       |
| PC-E   | PC-C        | 0.011 sec       | 0.022 sec       |

`OFFICE to CLUB transmission and vica-versa take the most time because the message needs to pass through two routers. Message passing delay increases with increase in number of network devices it passes through.`
