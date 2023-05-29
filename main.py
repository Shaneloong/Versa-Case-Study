import json

# Initialize an empty array
result_array = []

# Loop through 1 to 100
for i in range(1, 101):
    # Check if the number is divisible by 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        result_array.append("BIGBANG")
    # Check if the number is divisible by 3
    elif i % 3 == 0:
        result_array.append("BIG")
    # Check if the number is divisible by 5
    elif i % 5 == 0:
        result_array.append("BANG")
    # If the number is not divisible by 3 or 5, append the number itself
    else:
        result_array.append(i)

# Write the result array to a json file
with open('output.json', 'w') as file_handler:
    json.dump(result_array, file_handler)
print(result_array)
