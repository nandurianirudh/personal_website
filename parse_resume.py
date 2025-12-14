import re

def parse_resume():
    try:
        with open('resume_text.txt', 'r', encoding='utf-16') as f:
            text = f.read()
        
        # Normalize newlines
        lines = text.split('\n')
        
        capturing = False
        captured_text = []
        
        print("--- EXTRACTED RESUME SECTIONS ---")
        
        for line in lines:
            line = line.strip()
            if not line: continue
            
            # Simple keyword check to find relevant areas
            if "Accenture" in line or "BRIDGEi2i" in line or "Experience" in line or "Work" in line or "Professional" in line:
                print(f"\n[KEYWORD FOUND]: {line}")
                capturing = True
            
            if capturing:
                print(line)
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parse_resume()
