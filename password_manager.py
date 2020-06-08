import sqlite3 





def create_password():
    website = input("What is the website that you have made a password for?")
    website_username = input("What is the username for the website you are making a password for?")
    website_password = input("What is the password for the website you are making?")
    c.execute("INSERT INTO passwords (website, website_username, website_password) VALUES (?, ?, ?)",
          (website, website_username, website_password))
    db.commit()
    db.close()

def find_password():
    pass

def main():
    direction_question = input("This is your password manager. Press 1 to create a new pasword, Press 2 to search for a password, or Press 3 to exit the program")
    if direction_question.lower() == "1":
        create_password()
    if direction_question.lower() == "2":
        find_password()
    if direction_question.lower() == "3":
        print("u done")

if __name__ == "__main__":
    db = sqlite3.connect('password.db')
    c = db.cursor()
    main()
