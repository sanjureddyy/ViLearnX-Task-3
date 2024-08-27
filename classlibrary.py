class LibraryItem:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.is_checked_out = False

    def __str__(self):
        status = "Checked out" if self.is_checked_out else "Available"
        return f"Title: {self.title}, Author: {self.author}, Category: {self.category}, Status: {status}"

class Book(LibraryItem):
    def __init__(self, title, author, isbn, category):
        super().__init__(title, author, category)
        self.isbn = isbn

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, ISBN: {self.isbn}"

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.checked_out_items = []
        self.fines = 0.0

    def check_out_item(self, item):
        if not item.is_checked_out:
            item.is_checked_out = True
            self.checked_out_items.append(item)
            print(f"Checked out: {item.title}")
        else:
            print(f"Item '{item.title}' is already checked out.")

    def return_item(self, item, days_overdue=0):
        if item in self.checked_out_items:
            item.is_checked_out = False
            self.checked_out_items.remove(item)
            self.calculate_fine(days_overdue)
            print(f"Returned: {item.title}")
        else:
            print(f"Item '{item.title}' was not checked out by {self.name}.")

    def calculate_fine(self, days_overdue):
        fine_rate = 0.50  # 50 cents per day overdue
        fine_amount = days_overdue * fine_rate
        self.fines += fine_amount
        if fine_amount > 0:
            print(f"Overdue fine for {days_overdue} days: ${fine_amount:.2f}")
        else:
            print("No overdue fines.")

    def __str__(self):
        return f"User: {self.name}, ID: {self.user_id}, Fines: ${self.fines:.2f}"

# Example Usage
if __name__ == "__main__":
    # Create some library items
    book1 = Book("1984", "George Orwell", "9780451524935", "Fiction")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", "Fiction")

    # Create a user
    user1 = User("Alice", "U001")

    # Display book information
    print(book1)
    print(book2)

    # User checks out a book
    user1.check_out_item(book1)

    # Try to check out the same book again
    user1.check_out_item(book1)

    # User returns the book with 3 days overdue
    user1.return_item(book1, days_overdue=3)

    # Display user information
    print(user1)

    # Display book information again
    print(book1)
