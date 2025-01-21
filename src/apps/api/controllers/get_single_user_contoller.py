from fastapi import Response
from contexts.users.application.get_user_by_id import get_user_by_id
from contexts.users.domain.user_repository import UserRepository


def get_single_user_controller(user_id: int, repo: UserRepository):
    user = get_user_by_id(user_id, repo)
    if user is None:
        return Response(status_code=404, content="User not found")
    return user
