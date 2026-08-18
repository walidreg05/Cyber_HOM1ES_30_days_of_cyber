alphanum = "0123456789ABCDEF"
def decimal_to_hex(num):
    if num == 0:
        return "0"
    
    hex_str = ""
    is_negative = num < 0
    num = abs(num)
    
    while num > 0:
        rst = num % 16
        hex_str = alphanum[rst] + hex_str
        num = num // 16
        
    return f"-0x{hex_str}" if is_negative else f"0x{hex_str}"

# Example Usage
print(decimal_to_hex(255))   # Output: 0xFF
print(decimal_to_hex(4096))  # Output: 0x1000
