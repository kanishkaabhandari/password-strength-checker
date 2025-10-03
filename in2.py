import re

def assess_password_strength(password):
    """
    Assesses the strength of a password based on several criteria.

    Args:
        password (str): The password string to assess.

    Returns:
        tuple: A tuple containing (strength_score, feedback_messages).
               strength_score is an integer, feedback_messages is a list of strings.
    """
    score = 0
    feedback = []

    # Criteria 1: Length
    min_length = 8
    if len(password) >= min_length:
        score += 2
        feedback.append(f"✓ Good length ({len(password)} characters).")
    else:
        feedback.append(f"✗ Password is too short. Needs at least {min_length} characters.")

    # Criteria 2: Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("✓ Contains uppercase letters.")
    else:
        feedback.append("✗ Consider adding uppercase letters.")

    # Criteria 3: Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("✓ Contains lowercase letters.")
    else:
        feedback.append("✗ Consider adding lowercase letters.")

    # Criteria 4: Numbers
    if re.search(r"\d", password):
        score += 1
        feedback.append("✓ Contains numbers.")
    else:
        feedback.append("✗ Consider adding numbers.")

    # Criteria 5: Special characters
    # Using a regex pattern for common special characters
    special_chars_pattern = r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?`~]"
    if re.search(special_chars_pattern, password):
        score += 2 # Give more weight to special characters
        feedback.append("✓ Contains special characters.")
    else:
        feedback.append("✗ Consider adding special characters (e.g., !@#$%^&*).")

    return score, feedback

def provide_strength_level(score):
    """
    Determines the overall strength level based on the score.
    """
    if score >= 7:
        return "Very Strong"
    elif score >= 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

# --- Main program loop ---
if __name__ == "__main__":
    print("--- Password Strength Checker ---")
    print("Enter a password to check its strength. Type 'exit' to quit.")

    while True:
        user_password = input("\nEnter your password: ")

        if user_password.lower() == 'exit':
            print("Exiting password checker. Goodbye!")
            break

        if not user_password: # Handle empty input
            print("Password cannot be empty. Please enter a password.")
            continue

        strength_score, feedback_messages = assess_password_strength(user_password)
        overall_strength = provide_strength_level(strength_score)

        print("\n--- Assessment Results ---")
        print(f"Overall Strength: {overall_strength}")
        print("--- Feedback ---")
        for msg in feedback_messages:
            print(msg)
        print("--------------------------")