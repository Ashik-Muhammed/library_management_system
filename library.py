import tkinter as tk
from tkinter import messagebox


class LibraryManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("600x600")
        self.master.config(bg='#F0F0F0')

        self.books = []
        self.lend_list = []

        # Labels
        self.login_label = tk.Label(self.master, text="Library Management System", font=("Helvetica", 16),
                                    bg='#F0F0F0', fg='black')
        self.login_label.pack(pady=20)
        self.username_label = tk.Label(self.master, text="Username", font=("Helvetica", 12), bg='#F0F0F0', fg='black')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.username_entry.pack(pady=5)
        self.password_label = tk.Label(self.master, text="Password", font=("Helvetica", 12), bg='#F0F0F0', fg='black')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, font=("Helvetica", 12), show="*")
        self.password_entry.pack(pady=5)

        # Login
        self.login_button = tk.Button(self.master, text="Login", command=self.login, font=("Helvetica", 12))
        self.login_button.pack(pady=10)

        # Register
        self.register_button = tk.Button(self.master, text="Register", command=self.register, font=("Helvetica", 12))
        self.register_button.pack()

        self.username = ""
        self.password = ""
        self.librarians = []

    def login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        for librarian in self.librarians:
            if self.username == librarian[0] and self.password == librarian[1]:
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.login_label.destroy()
                self.username_label.destroy()
                self.username_entry.destroy()
                self.password_label.destroy()
                self.password_entry.destroy()
                self.login_button.destroy()
                self.register_button.destroy()
                self.library_management_screen()
                return
        messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.librarians.append([self.username, self.password])
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def library_management_screen(self):
        self.add_book_label = tk.Label(self.master, text="Add Book", font=("Helvetica", 16), bg='#F0F0F0', fg='black')
        self.add_book_label.pack(pady=20)
        self.add_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.add_book_entry.pack(pady=5)
        self.add_book_button = tk.Button(self.master, text="Add Book", command=self.add_book, font=("Helvetica", 12))
        self.add_book_button.pack()

        self.remove_book_label = tk.Label(self.master, text="Remove Book", font=("Helvetica", 16), bg='#F0F0F0',
                                          fg='black')
        self.remove_book_label.pack(pady=20)
        self.remove_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.remove_book_entry.pack(pady=5)
        self.remove_book_button = tk.Button(self.master, text="Remove Book", command=self.remove_book,
                                            font=("Helvetica", 12))
        self.remove_book_button.pack()

        self.issue_book_label = tk.Label(self.master, text="Issue Book", font=("Helvetica", 16), bg='#F0F0F0',
                                         fg='black')
        self.issue_book_label.pack(pady=20)
        self.issue_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.issue_book_entry.pack(pady=5)
        self.issue_book_button = tk.Button(self.master, text="Issue Book", command=self.issue_book,
                                           font=("Helvetica", 12))
        self.issue_book_button.pack()

        self.view_books_button = tk.Button(self.master, text="View Books", command=self.view_books,
                                           font=("Helvetica", 12))
        self.view_books_button.pack(pady=10)

    def add_book(self):
        book = self.add_book_entry.get()
        if book:
            self.books.append(book)
            messagebox.showinfo("Success", "Book added successfully")
            self.add_book_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a book title")

    def remove_book(self):
        book = self.remove_book_entry.get()
        if book in self.books:
            self.books.remove(book)
            messagebox.showinfo("Success", "Book removed successfully")
        else:
            messagebox.showerror("Error", "Book not found")
        self.remove_book_entry.delete(0, tk.END)

    def issue_book(self):
        book = self.issue_book_entry.get()
        if book in self.books:
            self.books.remove(book)
            messagebox.showinfo("Success", "Book issued successfully")
        else:
            messagebox.showerror("Error", "Book not found")
        self.issue_book_entry.delete(0, tk.END)

    def view_books(self):
        if self.books:
            message = "\n".join(self.books)
            messagebox.showinfo("Books", message)
        else:
            messagebox.showinfo("Books", "No books available")


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagement(root)
    root.mainloop()
