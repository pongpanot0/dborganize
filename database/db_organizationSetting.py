import datetime
from sqlalchemy.orm.session import Session
from database.models import DborganiaztionSetting
from routes.schemas import  organiaztiosettingBase

def create_organiaztionSetting(db:Session,request:organiaztiosettingBase):
    new_organiaztionSetting = DborganiaztionSetting(
    reject_req_day = request.reject_req_day,
    reject_req_day_flag =request.reject_req_day_flag,
    created_at =datetime.datetime.now(),
    created_by =request.created_by,
    updated_at =datetime.datetime.now(),
    updated_by =request.updated_by,
    in_active  = request.in_active,
    )
    db.add(new_organiaztionSetting)
    db.commit()
    db.refresh(new_organiaztionSetting)
    return new_organiaztionSetting

def get_all(db:Session):
    return db.query(DborganiaztionSetting).all()

def get_one(id:int,db:Session):
    return db.query(DborganiaztionSetting).filter(DborganiaztionSetting.setting_id == id).first()

def update_use(db:Session,id:int,request:organiaztiosettingBase):
    assign_role = db.query(DborganiaztionSetting).filter(DborganiaztionSetting.setting_id == id)
    assign_role.update({
        DborganiaztionSetting.reject_req_day : request.reject_req_day,
        DborganiaztionSetting.reject_req_day_flag : request.reject_req_day_flag,
        DborganiaztionSetting.created_by : request.created_by,
        DborganiaztionSetting.updated_at : datetime.datetime.now(),
        DborganiaztionSetting.updated_by : request.updated_by,
        DborganiaztionSetting.in_active : request.in_active,
    
    })
    db.commit()
    return 'Ok'