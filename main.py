import json
import random
import string
import sys

options = {
    "-h" : "is showing every options",
    "-rpass" : "is creating random password",
    "-end" : "is ending proses"
}
print("Welcome in program")

register = input("Do you have account(Y/N): ")

if register == "N":
    username = input("Type your name: ")
    password = input("Type your password: ")
    phone_number = input("Type your phone number: ")
        
    information = {
        "username": username,
        "password": password,
        "phone_number": phone_number
    }

    json_object = json.dumps(information, indent=4)

    print(json_object)

    with open("UserPass.json", "w") as outfile:
        outfile.write(json_object)

elif register == "Y":
    with open('UserPass.json', 'r') as openfile:
        json_object = json.load(openfile)

        username = input("Type your name: ")
        password = input("Type your password: ")
        if username and password == json_object["username" and "password"]:
            print("Ok everything went good")
            print("")
            for x, y in options.items():
                print(x, y)
            for z in range(random.randint(1000, 1000)):
                options_quest = input(">>>")

                if options_quest == "-h":
                    for x, y in options.items():
                        print(x, y)
                if options_quest == "-rpass":

                    num = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")


                    def random_pass():
                        ran = ''.join(random.choice(string.ascii_letters) for x in range(5))
                        ran += ''.join(random.choice(num) for x in range(5))

                        to_string = list(ran)

                        random.shuffle(to_string)

                        final_pass = ''.join(to_string)

                        return final_pass


                    print("Your password is: ", random_pass())
                if options_quest == "-end":
                    sys.exit(1)

        else:
            print("Something gone wrong")
            change_password = input("If you don't remember password you can change it(Y/N)")
            if change_password == "Y":
                username = input("Type your name: ")
                phone_number = input("Type your phone number: ")
                if username and phone_number == json_object["username" and "phone_number"]:

                    with open('UserPass.json', 'r') as openfile:
                        json_object = json.load(openfile)

                    if username and phone_number == json_object["username" and "phone_number"]:
                        change_password_new = input("Type new password: ")
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
