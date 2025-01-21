from abc import ABC, abstractmethod
from typing import Tuple
from contexts.users.domain.User import User


class UserRepository(ABC):

    @abstractmethod
    def add_user(self, user: User): ...

    @abstractmethod
    def get_users(self) -> Tuple[User]: ...

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User | None: ...
