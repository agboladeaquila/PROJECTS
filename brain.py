import json
import csv 
memory_file="memory.json"
def load_memory():
    try: 
        with open(memory_file, "r") as f:
            return json.load(f)
    except:
        return{}
def save_memory(memory):
    with open(memory_file, "w") as f:
        json.dump(memory, f, indent=4)
        