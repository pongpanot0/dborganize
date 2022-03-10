import datetime
from sqlalchemy.orm.session import Session
from database.models import DbUser
from routes.schemas import UserBase

def create_user(db:Session,request:UserBase):
    new_user = DbUser(
        company_id = request.company_id,
        organization_id = request.organization_id,
        current_organization_id = request.current_organization_id,
        user_name = request.user_name,
        user_position = request.user_position,
        user_email = request.user_email,
        user_password = request.user_password,
        user_available = request.user_available,
        activate_at = datetime.datetime.now(),
        language_id = request.language_id,
        theme_id = request.theme_id,
        created_at = datetime.datetime.now(),
        created_by = request.created_by,
        updated_at = datetime.datetime.now(),
        updated_by = request.updated_by,
        in_active = request.in_active,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db:Session):
    return db.query(DbUser).all()

def get_one(id:int,db:Session):
    return db.query(DbUser).filter(DbUser.user_id == id).first()

def update_use(db:Session,id:int,request:UserBase):
    assign_role = db.query(DbUser).filter(DbUser.user_id == id)
    assign_role.update({
        DbUser.company_id : request.company_id,
        DbUser.organization_id : request.organization_id,
        DbUser.current_organization_id : request.current_organization_id,
        DbUser.user_name : request.user_name,
        DbUser.user_position : request.user_position,
        DbUser.user_email : request.user_email,
        DbUser.user_password : request.user_password,
        DbUser.user_available : request.user_available,
        DbUser.language_id : request.language_id,
        DbUser.theme_id : request.theme_id,
        DbUser.updated_at : datetime.datetime.now(),
        DbUser.updated_by : request.updated_by,
        DbUser.in_active : request.in_active,
    })
    db.commit()
    return 'Ok'