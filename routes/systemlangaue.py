from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from routes.schemas import systemlangaueDisplay,systemlangaueBase
from database.database import get_db
from database import db_systemlangaue
from typing import List
router = APIRouter(
    prefix='/systemlangaue',
    tags=['systemlangaue']
)

@router.post('',response_model=systemlangaueDisplay)
def create_systemlangaue(request:systemlangaueBase,db:Session = Depends(get_db)):
    return db_systemlangaue.create_systemlangaue(db,request)


@router.get('/all',response_model=List[systemlangaueDisplay])
def get(db:Session = Depends(get_db)):
    return db_systemlangaue.get_all(db)

@router.get('/{id}',response_model=systemlangaueDisplay)
def get_one(id:int,db:Session = Depends(get_db)):
    return db_systemlangaue.get_one(id,db)

@router.put('/update/{id}')
def update_use(id:int,request:systemlangaueBase,db:Session =Depends(get_db)):
    return db_systemlangaue.update_use(db,id,request)