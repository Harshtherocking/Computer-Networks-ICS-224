# CRC AND HAMMING CODE IMPLEMENTATION
~ Harsh Vardhan Singh Chauhan 
~ 2022BCD0044
~ Python3 implementation

### CRC :- 
```python
# binary str to integer
def binary_to_int (binary_str : str) -> int : 
    binary_str = binary_str[::-1]
    rad = 1 
    integer = 0
    for digit in binary_str:
        integer = integer + rad * int(digit)
        rad = rad * 2
    
    return integer


# integer to binary string
def int_to_binary (integer : int) -> str  :
    binary_str = ""
    while (integer):
        binary_str = binary_str + str(integer%2)
        integer = integer // 2
    binary_str = binary_str[::-1]

    return binary_str


# message to binary string
def msg_to_bin (msg : str) -> str:
    nos = [int(n) for n in msg if n.isdigit()]
    if 1 in nos:
        nos.remove(1)
        nos.append(0)
    if " x " in msg:
        nos.append(1)
    nos.sort()

    binary_str = ["0"] * (nos[-1]+1)
    for no in nos:
        binary_str[no] = "1"

    binary_str = binary_str[::-1]
    return "".join(binary_str)



def bin_division(divident : str , divisor : str) -> str :
    window = divident[:len(divisor)]
    next  = divident[len(divisor):]
    while (next) :
        # print("window is ", window)
        if window[0] == "1":
            window = int_to_binary(binary_to_int(window) ^ binary_to_int(divisor)) + next[0]
            if len(window) < len(divisor):
                window = ( abs(len(divisor) - len(window)) * "0" ) + window
        else:
            window = int_to_binary(binary_to_int(window) ^ binary_to_int("0" * len(divisor))) + next[0]
            if len(window) < len(divisor):
                window = ( abs(len(divisor) - len(window)) * "0" ) + window
        next = next[1:]

    if window[0] == "1":
        window = int_to_binary(binary_to_int(window) ^ binary_to_int(divisor))
        if len(window) < len(divisor):
            window = ( abs(len(divisor) - len(window)-1) * "0" ) + window
    else:
        window = int_to_binary(binary_to_int(window) ^ binary_to_int("0" * len(divisor)))
        if len(window) < len(divisor):
            window = ( abs(len(divisor) - len(window)-1) * "0" ) + window

    return window




def CRC_encoder (msg : str, g : str):
    msg = msg_to_bin(msg)
    g  = msg_to_bin(g)
    remainder = bin_division(msg + "0" * (len(g)-1), g)
    print("Transmitted Message ", msg+remainder)
    return


def CRC_decoder (msg_recieved : str, g: str ) :
    g = msg_to_bin(g)
    remainder = bin_division(msg_recieved, g)
    print("Remainder is ", remainder)
    if binary_to_int(remainder) :
        print("Message is Corrputed (remainder != 1) ")
    else:
        print("Message is Transmitted Successfully (remainder = 0)")
    pass


# driver function
if __name__ == "__main__":
    print("SENDER's SIDE :")
    msg = input("Enter M(x) : ")
    g = input("Enter G(x) : ")
    CRC_encoder(msg, g)
    
    print("RECIEVER's SIDE : ")
    msg_recieved = input("Enter M_rec(x) : ")
    CRC_decoder(msg_recieved,g)
```
```console
SENDER's SIDE :
Enter M(x) :  x6 + x5 + x2 + x
Enter G(x) :  x3 + x2 + 1
Transmitted Message  1100110010
RECIEVER's SIDE :
Enter M_rec(x) : 1100110010
Remainder is  000
Message is Transmitted Successfully (remainder = 0)
```
```console
SENDER's SIDE :
Enter M(x) :  x6 + x5 + x2 + x
Enter G(x) :  x3 + x2 + 1
Transmitted Message  1100110010
RECIEVER's SIDE :
Enter M_rec(x) : 1110110010
Remainder is  001
Message is Corrputed (remainder != 1)
```
