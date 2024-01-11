### Name : Harsh Vardhan Singh Chauhan
### Roll no : 2022BCD0044
### Batch no : 2
### Domain name : 
### IP address : `192.168.10.89`
### MAC : `f4:39:09:2b:c2:fc`
- Date : `Thursday 11 January 2024 03:40:38 PM IST`

# Exercise - 1
### Aim
To establish a connection between two devices through Copper Crossover wire using Cisco packet tracer
### Requirements
1) Cisco Packet Tracer 8.2.1
2) Windows PC or 2 Linux PC, Each PC must Have One NIC cards.
3) RJ-45 Sockets – Copper Cross-over Wire.
4) Class C IP Address using Static IP configuration.
### Physical Connection
![image](https://github.com/Harshtherocking/Computer-Networks-ICS-224/assets/65885345/1c9c27f9-3454-416a-ada4-74ce65392cf5)


pinging PC-B from PC-A
```console
C:\>ping 192.168.1.2

Pinging 192.168.1.2 with 32 bytes of data:

Reply from 192.168.1.2: bytes=32 time=9ms TTL=128
Reply from 192.168.1.2: bytes=32 time<1ms TTL=128
Reply from 192.168.1.2: bytes=32 time<1ms TTL=128
Reply from 192.168.1.2: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.1.2:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 9ms, Average = 2ms
```

IP for PC-A
```console
C:\>ipconfig

FastEthernet0 Connection:(default port)

   Connection-specific DNS Suffix..: 
   Link-local IPv6 Address.........: FE80::20C:85FF:FE2C:A44
   IPv6 Address....................: ::
   IPv4 Address....................: 192.168.1.1
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: ::
                                     192.168.1.1

Bluetooth Connection:

   Connection-specific DNS Suffix..: 
   Link-local IPv6 Address.........: ::
   IPv6 Address....................: ::
   IPv4 Address....................: 0.0.0.0
   Subnet Mask.....................: 0.0.0.0
   Default Gateway.................: ::
                                     0.0.0.0
```

IP for PC-B
```console
C:\>ipconfig

FastEthernet0 Connection:(default port)

   Connection-specific DNS Suffix..: 
   Link-local IPv6 Address.........: FE80::201:64FF:FEC7:A604
   IPv6 Address....................: ::
   IPv4 Address....................: 192.168.1.2
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: ::
                                     192.168.1.2

Bluetooth Connection:

   Connection-specific DNS Suffix..: 
   Link-local IPv6 Address.........: ::
   IPv6 Address....................: ::
   IPv4 Address....................: 0.0.0.0
   Subnet Mask.....................: 0.0.0.0
   Default Gateway.................: ::
                                     0.0.0.0
```
pinging PC-A from PC-B
```console
C:\>ping 192.168.1.1

Pinging 192.168.1.1 with 32 bytes of data:

Reply from 192.168.1.1: bytes=32 time<1ms TTL=128
Reply from 192.168.1.1: bytes=32 time<1ms TTL=128
Reply from 192.168.1.1: bytes=32 time<1ms TTL=128
Reply from 192.168.1.1: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.1.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```

checking IP for PC-A from PC-B
```console
C:\>arp -a
  Internet Address      Physical Address      Type
  192.168.1.1           000c.852c.0a44        dynamic

```

checking IP for PC-B from PC-A
```console
C:\>arp -a
  Internet Address      Physical Address      Type
  192.168.1.2           0001.64c7.a604        dynamic
```

# Exercise - 2
### Aim
To establish the connection between two devices with one switch through Copper Straight Through cable.
### Requirements
1) Cisco Packet Tracer 8.2.1
2) Windows PC or 2 Linux PC, Each PC must Have One NIC cards.
3) RJ-45 Sockets – Copper Cross-over Wire.
4) Class C IP Address using Static IP configuration.
### Physical Connection
![image](https://github.com/Harshtherocking/Computer-Networks-ICS-224/assets/65885345/5d50c342-722c-4660-98e1-e34d8552f278)

for PC-A
```console
C:\>ipconfig

FastEthernet0 Connection:(default port)

   Connection-specific DNS Suffix..: 
   Link-local IPv6 Address.........: FE80::2E0:8FFF:FEE3:6CBE
   IPv6 Address....................: ::
   IPv4 Address....................: 192.168.1.1
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: ::
                                     192.168.1.1

Bluetooth Connection:

   Connection-specific DNS Suffix..: 
   Link-local IPv6 Address.........: ::
   IPv6 Address....................: ::
   IPv4 Address....................: 0.0.0.0
   Subnet Mask.....................: 0.0.0.0
   Default Gateway.................: ::
                                     0.0.0.0
```
```console
C:\>ping 192.168.1.2

Pinging 192.168.1.2 with 32 bytes of data:

Reply from 192.168.1.2: bytes=32 time<1ms TTL=128
Reply from 192.168.1.2: bytes=32 time=4ms TTL=128
Reply from 192.168.1.2: bytes=32 time<1ms TTL=128
Reply from 192.168.1.2: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.1.2:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 4ms, Average = 1ms
```
```console
C:\>arp -a
  Internet Address      Physical Address      Type
  192.168.1.2           0030.a330.7dd6        dynamic
```

for PC-B
```console
C:\>ipconfig

FastEthernet0 Connection:(default port)

   Connection-specific DNS Suffix..: 
   Link-local IPv6 Address.........: FE80::230:A3FF:FE30:7DD6
   IPv6 Address....................: ::
   IPv4 Address....................: 192.168.1.2
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: ::
                                     192.168.1.2

Bluetooth Connection:

   Connection-specific DNS Suffix..: 
   Link-local IPv6 Address.........: ::
   IPv6 Address....................: ::
   IPv4 Address....................: 0.0.0.0
   Subnet Mask.....................: 0.0.0.0
   Default Gateway.................: ::
                                     0.0.0.0
```
```console
C:\>ping 192.168.1.1

Pinging 192.168.1.1 with 32 bytes of data:

Reply from 192.168.1.1: bytes=32 time<1ms TTL=128
Reply from 192.168.1.1: bytes=32 time<1ms TTL=128
Reply from 192.168.1.1: bytes=32 time<1ms TTL=128
Reply from 192.168.1.1: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.1.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```
```console
C:\>arp -a
  Internet Address      Physical Address      Type
  192.168.1.1           00e0.8fe3.6cbe        dynamic
```

for Switch - checking MAC adress table
```
%LINK-5-CHANGED: Interface FastEthernet0/1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/1, changed state to up

%LINK-5-CHANGED: Interface FastEthernet0/2, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/2, changed state to up

Switch>enable
Switch#show mac-address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----

Switch#
```

# Excercise - 3
### Aim
To establish the connection between five devices with one switch through Copper Straight Through cable.
### Requirements
1) Cisco Packet Tracer 8.2.1
2) Windows PC or 2 Linux PC, Each PC must Have One NIC cards.
3) RJ-45 Sockets – Copper Cross-over Wire.
4) Class C IP Address using Static IP configuration.
### Physical Connection
![image](https://github.com/Harshtherocking/Computer-Networks-ICS-224/assets/65885345/54fd1dc9-5fc5-413f-a92d-0139d4b0f3e7)

IP for PC-A
```console
C:\>ipconfig

FastEthernet0 Connection:(default port)

   Connection-specific DNS Suffix..: 
   Link-local IPv6 Address.........: FE80::260:3EFF:FE9A:C091
   IPv6 Address....................: ::
   IPv4 Address....................: 192.168.1.1
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: ::
                                     192.168.1.1

Bluetooth Connection:

   Connection-specific DNS Suffix..: 
   Link-local IPv6 Address.........: ::
   IPv6 Address....................: ::
   IPv4 Address....................: 0.0.0.0
   Subnet Mask.....................: 0.0.0.0
   Default Gateway.................: ::
                                     0.0.0.0
```

IP for PC-B
```console
C:\>ipconfig

FastEthernet0 Connection:(default port)

   Connection-specific DNS Suffix..: 
   Link-local IPv6 Address.........: FE80::230:F2FF:FE7B:AB0B
   IPv6 Address....................: ::
   IPv4 Address....................: 192.168.1.2
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: ::
                                     192.168.1.2

Bluetooth Connection:

   Connection-specific DNS Suffix..: 
   Link-local IPv6 Address.........: ::
   IPv6 Address....................: ::
   IPv4 Address....................: 0.0.0.0
   Subnet Mask.....................: 0.0.0.0
   Default Gateway.................: ::
                                     0.0.0.0
```

pinging other PCs from PC-D
```console
C:\>ping 192.168.1.1

Pinging 192.168.1.1 with 32 bytes of data:

Reply from 192.168.1.1: bytes=32 time<1ms TTL=128
Reply from 192.168.1.1: bytes=32 time<1ms TTL=128
Reply from 192.168.1.1: bytes=32 time<1ms TTL=128
Reply from 192.168.1.1: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.1.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```
```console
C:\>ping 192.168.1.5

Pinging 192.168.1.5 with 32 bytes of data:

Reply from 192.168.1.5: bytes=32 time=1ms TTL=128
Reply from 192.168.1.5: bytes=32 time<1ms TTL=128
Reply from 192.168.1.5: bytes=32 time<1ms TTL=128
Reply from 192.168.1.5: bytes=32 time=6ms TTL=128

Ping statistics for 192.168.1.5:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 6ms, Average = 1ms
```
ARP command for PC-A
```console
C:\>arp -a
  Internet Address      Physical Address      Type
  192.168.1.3           000a.f3d0.506b        dynamic
  192.168.1.4           0001.63cc.8e3b        dynamic
```
ARP command for PC-B
```console
C:\>arp -a
  Internet Address      Physical Address      Type
  192.168.1.3           000a.f3d0.506b        dynamic
```
ARP command for PC-C
```console
C:\>arp -a
  Internet Address      Physical Address      Type
  192.168.1.1           0060.3e9a.c091        dynamic
  192.168.1.2           0030.f27b.ab0b        dynamic
  192.168.1.4           0001.63cc.8e3b        dynamic
  192.168.1.5           0040.0b91.dd9e        dynamic
```
ARP command for PC-D
```console
C:\>arp -a
  Internet Address      Physical Address      Type
  192.168.1.1           0060.3e9a.c091        dynamic
  192.168.1.5           0040.0b91.dd9e        dynamic
```
ARP command for PC-E
```console
C:\>arp -a
  Internet Address      Physical Address      Type
  192.168.1.4           0001.63cc.8e3b        dynamic
```


MAC Address Table for Switch
```console
Switch>enable
Switch#show mac-address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----

   1    0001.63cc.8e3b    DYNAMIC     Fa0/4
   1    000a.f3d0.506b    DYNAMIC     Fa0/3
   1    0030.f27b.ab0b    DYNAMIC     Fa0/2
   1    0040.0b91.dd9e    DYNAMIC     Fa0/5
   1    0060.3e9a.c091    DYNAMIC     Fa0/1
Switch#
```
