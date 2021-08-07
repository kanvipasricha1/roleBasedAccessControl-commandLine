from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from user_roles import RoleType


@dataclass
class BaseUser(ABC):
    name: str
    email: str

    @abstractmethod
    def describe_user(self):
        """this function describes the user"""

    def assign_role_to_a_user(self):
        """this function assigns a role to the user"""


@dataclass
class Admin(BaseUser):

    def describe_user(self):
        print('User with name', self.name, self.email)


@dataclass
class Normal(BaseUser):
    role: RoleType = None

    def describe_user(self):
        print('User with name', self.name, self.email)

    def assign_role_to_a_user(self, user_role: RoleType):
        self.role = user_role

    def assign_resources_to_user(self, resource: list):
        self.resouces = resource
