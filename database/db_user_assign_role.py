import datetime
from sqlalchemy.orm.session import Session
from database.models import Dbuser_assign_role
from routes.schemas import  user_assign_roleBase

def create_user_assign_role(db:Session,request:user_assign_roleBase):
    new_user_assign_role = Dbuser_assign_role(
    user_id =request.user_id,
    role_id =request.role_id,
    created_at =datetime.datetime.now(),
    created_by =request.created_by,
    updated_at =datetime.datetime.now(),
    updated_by =request.updated_by,
    )
    db.add(new_user_assign_role)
    db.commit()
    db.refresh(new_user_assign_role)
    return new_user_assign_role

def get_all(db:Session,skip: int = 0, limit: int = 1):
    return db.query(Dbuser_assign_role).offset(skip).limit(limit).all()


def get_one(id:int,db:Session,):
    return db.query(Dbuser_assign_role).filter(Dbuser_assign_role.assign_role_id == id).first()

def update_use(db:Session,id:int,request:user_assign_roleBase):
    assign_role = db.query(Dbuser_assign_role).filter(Dbuser_assign_role.assign_role_id == id)
    assign_role.update({
        Dbuser_assign_role.user_id : request.user_id,
        Dbuser_assign_role.role_id : request.role_id,
        Dbuser_assign_role.created_at : request.created_at,
        Dbuser_assign_role.created_by : request.created_by,
        Dbuser_assign_role.updated_at : request.updated_at,
        Dbuser_assign_role.updated_by : request.updated_by,
    })
    db.commit()
    return 'Ok'