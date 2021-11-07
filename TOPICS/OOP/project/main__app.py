from Human import Human
import sqlite3  # to deal with database
import coloredText


# the main data base
db = sqlite3.connect("../database/mainDatabase.db")


def create_new_user():

    # connect to database
    cr = db.cursor()

    # create the user process
    user = Human()

    # insert the data into the database
    cr.execute(f"INSERT INTO users VALUES ({user.ID}, "
               f"'{user.firstName}', "
               f"'{user.middleName}', "
               f"'{user.lastName}', "
               f"'{user.phoneNumber}', "
               f"{user.get_nationalid()}, "
               f"'{user.gender}', "
               f"'{user.birthday}', "
               f"'{user.governorate}')")

    # save changes and close the database
    db.commit()
    print(coloredText.mk_green("created new user done"))


def show_one_user(userNationalID):
    # connect to database
    cr = db.cursor()

    cr.execute(f"select * from users where national_id = {userNationalID}")
    print(cr.fetchone())


def show_user_details(user):
    print(f"id: {user[0]}\n"
          f"name: {user[1]} {user[2]} {user[2]}\n"
          f"phoneNumber: {user[4]}\n"
          f"nationalID: {user[5]}\n"
          f"gender: {user[6]}\n"
          f"birthday: {user[7]}\n"
          f"governorate: {user[8]}\n-------------------")


def delete_user():

    cr = db.cursor()

    nationalId = int(input("enter id national id for the person you want to delete: "))

    if input("are you sure to delete? (y, n) ").lower() == 'y':

        cr.execute(f"delete from users where id = {nationalId}")
        db.commit()
        print(coloredText.mk_red("deleted user successfully"))

    else:
        print("nothing has happend")


def show_all_users():
    cr = db.cursor()
    cr.execute("select * from users")
    allUsers = cr.fetchall()

    for user in allUsers:
        show_user_details(user)

    db.commit()


def main__func():
    # the rules of the program
    theMessage = """
1. create user
2. show user
3. show all users
4. delete user
5. quite the program: 
"""

    # taking user input
    user_input = input(theMessage)

    # the whole operations
    while user_input != '5':

        if user_input == '1':
            create_new_user()

        elif user_input == '2':
            show_one_user(input("enter user national id : "))

        elif user_input == '3':
            show_all_users()

        elif user_input == '4':
            delete_user()

        else:
            print("wrong input")

        # take the input again to avoid infinite loop
        user_input = input(theMessage)


main__func()


