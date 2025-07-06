def analyze_password_strength(password):
    """
    Analyze password strength and return score (1-5) and feedback
    """
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 12:
        score += 2  # Excellent length
    elif len(password) >= 8:
        score += 1  # Good length
    else:
        feedback.append("Consider making it longer (8+ characters recommended)")
    
    # Check for uppercase letters
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    
    # Check for lowercase letters
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
    # Check for numbers
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers")
    
    # Check for special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in special_chars for c in password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$%^&* etc.)")
    
    # Check for common weak patterns
    weak_patterns = ["123", "abc", "password", "qwerty", "letmein", "admin"]
    password_lower = password.lower()
    
    for pattern in weak_patterns:
        if pattern in password_lower:
            score = max(1, score - 1)  # Reduce score but keep minimum of 1
            feedback.append(f"Avoid common patterns like '{pattern}'")
            break
    
    # Ensure score is between 1 and 5
    score = max(1, min(5, score))
    
    return score, feedback

def estimate_crack_time(password):
    """
    Rough estimate of crack time (very simplified)
    """
    import math
    
    # Character set sizes
    char_sets = 0
    if any(c.islower() for c in password):
        char_sets += 26
    if any(c.isupper() for c in password):
        char_sets += 26
    if any(c.isdigit() for c in password):
        char_sets += 10
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        char_sets += 22
    
    # Total possible combinations
    total_combinations = char_sets ** len(password)
    
    # Assume 1 billion attempts per second
    attempts_per_second = 1_000_000_000
    
    # Average time to crack (half of all combinations)
    seconds_to_crack = total_combinations / (2 * attempts_per_second)
    
    # Convert to human readable format
    if seconds_to_crack < 60:
        return f"{seconds_to_crack:.1f} seconds"
    elif seconds_to_crack < 3600:
        return f"{seconds_to_crack/60:.1f} minutes"
    elif seconds_to_crack < 86400:
        return f"{seconds_to_crack/3600:.1f} hours"
    elif seconds_to_crack < 31536000:
        return f"{seconds_to_crack/86400:.1f} days"
    else:
        return f"{seconds_to_crack/31536000:.1f} years"

def main():
    print("Password Strength Analyzer")
    print("=" * 30)
    
    password = input("Enter a password to analyze: ")
    score, feedback = analyze_password_strength(password)
    
    strength_levels = {
        1: "Very Weak",
        2: "Weak", 
        3: "Fair",
        4: "Strong",
        5: "Very Strong"
    }
    
    print(f"\nPassword: {'*' * len(password)}")  # Hide actual password
    print(f"Strength: {score}/5 ({strength_levels[score]})")
    
    if feedback:
        print("\nFeedback:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("\nGreat password! No improvements needed.")
    
    # Bonus: Show estimated crack time
    crack_time = estimate_crack_time(password)
    print(f"\nEstimated crack time: {crack_time}")
    print("(This is a very rough estimate for educational purposes)")

if __name__ == "__main__":
    main()