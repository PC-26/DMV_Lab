def get_7bit_checksum(segments):
    total_sum = 0
    
    mask = 0x7F 

    for seg in segments:
        total_sum += int(seg, 2)
        
        while total_sum > mask:
            total_sum = (total_sum & mask) + (total_sum >> 7)
            
    
    checksum = bin(~total_sum & mask)[2:].zfill(7)
    return checksum


data_segments = ["1011001", "0110101"]
chk = get_7bit_checksum(data_segments)
print(f"Sender Checksum: {chk}")


received = data_segments + [chk]

if int(get_7bit_checksum(received), 2) == 0:
    print("Receiver: No Error Detected")