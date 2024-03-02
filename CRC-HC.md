# CRC AND HAMMING CODE IMPLEMENTATION
- Harsh Vardhan Singh Chauhan 
- 2022BCD0044
- Python3 implementation

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
### Hamming Code
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


# even parity
def even_parity (data : str) -> bool :
    n = 0 
    for d in data:
        n = n ^ int(d) 
    return not bool(n)


# to find redundant bits count 
def find_redundant_bits (length:int) -> int : 
    m = length
    r = 1 
    while True : 
        if 2**r >=  m +r +1 :
            return r
        r+=1

# to find redundant bits from msg recieved
def find_redundant_bits_decode(length : int) -> int : 
    m_r = length 
    r = 1
    while True :
        if 2**r >= m_r + 1 :
            return r
        r+=1


# get redundant bit position
def get_r_pos(length : int) -> list[int] : 
    pos = []
    i = 0
    while True :
        if (2 ** i <= length):
            pos.append(2**i)
            i+=1
        else:
            return pos

# get redundant bit relation with other bits
def get_r_pos_rel(r_pos : list[int], length : int ) : 
    pos_rel = { k:[] for k in r_pos }
    for i in range (1, length + 1):
        for r in r_pos: 
            if i&r == r :
                pos_rel[r].append(i)

    return pos_rel


# filling redundant bits with values
def redundant_filler (pos : list[int] , msg : list[str]) -> bool : 
    # print(pos)
    # print(msg)
    string = [ msg[i-1] for i in pos if msg[i-1].isdigit() ] 
    if even_parity("".join(string)):
        return False

    return True



# encoding use Hamming Code
def HamEncode (dataword : str ) : 
    r_bits = find_redundant_bits(len(dataword))
    total_bits = len(dataword) + r_bits
    
    r_pos = get_r_pos(total_bits)
    r_pos_rel = get_r_pos_rel(r_pos, total_bits)
    
    msg = list(dataword)
    msg.reverse()
    for pos in r_pos:
        msg.insert(pos-1," ") 
    
    for r in r_pos_rel:
        if redundant_filler(r_pos_rel[r], msg):
            msg[r-1] = "1"
        else:
            msg[r-1] = "0"
    
    msg.reverse()
    msg = "".join(msg)
    print(f"Message Transmitted : {msg}")



def HamDecode (dataword : str):
    r_bits = find_redundant_bits_decode(len(dataword))
    total_bits = len(dataword)
    
    r_pos = get_r_pos(total_bits)
    r_pos_rel = get_r_pos_rel(r_pos, total_bits)
    
    msg = list(dataword)
    msg.reverse()
    
    correct = []
    for r in r_pos_rel:
        if redundant_filler(r_pos_rel[r], msg):
            correct.append("1")
        else : 
            correct.append("0")
    
    correct = correct[::-1]
    correct = binary_to_int("".join(correct))
    
    if correct : 
        print(f"The bit at {correct} st/nd/rd/th is corrupted")
        if msg[correct-1] == "0":
            msg[correct-1] = "1"
        else:
            msg[correct-1] = "0"
        msg.reverse()
        msg = "".join(msg)
        print(f"Message after Correction : {msg}")
    else:
        print(f"Message Successfully Transmitted")
    
    return 


# driver code
if __name__ == "__main__":
    print("SENDER's side:")
    dataword = input("Enter the Dataword : ").strip()
    # dataword = "10011011100"
    HamEncode(dataword)
    print("RECIVER's side:")
    data_rec = input("Enter the Dataword recieved : ").strip()    
    # data_rec  = "100110101100000"
    HamDecode(data_rec) 
```
```console
SENDER's side:
Enter the Dataword : 10011011100
Message Transmitted : 100110101100000

RECIVER's side:
Enter the Dataword recieved : 100110101100000
Message Successfully Transmitted
```
```console
SENDER's side:
Enter the Dataword : 10011011100
Message Transmitted : 100110101100000

RECIVER's side:
Enter the Dataword recieved : 10110111100000
The bit at 9 st/nd/rd/th is corrupted
Message after Correction : 10110011100000
```
