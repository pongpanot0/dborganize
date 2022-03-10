import datetime
from sqlalchemy.orm.session import Session
from database.models import Dbsystemtheme
from routes.schemas import  systhemThemeBase

def create_systemtheme(db:Session,request:systhemThemeBase):
    new_systemtheme = Dbsystemtheme(
    theme_name = request.theme_name,
    theme_logo = request.theme_logo,
    theme_color = request.theme_color,
    external_email_logo = request.external_email_logo,
    external_email_theme_color = request.external_email_theme_color,
    internal_email_logo = request.internal_email_logo,
    internal_email_theme_color = request.internal_email_theme_color,
    internal_email_footer = request.internal_email_footer,
    created_at = datetime.datetime.now(),
    created_by = request.created_by,
    updated_at = datetime.datetime.now(),
    updated_by = request.updated_by,
    in_activae = request.in_activae,
    )
    db.add(new_systemtheme)
    db.commit()
    db.refresh(new_systemtheme)
    return new_systemtheme

def get_all(db:Session):
    return db.query(Dbsystemtheme).all()

def get_one(id:int,db:Session):
    return db.query(Dbsystemtheme).filter(Dbsystemtheme.theme_id == id).first()

def update_use(db:Session,id:int,request:systhemThemeBase):
    assign_role = db.query(Dbsystemtheme).filter(Dbsystemtheme.theme_id == id)
    assign_role.update({
        Dbsystemtheme.theme_name : request.theme_name,
        Dbsystemtheme.theme_logo : request.theme_logo,
        Dbsystemtheme.theme_color : request.theme_color,
        Dbsystemtheme.external_email_logo : request.external_email_logo,
        Dbsystemtheme.external_email_theme_color : request.external_email_theme_color,
        Dbsystemtheme.internal_email_logo : request.internal_email_logo,
        Dbsystemtheme.internal_email_theme_color : request.internal_email_theme_color,
        Dbsystemtheme.internal_email_footer : request.internal_email_footer,
        Dbsystemtheme.created_by : request.created_by,
        Dbsystemtheme.updated_by : request.updated_by,
        Dbsystemtheme.in_activae : request.in_activae,
    })
    db.commit()
    return 'Ok'