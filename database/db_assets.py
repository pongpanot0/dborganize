import datetime
from sqlalchemy.orm.session import Session
from database.models import Dbassets
from routes.schemas import assetsBase


def create_assets(db: Session, request: assetsBase):
    new_assets = Dbassets(
        owner=request.owner,
        onwer_id=request.onwer_id,
        asset_file_name=request.asset_file_name,
        asset_file_type=request.asset_file_type,
        asset_file_size=request.asset_file_size,
        asset_public_path=request.asset_public_path,
        created_at=datetime.datetime.now(),
        created_by=request.created_by,
        updated_at=datetime.datetime.now(),
        updated_by=request.updated_by,
        in_active=request.in_active,
    )
    db.add(new_assets)
    db.commit()
    db.refresh(new_assets)
    return new_assets


def get_all(db: Session):
    return db.query(Dbassets).all()


def get_one(id:int,db:Session):
    return db.query(Dbassets).filter(Dbassets.asset_id == id).first()

def update_use(db:Session,id:int,request:assetsBase):
    assign_role = db.query(Dbassets).filter(Dbassets.asset_id == id)
    assign_role.update({
        Dbassets.owner : request.owner,
        Dbassets.onwer_id : request.onwer_id,
        Dbassets.asset_file_name : request.asset_file_name,
        Dbassets.asset_file_type : request.asset_file_type,
        Dbassets.asset_file_size : request.asset_file_size,
        Dbassets.created_by : request.created_by,
        Dbassets.updated_by : request.updated_by,
    })
    db.commit()
    return 'Ok'