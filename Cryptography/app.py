import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# ---------- Global Variables & Initialization ----------
# Generate a key (in production, store securely)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)
# In-memory data storage: each entry stored as a dictionary.
# Format: { "encrypted_text": {"encrypted_text": "...", "passkey": "hashed_passkey"} }
stored_data = {}
failed_attempts = 0  # Global counter for decryption failures

# ---------- Utility Functions ----------
def hash_passkey(passkey):
    """Return SHA-256 hash of the passkey."""
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text):
    """Encrypt the text using the Fernet cipher."""
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, passkey):
    """
    Decrypt data only if the provided passkey (after hashing) matches the stored passkey.
    Increase failed_attempts on failure.
    """
    global failed_attempts
    provided_hash = hash_passkey(passkey)

    # Retrieve the stored entry using encrypted_text as key.
    entry = stored_data.get(encrypted_text)
    if entry and entry["passkey"] == provided_hash:
        # Reset counter upon success.
        failed_attempts = 0
        try:
            return cipher.decrypt(encrypted_text.encode()).decode()
        except Exception:
            return None
    else:
        failed_attempts += 1
        return None

# ---------- Streamlit UI & Pages ----------
st.title("🛡️ Secure Data Encryption System")

# Sidebar menu for navigation
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

# HOME PAGE
if choice == "Home":
    st.subheader("Welcome!")
    st.write("Store and retrieve your data securely using a unique passkey.")
    st.write("Choose an option from the sidebar to begin.")

# STORE DATA PAGE
elif choice == "Store Data":
    st.subheader("Store Data")
    text_to_store = st.text_area("Enter the data you want to secure:")
    passkey_input = st.text_input("Enter a unique passkey:", type="password")
    
    if st.button("Encrypt & Save"):
        if text_to_store and passkey_input:
            # Encrypt the data and hash the passkey before storing.
            encrypted_text = encrypt_data(text_to_store)
            hashed_key = hash_passkey(passkey_input)
            stored_data[encrypted_text] = {"encrypted_text": encrypted_text, "passkey": hashed_key}
            st.success("✅ Data stored securely!")
            st.info(f"Your encrypted data is:\n\n`{encrypted_text}`")
        else:
            st.error("⚠️ Please provide both data and a passkey.")

# RETRIEVE DATA PAGE
elif choice == "Retrieve Data":
    st.subheader("Retrieve Data")
    
    # If too many failed attempts, force reauthorization.
    if failed_attempts >= 3:
        st.warning("❗ Too many failed attempts! Please use the Login page to reauthorize.")
    else:
        input_encrypted = st.text_area("Paste your encrypted data:")
        passkey_attempt = st.text_input("Enter your passkey:", type="password")
        
        if st.button("Decrypt"):
            if input_encrypted and passkey_attempt:
                result = decrypt_data(input_encrypted, passkey_attempt)
                if result is not None:
                    st.success(f"✅ Decrypted Data: {result}")
                else:
                    remaining = max(0, 3 - failed_attempts)
                    st.error(f"❌ Incorrect passkey! Attempts remaining: {remaining}")
            else:
                st.error("⚠️ Both fields are required!")

# LOGIN PAGE (Reauthorization)
elif choice == "Login":
    st.subheader("Reauthorization Required")
    master_pass = st.text_input("Enter master password:", type="password")
    # For demonstration: the master password is hardcoded.
    if st.button("Login"):
        if master_pass == "admin123":
            failed_attempts = 0
            st.success("✅ Reauthorized successfully! You can now retry retrieving your data.")
        else:
            st.error("❌ Incorrect master password!")
