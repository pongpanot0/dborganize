from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from routes.schemas import user_assign_roleBase,user_assign_roleDisplay
from database.database import get_db
from typing import List
from database import db_user_assign_role
router = APIRouter(
    prefix='/user_assign_role',
    tags=['user_assign_role']
)

@router.post('',response_model=user_assign_roleDisplay)
def create_user_assign_role(request:user_assign_roleBase,db:Session = Depends(get_db)):
    return db_user_assign_role.create_user_assign_role(db,request)


@router.get('/all',response_model=List[user_assign_roleDisplay])
def get(db:Session = Depends(get_db)):
    return db_user_assign_role.get_all(db)

@router.get('/{id}',response_model=user_assign_roleDisplay)
def get_one(id:int,db:Session = Depends(get_db)):
    return db_user_assign_role.get_one(id,db)

@router.put('/update/{id}')
def update_use(id:int,request:user_assign_roleBase,db:Session =Depends(get_db)):
    return db_user_assign_role.update_use(db,id,request)