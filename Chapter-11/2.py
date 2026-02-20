def register_user(username, password):
    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")

def show_users():
    with open("users.txt", "r") as file:
        for line in file:
            print(line.strip())

register_user("shahid", "1234")
show_users()
