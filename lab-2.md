# Cisco Packet Tracer (Cisco-PT): Establishing network connections using Hub, Switch
- Name : Harsh Vardhan Singh Chauhan
- Roll no : 2022BCD0044
- Batch no : 2
- Domain name : 
- IP address : `192.168.10.89`
- MAC : `f4:39:09:2b:c2:fc`
- Date : `Thursday 25 January 2024 02:51:49 PM IST`

# Exercise-1
### Aim : 
### Requirements : 
### Physical Connection : 
![image](https://github.com/Harshtherocking/Computer-Networks-ICS-224/assets/65885345/eac3a4ef-d3e2-4335-8c8a-d72521de1eba)

### Procedure :
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


