from fastapi import FastAPI

from fast_do_zero.schemas import UserSchema, UserPublicSchema

from http import  HTTPStatus

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo', 'test': 'teste'}

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublicSchema)
def create_user(user: UserSchema):
    return user
