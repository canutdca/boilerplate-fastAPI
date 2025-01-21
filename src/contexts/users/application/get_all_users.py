from contexts.users.domain.user_repository import UserRepository


def get_all_users(repo: UserRepository):
    return repo.get_users()
