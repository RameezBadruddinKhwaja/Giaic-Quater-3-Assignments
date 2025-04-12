import re
import streamlit as st

# Function to check password strength

def check_password_strength(password):
    """
    Evaluates the strength of a given password based on:
    - Length >= 8
    - Contains uppercase letter
    - Contains lowercase letter
    - Contains digit
    - Contains special character
    Returns a tuple: (score, feedback_list)
    """

    
    common_passwords = ["password", "password123", "123456", "qwerty"]

    # If password is in a known weak list
    if password.lower() in common_passwords:
        return 0, ["This password is very common and easily guessable."]

    score = 0
    feedback_list = []

    # 1) Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback_list.append("Use at least 8 characters.")

    # 2) Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback_list.append("Add at least one uppercase letter.")

    # 3) Check lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback_list.append("Add at least one lowercase letter.")

    # 4) Check digit
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback_list.append("Add at least one digit (0-9).")

    # 5) Check special character
    # You can expand this to more symbols as needed
    if re.search(r"[\W_]", password):
        # \W matches any non-word character (including special chars),
        
        score += 1
    else:
        feedback_list.append("Include at least one special character (!@#$%^&* etc.).")

    return score, feedback_list


# Streamlit App

def main():
    st.title("Password Strength Meter")
    st.write("Analyze your password and get suggestions for improvement.")

    # Input field for the password
    password = st.text_input("Enter your password", type="password")

    if st.button("Check Strength"):
        if password:
            score, feedback_list = check_password_strength(password)

            # Determine overall strength category
            if score <= 2:
                strength_label = "Weak"
            elif score in [3, 4]:
                strength_label = "Moderate"
            else:
                strength_label = "Strong"

            # Display the result
            st.markdown(f"**Score:** {score} / 5")
            st.markdown(f"**Strength:** {strength_label}")

            # Provide feedback
            if strength_label == "Strong":
                st.success("Your password is strong! Great job.")
            else:
                st.warning("Your password could be improved. See suggestions below:")
                for feedback_item in feedback_list:
                    st.write(f"- {feedback_item}")
        else:
            st.error("Please enter a password to check.")

    
    if st.button("Generate a secure password"):
        import random
        import string

        
        chars = string.ascii_letters + string.digits + "!@#$%^&*()_-+="
        generated_password = "".join(random.choice(chars) for _ in range(12))
        st.info(f"Generated Password: {generated_password}")
        st.write("Copy it and check its strength above!")

if __name__ == "__main__":
    main()
