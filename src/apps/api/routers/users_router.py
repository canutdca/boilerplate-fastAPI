from fastapi import APIRouter, Depends

from apps.api.controllers.get_all_users_controller import get_all_users_controller
from apps.api.controllers.get_single_user_contoller import get_single_user_controller
from contexts.users.application.create_user.create_user import create_user
from contexts.users.domain.user_repository import UserRepository
from contexts.users.infrastructure.user_repository_memory import UserRepositoryMemory


router = APIRouter()


def get_user_repository() -> UserRepository:
    return UserRepositoryMemory()


@router.get("/users")
def get_users(repo: UserRepository = Depends(get_user_repository)):
    return get_all_users_controller(repo)


@router.post("/users")
def create_users(body: dict, repo: UserRepository = Depends(get_user_repository)):
    return create_user(body, repo)


@router.get("/user/{user_id}")
def get_user(user_id: int, repo: UserRepository = Depends(get_user_repository)):
    return get_single_user_controller(user_id, repo)
