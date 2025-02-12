import sqlite3

class UserAccountSystem:
    def _init_(self, db_name="users.db"):
        # Connect to SQLite database (or create it if it doesn't exist)
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        # Create users table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT,
                email TEXT
            )
        ''')
        self.conn.commit()

    def create_account(self, username, password, email):
        # Insert a new user account into the database
        try:
            self.cursor.execute('''
                INSERT INTO users (username, password, email) 
                VALUES (?, ?, ?)
            ''', (username, password, email))
            self.conn.commit()
            print(f"Account created for {username}.")
        except sqlite3.IntegrityError:
            print("Username already exists. Please choose a different one.")

    def read_account(self, username):
        # Retrieve user data by username
        self.cursor.execute('''
            SELECT username, email FROM users WHERE username = ?
        ''', (username,))
        user = self.cursor.fetchone()

        if user:
            print(f"User: {user[0]}")
            print(f"Email: {user[1]}")
        else:
            print(f"Account for {username} does not exist.")

    def update_account(self, username, new_password=None, new_email=None):
        # Update password or email for the given username
        if new_password:
            self.cursor.execute('''
                UPDATE users SET password = ? WHERE username = ?
            ''', (new_password, username))
        if new_email:
            self.cursor.execute('''
                UPDATE users SET email = ? WHERE username = ?
            ''', (new_email, username))

        self.conn.commit()
        print(f"Account for {username} updated.")

    def delete_account(self, username):
        # Delete user account from the database
        self.cursor.execute('''
            DELETE FROM users WHERE username = ?
        ''', (username,))
        self.conn.commit()
        print(f"Account for {username} deleted.")

    def close(self):
        # Close the database connection
        self.conn.close()

def main():
    system = UserAccountSystem()

    while True:
        print("\nUser Account System Menu:")
        print("1. Create Account")
        print("2. Read Account")
        print("3. Update Account")
        print("4. Delete Account")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            system.create_account(username, password, email)

        elif choice == '2':
            username = input("Enter username to read: ")
            system.read_account(username)

        elif choice == '3':
            username = input("Enter username to update: ")
            new_password = input("Enter new password (leave blank to keep the same): ")
            new_email = input("Enter new email (leave blank to keep the same): ")

            if not new_password:
                new_password = None
            if not new_email:
                new_email = None

            system.update_account(username, new_password, new_email)

        elif choice == '4':
            username = input("Enter username to delete: ")
            system.delete_account(username)

        elif choice == '5':
            print("Exiting the User Account System.")
            system.close()
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
