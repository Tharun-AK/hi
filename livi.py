
from collections import deque

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.book_id} - {self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = {}  # hashmap to store books by ID
        self.recent_activity = []  # stack to store recent actions
        self.book_requests = deque()  # queue for book request handling

    # Add book to library
    def add_book(self, book: Book):
        if book.book_id in self.books:
            print("Book ID already exists!")
        else:
            self.books[book.book_id] = book
            self.recent_activity.append(f"Added: {book.title}")
            print(f"Book '{book.title}' added successfully.")

    # Remove a book
    def remove_book(self, book_id):
        if book_id in self.books:
            removed = self.books.pop(book_id)
            self.recent_activity.append(f"Removed: {removed.title}")
            print(f"Book '{removed.title}' removed successfully.")
        else:
            print("Book not found.")

    # Search book by ID (Binary Search simulation after sorting)
    def search_book(self, target_id):
        sorted_ids = sorted(self.books.keys())
        low, high = 0, len(sorted_ids) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_ids[mid] == target_id:
                book = self.books[target_id]
                print(f"Found: {book}")
                return book
            elif sorted_ids[mid] < target_id:
                low = mid + 1
            else:
                high = mid - 1
        print("Book not found.")
        return None

    # Sort books by title using simple Bubble Sort
    def sort_books_by_title(self):
        book_list = list(self.books.values())
        n = len(book_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if book_list[j].title > book_list[j + 1].title:
                    book_list[j], book_list[j + 1] = book_list[j + 1], book_list[j]
        print("Books sorted by title:")
        for b in book_list:
            print(b)

    # Request book
    def request_book(self, book_id):
        if book_id in self.books:
            self.book_requests.append(book_id)
            print(f"Book ID {book_id} added to request queue.")
        else:
            print("Book ID not found.")

    # Process next book request
    def process_next_request(self):
        if self.book_requests:
            book_id = self.book_requests.popleft()
            if book_id in self.books:
                book = self.books[book_id]
                print(f"Processing request: {book}")
                self.recent_activity.append(f"Requested: {book.title}")
            else:
                print("Book no longer available.")
        else:
            print("No book requests in queue.")

    # Show recent actions (stack)
    def show_recent_activity(self):
        print("Recent Activity (Last 5):")
        for action in reversed(self.recent_activity[-5:]):
            print(action)

    # List all books
    def list_all_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("All books in the library:")
        for book in self.books.values():
            print(book)

# Sample usage
def main():
    lib = Library()

    # Add some books
    lib.add_book(Book(1, "The Alchemist", "Paulo Coelho"))
    lib.add_book(Book(2, "1984", "George Orwell"))
    lib.add_book(Book(3, "To Kill a Mockingbird", "Harper Lee"))
    lib.add_book(Book(4, "Sapiens", "Yuval Noah Harari"))

    # List books
    lib.list_all_books()

    # Search for a book
    lib.search_book(2)

    # Sort books by title
    lib.sort_books_by_title()

    # Request a book
    lib.request_book(2)
    lib.request_book(3)

    # Process requests
    lib.process_next_request()
    lib.process_next_request()
    lib.process_next_request()

    # Show recent activity
    lib.show_recent_activity()

    # Remove a book
    lib.remove_book(4)

    # Show all again
    lib.list_all_books()
    lib.show_recent_activity()

if __name__ == "__main__":
    main()
