import random

def main():
    prediction = number("Level: ")
    print(prediction)

def number(number_guess):
    trials = 5
    score = 0

    while True:
        try:
            level = int(input(number_guess))

            if level < 1 or level > 3:
                return "Level not available"

            if level == 1:
                generate = random.randint(1, 10)
            elif level == 2:
                generate = random.randint(1, 20)
            else:
                generate = random.randint(1, 50)

            lower = max(1, generate - 5)
            upper = generate + 5

            for attempt in range(trials):

                if attempt >= trials - 2:
                    print(f"Hint: number is between {lower} and {upper}")

                answer = int(input("Guess the number: "))

                if answer == generate:
                    if level == 1:
                        score += 5
                    elif level == 2:
                        score += 15
                    else:
                        score += 25

                    print("Correct!")
                    break
                else:
                    print("Wrong answer")

            else:
                print("All attempts were incorrect")
                print(f"Answer = {generate}")

        except EOFError:
            return f"Score = {score}"

if __name__ == "__main__":
    main()