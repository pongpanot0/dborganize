from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from routes.schemas import assetsBase,assetsDisplay
from database.database import get_db
from database import db_assets
router = APIRouter(
    prefix='/assets',
    tags=['assets']
)

@router.post('',response_model=assetsDisplay)
def create_assets(request:assetsBase,db:Session = Depends(get_db)):
    return db_assets.create_assets(db,request)

@router.get('/all',response_model=List[assetsDisplay])
def get(db:Session = Depends(get_db)):
    return db_assets.get_all(db)

@router.get('/{id}',response_model=assetsDisplay)
def get_one(id:int,db:Session = Depends(get_db)):
    return db_assets.get_one(id,db)

@router.put('/update/{id}')
def update_use(id:int,request:assetsBase,db:Session =Depends(get_db)):
    return db_assets.update_use(db,id,request)