import streamlit as st

# Yeh main function hai jo app ke pages handle karta hai.
def main():
    st.sidebar.title("Navigation")
    # Yeh sidebar se page select karne ka code hai.
    page = st.sidebar.radio("Page chunain:", ["Home", "Info", "Challenge", "Video"])
    
    if page == "Home":
        show_home()
    elif page == "Info":
        show_info()
    elif page == "Challenge":
        show_challenge()
    elif page == "Video":
        show_video()

# Home page display karne wala function.
def show_home():
    st.title("Growth Mindset Challenge")
    st.write("Aapka swagat hai! Growth mindset aik aisi soch hai jisse aap mehnat se tarakki kar sakte hain.")
    st.write("Sidebar se dusre pages chunain aur mazeed maloomat hasil karein.")

# Growth mindset ke bare mein maloomat dene wala function.
def show_info():
    st.header("Growth Mindset Kya Hai?")
    st.markdown("""
    **Growth Mindset:**  
    Aap ke andar ke potential ko barhana, challenges ko gale lagana aur galtiyon se seekhna.  
    Mehnat aur lagan se aap apni skills ko nikharsakte hain.
    """)
    st.write("Is se aap har mushkil ka muqabla kar sakte hain aur apni zindagi mein behtari la sakte hain.")

# Interactive section jahan user apna self-rating aur goal set karta hai.
def show_challenge():
    st.header("Interactive Challenge")
    rating = st.slider("1 se 10 tak, aap kitne growth mindset walay hain?", 1, 10, 5)
    st.write("Aapka rating hai:", rating)
    if rating < 5:
        st.warning("Abhi aur behtar banne ki gunjaish hai. Mehnat karein!")
    else:
        st.success("Shabash! Aap progress par hain.")
    
    goal = st.text_input("Aaj ka learning goal likhain:")
    if st.button("Goal Set Karein"):
        if goal:
            st.info("Aapka goal hai: " + goal)
        else:
            st.error("Meherbani karke goal likhain.")

# Video page jahan inspiration video ka link diya gaya hai.
def show_video():
    st.header("Inspiration Video")
    st.write("Dekhein: [The Best Way to Build Python Apps?](https://www.youtube.com/watch?v=rM-jDeSgOQw&list=PLEpRcxOmTFlMdi3TxjoM4qXh_AN4a5XN4)")
    st.write("Video dekhein, phir UV aur Streamlit se apna app banain aur publish karein.")

# App ko run karne wala code.
if __name__ == "__main__":
    main()
