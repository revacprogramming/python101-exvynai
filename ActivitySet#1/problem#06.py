# Loops & Iterators

nums = list()
while True:
    command = input("Enter a number: ")
    if command == "done":
        break
    try:
        nums.append(int(command))
    except:
        print("Invalid input")

print("Maximum is", max(nums))
print("Minimum is", min(nums))
