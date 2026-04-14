import os, zlib

def evaluate_compression_ratio(file_path):
    if not os.path.exists(file_path):
        return
    
    with open(file_path, 'rb') as f:
        data = f.read()
  
    compressed = zlib.compress(data)
    
    print(f"--- CAPACITY REPORT: {os.path.basename(file_path)} ---")
    print(f"Original Size: {len(data)} bytes")
    print(f"Compressed Size: {len(compressed)} bytes")
    print("--- BINARY SNAPSHOT (HEX) ---")
    print(compressed.hex())
    print("--- END REPORT ---")
evaluate_compression_ratio("/home/node/.openclaw/workspace/USER.md")
