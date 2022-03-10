import datetime
from sqlalchemy.orm.session import Session
from database.models import Dborganiaztion
from routes.schemas import  organiaztionBase

def create_organiaztion(db:Session,request:organiaztionBase):
    new_organiaztion = Dborganiaztion(
    company_id = request.company_id,
    organization_name = request.organization_name,
    organization_parent = request.organization_parent,
    langauage_id = request.langauage_id,
    theme_id = request.theme_id,
    create_at = datetime.datetime.now(),
    created_by = request.created_by_id,
    updated_at = datetime.datetime.now(),
    updated_by = request.updated_by,
    in_active = request.in_active,
    )
    db.add(new_organiaztion)
    db.commit()
    db.refresh(new_organiaztion)
    return new_organiaztion

def get_all(db:Session):
    return db.query(Dborganiaztion).all()


def get_one(id:int,db:Session):
    return db.query(Dborganiaztion).filter(Dborganiaztion.organiaztion_id == id).first()


def update_use(db:Session,id:int,request:organiaztionBase):
    assign_role = db.query(Dborganiaztion).filter(Dborganiaztion.organiaztion_id == id)
    assign_role.update({
        Dborganiaztion.company_id : request.company_id,
        Dborganiaztion.organization_name : request.organization_name,
        Dborganiaztion.organization_parent : request.organization_parent,
        Dborganiaztion.langauage_id : request.langauage_id,
        Dborganiaztion.theme_id : request.theme_id,
        Dborganiaztion.updated_at : datetime.datetime.now(),
        Dborganiaztion.updated_by : request.updated_by,
        Dborganiaztion.in_active : request.in_active,
    })
    db.commit()
    return 'Ok'

