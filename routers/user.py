from fastapi import APIRouter

router = APIRouter()

user_list = ['John', 'Bill', 'Eric']


@router.get('/users')  # index の処理
def get_users():
    return {'users': user_list}
