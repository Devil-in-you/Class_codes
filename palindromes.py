def is_palindrome(number):
    # Convert the number to a string
    number_str = str(number)
    
    return number_str == number_str[::-1]

def find_palindromes_in_range(start, end):
    palindromes = []
    #will be adding in the list given above
    for num in range(start, end + 1):
        if is_palindrome(num):
            palindromes.append(num)
    
    return palindromes

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

palindromes = find_palindromes_in_range(start, end)

if palindromes:
    print("Palindromic numbers in the range:", palindromes)
else:
    print("No palindromic numbers found in the given range.")
