def palindrome(p_input):
    p_input = p_input.upper()
    rev_input = p_input[::-1]
    if p_input == rev_input:
        print("This is a palindrome")
        return True
    else:
        print("This is not a palindrome")
        return False

palindrome("Madam")
