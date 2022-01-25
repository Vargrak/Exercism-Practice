def encode(numbers):
    VQ = []
    for number in numbers:
        #init list and format to binary (reversed for slicing)
        bits = []
        binary = format(int(f"{number}", 10), f'b')[::-1]
       
       #slicing
        bits = [f'{binary[i:i+7]}' for i in range(0, len(binary), 7)]
        bits.reverse()

        #un-reverses binary and appends MBS
        for index, chunk in enumerate(bits):
            bits[index] = chunk[::-1].zfill(7)
            if index != len(bits)-1:
                bits[index] = int(f'1{bits[index]}', 2)
            else:
                bits[index] = int(f'0{bits[index]}', 2)
        VQ.extend(bits)
    return VQ

def decode(bytes_):
    #init list, counter
    bits, former = [], 0

    #format to binary, slice MBS off, append binary sum to output list if MBS is 0
    for index, chunk in enumerate(bytes_):
        bytes_[index] = format(int(f'{chunk}', 10), f'08b')[1:8]
        if format(int(f'{chunk}', 10), f'08b')[0] == "0":
            bits.append(int(f"{''.join(bytes_[former:index+1])}", 2))
            former = index+1
    if len(bits) < 1:
        raise ValueError("incomplete sequence")
    return bits 