from typing import List, Tuple
from contexts.users.domain.User import User
from contexts.users.domain.user_repository import UserRepository


class UserRepositoryMemory(UserRepository):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "users"):
            self.users: List[User] = [User(1, "user 1")]

    def add_user(self, user: User):
        self.users.append(user)

    def get_users(self) -> Tuple[User]:
        return tuple(self.users)

    # TODO: implement Criteria pattern
    def get_user_by_id(self, user_id: int) -> User | None:
        return next((user for user in self.users if user.id == user_id), None)
