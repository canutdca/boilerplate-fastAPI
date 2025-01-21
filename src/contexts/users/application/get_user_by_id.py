from contexts.users.domain.user_repository import UserRepository


def get_user_by_id(user_id: int, repo: UserRepository):
    return repo.get_user_by_id(user_id)
