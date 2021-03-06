#The Dependicies and Packages required for this script
import sqlite3 
from cryptography.fernet import Fernet


def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Loads the key named `secret.key` from the current directory.
    """
    return open("secret.key", "rb").read()


#These are the keys for encryption
key = load_key()
f = Fernet(key)


def decode_data(datas):
    new_name = f.decrypt(datas)
    final_name = new_name.decode()
    return final_name 


def create_password():
    """
    This function is used for gathering the user's data about the website, their username to that site, and their password. 
    This data in then encrypted using the key generated at lines 5 and 6.
    Finally, the data is pushed to the sql database using bind parameters so that there is no risk of sql injection attacks
    """

    #Each of these variables asks for a input which is then encoded into bytes so that it can be encrypted.
    #The user input is then encrypted using the keys generated on lines 5,6
    encrypted_website = f.encrypt(input("What is the website that you have made a password for?>").encode())
    encrypted_username = f.encrypt(input("What is the username for the website you are making a password for?>").encode())
    encrypted_password = f.encrypt(input("What is the password for the website you are making?>").encode())
    
    #This is the command which uses bind parameters to insert the encrypted data into the database. The type of data being inserted is a blob
    c.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
          (encrypted_website, encrypted_username, encrypted_password))


def find_password():
    """
    This function is to get the password of the website that the user expected
    """
    website_name = input("What is the website's name for which you need a password>")
    c.execute("SELECT * FROM passwords")
    data = c.fetchall()
    for row in data:
        print(row[0])
        name = decode_data(row[0])
        if name == website_name:
            password = decode_data(row[2])
            print(f'The password to {website_name} is {password}')


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
        else:
            print("Invalid response")
    db.commit()
    db.close()


if __name__ == "__main__":
    db = sqlite3.connect('password.db')
    c = db.cursor()
    # generate_key()
    #This is the code to create the table
        # c.execute("""CREATE TABLE passwords (
        #                 website blob,
        #                 username blob,
        #                 password blob
        #                 )""")
    main()
