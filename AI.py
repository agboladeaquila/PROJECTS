from brain import load_memory, save_memory
memory = load_memory()
while True:
    question=input("you;").lower()
    if question in memory:
        print("AI",memory[question])
    else: 
        print("AI: I don't know yet.")
        