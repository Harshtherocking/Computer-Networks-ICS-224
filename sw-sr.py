## Harsh Vardhan Singh Chauhan
### 2022BCD0044
#### Stop-and-Wait
```py
import time

SWS = 4
RWS = 1
TimeOut = 1


def msg_to_frames(msg : str, size : int):
frames = []
for i in range(len(MSG)//size):
frames.append(msg[i:i+SWS])
return frames

def SlidingWindow():
ith = 1
win_idx = 0
retransmission = 0
transmission = 0
while win_idx < len(FRAMES):
window = FRAMES[win_idx : win_idx + SWS]
# sending
print(f"Sending Window having Frames : ", window, sep = "\n" )
time.sleep(TimeOut)
# recieving
for i in range(len(window)):
time.sleep(TimeOut)
if not ith % 5:
print(f"N-ACK recieved for frame : ", window[i], sep="\n" )
# no change in window index and immediate retransmission
retransmission += 1
ith +=1
break
print(f"P-ACK recieved for frame : ", window[i], sep="\n" )
win_idx += 1
ith +=1
transmission +=1

print(f"Total Transmissions : {transmission + retransmission}", f"Total Retransmission : {retransmission}", sep = "\n")



if __name__ == "__main__":
MSG = "10101010101010"
FrameSize = 2
FRAMES = msg_to_frames(MSG, FrameSize)
print(f"Frames are : " , len(FRAMES))
SlidingWindow()
```
```console
Enter the Frame size : 2
No of Frames : 30
Frames: {frames}

sending ----- 10 -----
ACK Rev for ----- 10 -----


sending ----- 01 -----
ACK Rev for ----- 01 -----


sending ----- 10 -----
ACK Rev for ----- 10 -----


sending ----- 01 -----
ACK Rev for ----- 01 -----


sending ----- 10 -----
ACK Rev for ----- 10 -----


sending ----- 01 -----
ACK Not REV for ----- 01 -----


sending ----- 01 -----
ACK Rev for ----- 01 -----


sending ----- 10 -----
ACK Rev for ----- 10 -----


sending ----- 01 -----
ACK Rev for ----- 01 -----


sending ----- 10 -----
ACK Rev for ----- 10 -----


sending ----- 01 -----
ACK Rev for ----- 01 -----


sending ----- 10 -----
ACK Not REV for ----- 10 -----


sending ----- 10 -----
ACK Rev for ----- 10 -----


sending ----- 01 -----
ACK Rev for ----- 01 -----


sending ----- 10 -----
ACK Rev for ----- 10 -----


sending ----- 01 -----
ACK Rev for ----- 01 -----


sending ----- 10 -----
ACK Rev for ----- 10 -----


sending ----- 01 -----
ACK Not REV for ----- 01 -----


sending ----- 01 -----
ACK Rev for ----- 01 -----


sending ----- 10 -----
ACK Rev for ----- 10 -----


sending ----- 01 -----
ACK Rev for ----- 01 -----


sending ----- 10 -----
ACK Rev for ----- 10 -----


sending ----- 01 -----
ACK Rev for ----- 01 -----


sending ----- 10 -----
ACK Not REV for ----- 10 -----


sending ----- 10 -----
ACK Rev for ----- 10 -----


sending ----- 01 -----
ACK Rev for ----- 01 -----


sending ----- 10 -----
ACK Rev for ----- 10 -----


sending ----- 01 -----
ACK Rev for ----- 01 -----


sending ----- 10 -----
ACK Rev for ----- 10 -----


sending ----- 01 -----
ACK Not REV for ----- 01 -----


sending ----- 01 -----
ACK Rev for ----- 01 -----


sending ----- 10 -----
ACK Rev for ----- 10 -----


sending ----- 01 -----
ACK Rev for ----- 01 -----


sending ----- 10 -----
ACK Rev for ----- 10 -----


sending ----- 01 -----
ACK Rev for ----- 01 -----

No of retransmitions : 5
No of total frames sent : 35
```
#### Sliding Window
```py
import time

SWS = 4
RWS = 1
TimeOut = 1


def msg_to_frames(msg : str, size : int):
    frames = []
    for i in range(len(MSG)//size):
        frames.append(msg[i:i+SWS])
    return frames

def SlidingWindow():
    ith = 1
    win_idx = 0
    retransmission = 0
    transmission = 0
    while win_idx < len(FRAMES):
        window = FRAMES[win_idx : win_idx + SWS]
        # sending
        print(f"Sending Window having Frames : ", window, sep = "\n" )
        time.sleep(TimeOut)
        # recieving
        for i in range(len(window)):
            time.sleep(TimeOut)
            if not ith % 5:
                print(f"N-ACK recieved for frame : ", window[i], sep="\n" )
                # no change in window index and immediate retransmission
                retransmission += 1
                ith +=1
                break
            print(f"P-ACK recieved for frame : ", window[i], sep="\n" )
            win_idx += 1
            ith +=1
            transmission +=1

    print(f"Total Transmissions : {transmission + retransmission}", f"Total Retransmission : {retransmission}", sep = "\n")



if __name__ == "__main__":
    MSG = "10110"*4
    FrameSize = 2
    FRAMES = msg_to_frames(MSG, FrameSize)
    print(f"Frames are : " , len(FRAMES))
    SlidingWindow()
```
```console
Frames are :  10
Sending Window having Frames :
['1011', '0110', '1101', '1010']
P-ACK recieved for frame :
1011
P-ACK recieved for frame :
0110
P-ACK recieved for frame :
1101
P-ACK recieved for frame :
1010
Sending Window having Frames :
['0101', '1011', '0110', '1101']
N-ACK recieved for frame :
0101
Sending Window having Frames :
['0101', '1011', '0110', '1101']
P-ACK recieved for frame :
0101
P-ACK recieved for frame :
1011
P-ACK recieved for frame :
0110
P-ACK recieved for frame :
1101
Sending Window having Frames :
['1010', '0101']
N-ACK recieved for frame :
1010
Sending Window having Frames :
['1010', '0101']
P-ACK recieved for frame :
1010
P-ACK recieved for frame :
0101
Total Transmissions : 12
Total Retransmission : 2
```
