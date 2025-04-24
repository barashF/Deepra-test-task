from fastapi import APIRouter


router = APIRouter(
    prefix='/test_task',
    tags=['Test task Deepra']
)


@router.get('friends/', summary='Друзьяшки')
async def friends(name: str, message: str):
    return f'Hello {name}! {message}'