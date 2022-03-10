from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from routes.schemas import organiaztiosettingBase,organiaztiosettingDisplay
from database.database import get_db
from typing import List
from database import db_organizationSetting
router = APIRouter(
    prefix='/organiaztiosetting',
    tags=['organiaztiosetting']
)

@router.post('',response_model=organiaztiosettingDisplay)
def create_organiaztionSetting(request:organiaztiosettingBase,db:Session = Depends(get_db)):
    return db_organizationSetting.create_organiaztionSetting(db,request)


@router.get('/all',response_model=List[organiaztiosettingDisplay])
def get(db:Session = Depends(get_db)):
    return db_organizationSetting.get_all(db)

@router.get('/{id}',response_model=organiaztiosettingDisplay)
def get_one(id:int,db:Session = Depends(get_db)):
    return db_organizationSetting.get_one(id,db)


@router.put('/update/{id}')
def update_use(id:int,request:organiaztiosettingBase,db:Session =Depends(get_db)):
    return db_organizationSetting.update_use(db,id,request)

