import json
import random
import string
import sys

options = {
    "-h": "is showing every options",
    "-rpass": "is creating random password",
    "-restp": "you can change password",
    "-deluser": "is removing your account",
    "-end": "is ending proses"
}

print("Welcome in program")

print("Do you have account(Y/N): ")
register = input(">>>")

if register == "N":
    print("Type your name: ")
    username = input(">>>")
    print("Type your password: ")
    password = input(">>>")
    print("Type your phone number: ")
    phone_number = input(">>>")

    information = {
        "username": username,
        "password": password,
        "phone_number": phone_number
    }

    len_username = len(username)
    len_password = len(password)
    len_phone = len(phone_number)

    if len_username == 0:
        print("Wrong user name")
        sys.exit(1)
    json_object = json.dumps(information, indent=4)

    with open("UserPass.json", "w") as outfile:
        outfile.write(json_object)
elif register == "Y":
    with open('UserPass.json', 'r') as openfile:
        json_object = json.load(openfile)

        print("Type your name: ")
        username = input(">>>")
        print("Type your password: ")
        password = input(">>>")
        if username and password == json_object["username" and "password"]:
            print("Ok everything went good")
            print("")
            for x, y in options.items():
                print(x, y)
            while True:
                options_quest = input(">>>")

                if options_quest == "-h":
                    for x, y in options.items():
                        print(x, y)
                if options_quest == "-rpass":

                    num = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
                    special_let = ("{", "}", "[", "]", "(", ")", "'", "#", "|", "*", "<", ">")


                    def random_pass():
                        print("How many letters you want: ")
                        ask_len_pass_let = input(">>>")
                        print("How many numbers you want: ")
                        ask_len_pass_num = input(">>>")
                        print("How many special characters you want: ")
                        ask_len_pass_spec = input(">>>")

                        try:
                            ran = ''.join(random.choice(string.ascii_letters) for x in range(int(ask_len_pass_let)))
                            ran += ''.join(random.choice(num) for x in range(int(ask_len_pass_num)))
                            ran += ''.join(random.choice(special_let) for x in range(int(ask_len_pass_spec)))
                            to_string = list(ran)

                            random.shuffle(to_string)

                            final_pass = ''.join(to_string)

                            return final_pass
                        except:
                            print("You must write number")
                            sys.exit(1)


                    print("Your password is: ", random_pass())
                if options_quest == "-deluser":
                    print("In process of working")

                if options_quest == "-restp":
                    print("Are you sure you want change password(Y/N)")
                    change_password_new = input(">>>")
                    if change_password_new == "Y":
                        print("Type your name: ")
                        username = input(">>>")
                        print("Type your phone number: ")
                        phone_number = input(">>>")

                        information = {
                            "username": username,
                            "password": password,
                            "phone_number": phone_number
                        }

                        if username and phone_number == json_object["username" and "phone_number"]:
                            print("Type new password: ")
                            change_password_new = input(">>>")
                            json_object["password"] = change_password_new
                            password = change_password_new

                            outfile = open("UserPass.json", "w")
                            json.dump(json_object, outfile)
                            json_object = json.dumps(information, indent=3)
                            outfile.close()

                if options_quest == "-end":
                    sys.exit(1)

        else:
            print("Something gone wrong")
            print("If you don't remember password you can change it(Y/N)")
            change_password = input(">>>")
            if change_password == "Y":
                print("Type your name: ")
                username = input(">>>")
                print("Type your phone number: ")
                phone_number = input(">>>")
                if username and phone_number == json_object["username" and "phone_number"]:

                    with open('UserPass.json', 'r') as openfile:
                        json_object = json.load(openfile)

                    if username and phone_number == json_object["username" and "phone_number"]:
                        print("Type new password: ")
                        change_password_new = input(">>>")
                        password = change_password_new
                        json_object["password"] = change_password_new

                        information = {
                            "username": username,
                            "password": password,
                            "phone_number": phone_number
                        }

                        outfile = open("UserPass.json", "w")
                        json.dump(json_object, outfile)
                        json_object = json.dumps(information, indent=3)
                        outfile.close()

            else:
                print("Something gone wrong")
else:
    print("Something gone wrong")
