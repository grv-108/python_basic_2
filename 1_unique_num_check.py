# 1. Unique Numbers Check

# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

def getUserInput():
    return input("Enter number saperated by , --> ").strip()

def unique_num_check(user_input):
    user_input = user_input.split(",")
    if len(user_input) == len(set(user_input)):
        return True
    else:
        return False
    
def main():
    user_input = getUserInput()
    result = unique_num_check(user_input)
    print(f"Are Numbers unique : {result}")
    
if __name__ == "__main__":
    main()