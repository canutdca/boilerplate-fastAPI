from contexts.users.application.get_all_users import get_all_users
from contexts.users.domain.user_repository import UserRepository


def get_all_users_controller(repo: UserRepository):
    return get_all_users(repo)
