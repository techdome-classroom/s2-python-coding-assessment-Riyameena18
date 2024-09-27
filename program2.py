class Solution(object):
   class Solution(object):
   def roman_to_int(s: str) -> int:
    # Mapping of Roman numerals to their integer values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    
    for char in reversed(s):
        current_value = roman_values[char]
        
        # If the current value is less than the previous value, subtract it
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        prev_value = current_value  # Update the previous value
    
    return total

# Get user input
user_input = input("Enter a Roman numeral: ")
result = roman_to_int(user_input)
print(f"The integer value of the Roman numeral {user_input} is {result}.")



