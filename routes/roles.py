from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from routes.schemas import rolesBase,rolesDisplay
from database.database import get_db
from database import db_role
from typing import List
router = APIRouter(
    prefix='/role',
    tags=['role']
)

@router.post('',response_model=rolesDisplay)
def create_roles(request:rolesBase,db:Session = Depends(get_db)):
    return db_role.create_roles(db,request)

@router.get('/all',response_model=List[rolesDisplay])
def get(db:Session = Depends(get_db)):
    return db_role.get_all(db)

@router.get('/{id}',response_model=rolesDisplay)
def get_one(id:int,db:Session = Depends(get_db)):
    return db_role.get_one(id,db)


@router.put('/update/{id}')
def update_use(id:int,request:rolesDisplay,db:Session =Depends(get_db)):
    return db_role.update_use(db,id,request)