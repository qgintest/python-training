def strength(password):
    has_length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)

    if has_length and has_upper and has_digit:
        return "Strong Password"
    return "Weak Password"

# Example usage
print(strength('abD12388'))
