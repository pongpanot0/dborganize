from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from routes.schemas import UserBase,UserDisplay
from database.database import get_db
from database import db_user
from typing import List
router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post('',response_model=UserDisplay)
def create_user(request:UserBase,db:Session = Depends(get_db)):
    return db_user.create_user(db,request)

@router.get('/all',response_model=List[UserDisplay])
def get(db:Session = Depends(get_db)):
    return db_user.get_all(db)

@router.get('/{id}',response_model=UserDisplay)
def get_one(id:int,db:Session = Depends(get_db)):
    return db_user.get_one(id,db)

@router.put('/update/{id}')
def update_use(id:int,request:UserBase,db:Session =Depends(get_db)):
    return db_user.update_use(db,id,request)

