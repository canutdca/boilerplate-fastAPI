from fastapi import Response
from contexts.users.application.create_user.get_new_id import get_new_id
from contexts.users.domain.User import User
from contexts.users.domain.user_repository import UserRepository


def create_user(body: dict, repo: UserRepository) -> None:
    # TODO: use pydantic for validate body
    user_name = body.get("name")
    print(user_name)
    if user_name is None:
        return Response(status_code=400, content="User name is required")
    ids = tuple(user.id for user in repo.get_users())
    repo.add_user(User(get_new_id(ids), user_name))
