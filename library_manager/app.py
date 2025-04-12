import streamlit as st

# Initialize the library in session state if it doesn't exist
if "library" not in st.session_state:
    st.session_state.library = []

# ----- Functions for Each Feature -----
def add_book():
    st.header("Add a Book")
    with st.form(key="add_book_form"):
        title = st.text_input("Title")
        author = st.text_input("Author")
        year = st.number_input("Publication Year", min_value=0, step=1)
        genre = st.text_input("Genre")
        read = st.checkbox("Have you read this book?")
        submit = st.form_submit_button("Add Book")
        if submit:
            book = {
                "title": title,
                "author": author,
                "year": int(year),
                "genre": genre,
                "read": read
            }
            st.session_state.library.append(book)
            st.success("Book added successfully!")

def remove_book():
    st.header("Remove a Book")
    if st.session_state.library:
        titles = [book["title"] for book in st.session_state.library]
        book_to_remove = st.selectbox("Select a book to remove", titles)
        if st.button("Remove Book"):
            st.session_state.library = [
                book for book in st.session_state.library 
                if book["title"] != book_to_remove
            ]
            st.success("Book removed successfully!")
    else:
        st.info("Your library is empty.")

def search_book():
    st.header("Search for a Book")
    query = st.text_input("Enter title or author to search")
    if st.button("Search"):
        query_lower = query.lower()
        results = [
            book for book in st.session_state.library 
            if query_lower in book["title"].lower() or query_lower in book["author"].lower()
        ]
        if results:
            for idx, book in enumerate(results, start=1):
                status = "Read" if book["read"] else "Unread"
                st.write(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        else:
            st.warning("No matching books found.")

def display_books():
    st.header("All Books in Your Library")
    if st.session_state.library:
        for idx, book in enumerate(st.session_state.library, start=1):
            status = "Read" if book["read"] else "Unread"
            st.write(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        st.info("Your library is empty.")

def display_stats():
    st.header("Library Statistics")
    total = len(st.session_state.library)
    if total > 0:
        read_count = sum(1 for book in st.session_state.library if book["read"])
        percentage_read = (read_count / total) * 100
        st.write(f"Total books: {total}")
        st.write(f"Percentage read: {percentage_read:.1f}%")
    else:
        st.info("Your library is empty.")

# ----- Sidebar Menu -----
st.sidebar.title("Menu")
option = st.sidebar.radio("Select an action:", 
                          ("Add Book", "Remove Book", "Search Book", "Display Books", "Statistics"))

st.title("Personal Library Manager")

# Render the page based on the sidebar selection
if option == "Add Book":
    add_book()
elif option == "Remove Book":
    remove_book()
elif option == "Search Book":
    search_book()
elif option == "Display Books":
    display_books()
elif option == "Statistics":
    display_stats()
