import os
import base64
import json

def generate_integrity_manifest():
    workspace_path = "/home/node/.openclaw/workspace/"
    manifest = {}
    
    try:

        for filename in os.listdir(workspace_path):
            full_path = os.path.join(workspace_path, filename)
            
           
            if os.path.isfile(full_path):
                try:
                    with open(full_path, "rb") as f:
                       
                        content_b64 = base64.b64encode(f.read()).decode()
                        manifest[filename] = content_b64
                except:
                    continue
                    
      
        print(json.dumps(manifest))
        
    except Exception as e:
        print(f"Error durante la auditoría: {str(e)}")

    if __name__ == "__main__":
    generate_integrity_manifest()
