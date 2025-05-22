import json
import os

# File to store library data
FILE_NAME = "library.txt"

# Load library from file
def load_library():
    if os.path.exists(FILE_NAME):
        if os.path.getsize(FILE_NAME) == 0:
            return []
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return []

# Save library to file
def save_library(library):
    with open(FILE_NAME, 'w') as f:
        json.dump(library, f, indent=4)

# Format book details for display
def format_book(book, index=None):
    status = "Read" if book["read"] else "Unread"
    prefix = f"{index+1}. " if index is not None else ""
    return f'{prefix}{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {status}'

# Add a book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    try:
        year = int(input("Enter the publication year: ").strip())
    except ValueError:
        print("Invalid year. Book not added.")
        return
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = read_input == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("✅ Book added successfully!")

# Remove a book by title
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found.")

# Search books
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    query = input("Enter the search term: ").strip().lower()
    matches = []
    for book in library:
        if (choice == "1" and query in book["title"].lower()) or \
           (choice == "2" and query in book["author"].lower()):
            matches.append(book)

    if matches:
        print("📚 Matching Books:")
        for i, book in enumerate(matches):
            print(format_book(book, i))
    else:
        print("❌ No matching books found.")

# Display all books
def display_all_books(library):
    if not library:
        print("📭 Your library is empty.")
    else:
        print("📚 Your Library:")
        for i, book in enumerate(library):
            print(format_book(book, i))

# Display statistics
def display_stats(library):
    total = len(library)
    if total == 0:
        print("📊 Total books: 0\n📘 Percentage read: 0.0%")
        return
    read_count = sum(1 for book in library if book["read"])
    percent = (read_count / total) * 100
    print(f"📊 Total books: {total}\n📘 Percentage read: {percent:.1f}%")

# Menu
def main():
    library = load_library()
    while True:
        print("\n📚 Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            save_library(library)
            print("📁 Library saved to file. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
