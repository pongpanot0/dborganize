import datetime
from sqlalchemy.orm.session import Session
from database.models import Dbsystemlangaue
from routes.schemas import  systemlangaueBase

def create_systemlangaue(db:Session,request:systemlangaueBase):
    new_systemlangaue = Dbsystemlangaue(
    language_name = request.language_name,
    language_code = request.language_code,
    language_desciption = request.language_desciption,
    created_at = datetime.datetime.now(),
    created_by = request.created_by,
    updated_at = datetime.datetime.now(),
    updated_by = request.updated_by,
    in_active = request.in_active,
    )
    db.add(new_systemlangaue)
    db.commit()
    db.refresh(new_systemlangaue)
    return new_systemlangaue

def get_all(db:Session):
    return db.query(Dbsystemlangaue).all()

def get_one(id:int,db:Session):
    return db.query(Dbsystemlangaue).filter(Dbsystemlangaue.language_id == id).first()


def update_use(db:Session,id:int,request:systemlangaueBase):
    assign_role = db.query(Dbsystemlangaue).filter(Dbsystemlangaue.language_id == id)
    assign_role.update({
        Dbsystemlangaue.language_name : request.language_name,
        Dbsystemlangaue.language_code : request.language_code,
        Dbsystemlangaue.language_desciption : request.language_desciption,
        Dbsystemlangaue.created_by : request.created_by,
        Dbsystemlangaue.updated_at : datetime.datetime.now,
        Dbsystemlangaue.updated_by : request.updated_by,
        Dbsystemlangaue.in_active : request.in_active,
    })
    db.commit()
    return 'Ok'