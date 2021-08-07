# class AssignRole:
from user import Normal
from user_roles import RoleType


def create_user():
    user_name = input('Enter user name: ')
    user_email = input('Enter user email: ')
    normal = Normal(name=user_name, email=user_email)
    normal.describe_user()
    user_role = input('Enter new user role, choices are [SD1, SD2, SD3]')
    normal.assign_role_to_a_user(RoleType[user_role])
    user_resources = input('Enter resources accessible to user, choices are'
                           ' [EC2, S3, SNS, SQS]')
    user_resources = user_resources.split(',')
    normal.assign_resources_to_user(user_resources)
    return normal


def switch_user(all_users):
    while True:
        new_user = input('Enter the name of user whose profile you want to switch to ')
        for user in all_users:
            if user.name == new_user:
                return user

        print(f'No user found with name : {new_user}')


def edit_role(all_users):
    user_to_edit = input('Enter name to edit role ')
    new_role = input('Enter new role Choices are [tech, ops, bi]')
    for user in all_users:
        if user.name == user_to_edit:
            user.assign_role_to_a_user = new_role


def view_roles(user):
    print(user.role)
