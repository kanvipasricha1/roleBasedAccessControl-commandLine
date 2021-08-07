from user import Admin
from utility import create_user, switch_user, edit_role, view_roles

if __name__ == "__main__":
    all_users = []
    master_admin = Admin(name='Admin', email='admin@bluestack.com')
    all_users.append(master_admin)
    current_user = master_admin

    allowed_permission = [1, 2, 3]

    while True:
        if isinstance(current_user, Admin):
            print("hi! you are logged in as admin")
            print("press 1 for login as another user \npress 2 "
                  "for create user \npress 3 for edit role \npress 4 to exit")
        else:
            print(f"hi! you are logged in as {current_user.name}")
            print("press 1 for login as another user \n"
                  "press 2 for view roles \npress 3 for access resource  \npress 4 to exit")

        choice = input('')
        if not choice.isnumeric():
            print("Please enter a valid choice")
            continue
        choice = int(choice)
        if choice not in allowed_permission:
            break

        if isinstance(current_user, Admin):
            if choice == 1:
                current_user = switch_user(all_users)
            elif choice == 2:
                new_user = create_user()
                all_users.append(new_user)
            elif choice == 3:
                edit_role(all_users)
        else:
            if choice == 1:
                current_user = switch_user(all_users)
            elif choice == 2:
                view_roles(current_user)
            elif choice == 3:
                edit_role(all_users)
