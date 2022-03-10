from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from routes.schemas import organiaztioDisplay,organiaztionBase
from database.database import get_db
from database import db_organization
router = APIRouter(
    prefix='/organize',
    tags=['organize']
)

@router.post('',response_model=organiaztioDisplay)
def create_organiaztion(request:organiaztionBase,db:Session = Depends(get_db)):
    return db_organization.create_organiaztion(db,request)

@router.get('/all',response_model=List[organiaztioDisplay])
def get(db:Session = Depends(get_db)):
    return db_organization.get_all(db)

@router.get('/{id}',response_model=organiaztioDisplay)
def get_one(id:int,db:Session = Depends(get_db)):
    return db_organization.get_one(id,db)

@router.put('/update/{id}')
def update_use(id:int,request:organiaztionBase,db:Session =Depends(get_db)):
    return db_organization.update_use(db,id,request)

