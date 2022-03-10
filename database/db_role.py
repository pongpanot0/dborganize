import datetime
from this import d
from sqlalchemy.orm.session import Session
from database.models import Dbroles
from routes.schemas import   rolesBase

def create_roles(db:Session,request:rolesBase):
    new_roles = Dbroles(
    role_name = request.role_name,
    role_description = request.role_description,
    created_at = datetime.datetime.now(),
    created_by = request.created_by,
    updated_at = datetime.datetime.now(),
    updated_by = request.updated_by,
    in_activate = request.in_activate,
    )
    db.add(new_roles)
    db.commit()
    db.refresh(new_roles)
    return new_roles

def get_all(db:Session):
    return db.query(Dbroles).all()

def get_one(id:int,db:Session):
    return db.query(Dbroles).filter(Dbroles.role_id == id).first()

def update_use(db:Session,id:int,request:rolesBase):
    assign_role = db.query(Dbroles).filter(Dbroles.role_id == id)
    assign_role.update({
        Dbroles.role_name : request.role_name,
        Dbroles.role_description : request.role_description,
        Dbroles.created_by : request.created_by,
        Dbroles.updated_at : datetime.datetime.now(),
        Dbroles.updated_by : request.updated_by,
        Dbroles.in_activate : request.in_activate,
    })
    db.commit()
    return 'Ok'