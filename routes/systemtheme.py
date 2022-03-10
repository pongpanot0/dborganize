from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from routes.schemas import systhemThemeBase,systhemThemeDisplay
from database.database import get_db
from database import db_systemtheme
from typing import List
router = APIRouter(
    prefix='/systemtheme',
    tags=['systemtheme']
)

@router.post('',response_model=systhemThemeDisplay)
def create_systemtheme(request:systhemThemeBase,db:Session = Depends(get_db)):
    return db_systemtheme.create_systemtheme(db,request)

@router.get('/all',response_model=List[systhemThemeDisplay])
def get(db:Session = Depends(get_db)):
    return db_systemtheme.get_all(db)

@router.get('/{id}',response_model=systhemThemeDisplay)
def get_one(id:int,db:Session = Depends(get_db)):
    return db_systemtheme.get_one(id,db)

@router.put('/update/{id}')
def update_use(id:int,request:systhemThemeBase,db:Session =Depends(get_db)):
    return db_systemtheme.update_use(db,id,request)