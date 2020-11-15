from fastapi import APIRouter

router = APIRouter()

user_list = ['John', 'Bill', 'Eric']


@router.get('/users')  # index の処理
def get_users():
    return {'users': user_list}


@router.get('/users/{index}')  # この処理を追加
def get_user(index: int):
    return {'user': user_list[index]}

