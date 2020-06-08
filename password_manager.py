import sqlite3 


def create_password():
    website = input("What is the website that you have made a password for?>")
    website_username = input("What is the username for the website you are making a password for?>")
    website_password = input("What is the password for the website you are making?>")
    c.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
          (website, website_username, website_password))

def find_password():
    website_name = input("What is the website's name for which you need a password>")
    c.execute("SELECT * FROM passwords")
    data = c.fetchall()
    for row in data:
        if row[0] == website_name:
            print(row[2])
            break 
    # print(f"The username to the website is '{data[1]}'")
    # print(f"The password to the website is '{data[2]}'")

def main():
    go_on = True
    while go_on:
        direction_question = input("This is your password manager. Press 1 to create a new pasword, Press 2 to search for a password, or Press 3 to exit the program>")
        if direction_question.lower() == "1":
            create_password()
        if direction_question.lower() == "2":
            find_password()
        if direction_question.lower() == "3":
            go_on = False
    if go_on == False:
        db.commit()
        db.close()

if __name__ == "__main__":
    db = sqlite3.connect('password.db')
    c = db.cursor()
    #This is the code to create the table
        # c.execute("""CREATE TABLE passwords (
        #                 website blob,
        #                 username blob,
        #                 password blob
        #                 )""")
    main()
