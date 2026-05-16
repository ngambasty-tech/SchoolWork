# Assignment: Hamming [15,11] Decoding

def hamming_15_11_decode(received):
    """Decodes a 15-bit vector using Hamming [15,11] logic."""
    
    # Create the parity-check matrix H with columns 1 to 15 in binary
    H = []
    for col_num in range(1, 16):
        bits = [(col_num >> i) & 1 for i in range(3, -1, -1)]
        H.append(bits)
    
    # Transpose H for matrix multiplication
    H_T = list(zip(*H))
    
    # Calculate syndrome by multiplying received vector with H_T (mod 2)
    syndrome = []
    for row in H_T:
        dot_product = sum(received[i] * row[i] for i in range(15))
        syndrome.append(dot_product % 2)
    
    # Convert syndrome bits to decimal to find error position
    error_pos = 0
    for bit in syndrome:
        error_pos = (error_pos << 1) | bit
    
    corrected = received[:]
    
    if error_pos == 0:
        print("[Status] No error detected.")
    else:
        # Correct the bit at the identified position (0-indexed)
        idx = error_pos - 1
        corrected[idx] ^= 1
        print(f"[Status] Error corrected at position {error_pos}")
    
    # Extract the original 11-bit message
    message = corrected[:11]
    return corrected, message

def main():
    # Test vector from exercise
    received_data = [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0]
    
    print("Hamming Decoder")
    corrected, message = hamming_15_11_decode(received_data)
    
    print(f"\nCorrected Codeword: {corrected}")
    print(f"Original Message: {message}")

if __name__ == "__main__":
    main()