def is_palindrome(text):
    """
    Return True if text is a palindrome.
    Ignores spaces and capitalization.
    """
    # make everything lowercase
    text = text.lower()
    # remove spaces
    text = text.replace(" ", "")
    # reverse the string
    reversed_text = text[::-1]
    # check if it matches
    return text == reversed_text

def is_palindrome_number(num):
    """
    Check if a number is a palindrome.
    """
    num_str = str(num)
    return num_str == num_str[::-1]

def palindrome_message(text):
    """
    Return a friendly message instead of just True/False.
    """
    if is_palindrome(text):
        return "Yes, it's a palindrome!"
    else:
        return "No, not a palindrome."

# Bonus: works on lists too
def is_palindrome_list(lst):
    """
    Check if a list is a palindrome.
    """
    return lst == lst[::-1]

# Demo code to try things out
if __name__ == "__main__":
    # test some strings
    print(is_palindrome("racecar"))   # True
    print(is_palindrome("hello"))     # False
    print(is_palindrome("A man a plan a canal Panama"))  # True

    # test numbers
    print(is_palindrome_number(121))     # True
    print(is_palindrome_number(123))     # False

    # test message
    print(palindrome_message("racecar"))
    print(palindrome_message("python"))

    # test lists
    print(is_palindrome_list([1, 2, 3, 2, 1]))   # True
    print(is_palindrome_list([1, 2, 3, 4]))      # False