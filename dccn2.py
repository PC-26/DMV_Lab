def xor(a, b):
  
    return "".join('0' if a[i] == b[i] else '1' for i in range(1, len(b)))

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]
    
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1

    
    return xor(divisor, tmp) if tmp[0] == '1' else xor('0' * pick, tmp)


input_bits = "1011001" 
generator = "1101"      

padded_data = input_bits + '0' * (len(generator) - 1)
remainder = mod2div(padded_data, generator)
sent_data = input_bits + remainder
print(f"Sender: Sent Code = {sent_data} (Remainder: {remainder})")

check = mod2div(sent_data, generator)
if '1' not in check:
    print("Receiver: No Error Detected")
else:
    print("Receiver: Error Detected")