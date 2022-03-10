
from .database import Base
from sqlalchemy.dialects.mysql import VARCHAR,TINYINT,TEXT
from sqlalchemy import Column,Integer,String,DateTime,Text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
class DbUser(Base):
    __tablename__ = 'users'
    user_id = Column(Integer,primary_key=True,index=True)
    company_id = Column(Integer)
    organization_id = Column(Integer,ForeignKey('organiaztion.organiaztion_id'))
    current_organization_id = Column(Integer)
    user_name = Column(VARCHAR(50))
    user_position = Column(VARCHAR(50))
    user_email = Column(VARCHAR(50))
    user_password = Column(VARCHAR(50))
    user_available = Column(TINYINT(1))
    activate_at = Column(DateTime)
    language_id = Column(Integer,ForeignKey('systemlangaue.language_id'))
    theme_id = Column(Integer,ForeignKey('system_theme.theme_id'))
    created_at = Column(DateTime)
    created_by = Column(Integer)
    updated_at = Column(DateTime)
    updated_by = Column(Integer)
    in_active = Column(TINYINT(1),default=0)
    org = relationship("Dborganiaztion", foreign_keys=[organization_id])
    lan = relationship("Dbsystemlangaue", foreign_keys=[language_id])
    thene = relationship("Dbsystemtheme", foreign_keys=[theme_id])
    user_organizationSetting = relationship('DborganiaztionSetting',back_populates='organiaztionSetting_created')
    role_created = relationship('Dbroles',back_populates='created_role_by')
    assing_role = relationship('Dbuser_assign_role',back_populates='role_created_by')
    
class Dborganiaztion(Base):
    __tablename__ = 'organiaztion'
    organiaztion_id = Column(Integer,primary_key=True,index=True)
    company_id = Column(Integer) #Get By company
    organization_name = Column(VARCHAR(50)) #Get By company
    organization_parent = Column(Integer) #Get By company
    langauage_id = Column(Integer,ForeignKey('systemlangaue.language_id')) #Get By langauage
    theme_id = Column(Integer,ForeignKey('system_theme.theme_id')) #Get By theme_id
    create_at = Column(DateTime)
    created_by = Column(Integer,ForeignKey('users.user_id')) #ดึงมาจาก USER ID
    updated_at = Column(DateTime)
    updated_by = Column(Integer) #ดึงมาจาก USER ID
    in_active = Column(TINYINT(1),default=0)
    use = relationship("DbUser", foreign_keys=[created_by])
    langauageorganize = relationship('Dbsystemlangaue',back_populates='organizelangauage')
    themeid = relationship('Dbsystemtheme',back_populates='organize')
    
    
class DborganiaztionSetting(Base):
    __tablename__ = 'organiaztionsetting'
    setting_id = Column(Integer,primary_key=True,index=True)
    reject_req_day = Column(Integer)
    reject_req_day_flag = Column(TINYINT(1),default=0)
    created_at = Column(DateTime)
    created_by = Column(Integer,ForeignKey('users.user_id')) #ดึงมาจาก User
    updated_at = Column(DateTime)
    updated_by = Column(Integer) #ดึงมาจาก User
    in_active = Column(TINYINT(1),default=0)
    organiaztionSetting_created = relationship('DbUser',back_populates='user_organizationSetting')
    
class Dbsystemtheme(Base):
    __tablename__ = 'system_theme'
    theme_id = Column(Integer,primary_key=True,index=True)
    theme_name = Column(VARCHAR(100))
    theme_logo = Column(Integer)
    theme_color = Column(VARCHAR(100))
    external_email_logo = Column(Integer)
    external_email_theme_color = Column(VARCHAR(100))
    internal_email_logo = Column(Integer)
    internal_email_theme_color = Column(VARCHAR(100))
    internal_email_footer = Column(Text(100))
    created_at = Column(DateTime)
    created_by = Column(Integer,ForeignKey('users.user_id'))
    updated_at = Column(DateTime)
    updated_by = Column(Integer)
    in_activae = Column(TINYINT(1),default=5)
    lange = relationship("DbUser", foreign_keys=[created_by])
    organize = relationship('Dborganiaztion',back_populates='themeid')
    
    
class Dbsystemlangaue(Base):
    __tablename__ = 'systemlangaue'
    language_id = Column(Integer,primary_key=True,index=True)
    language_name = Column(VARCHAR(100))
    language_code = Column(VARCHAR(100))
    language_desciption = Column(TEXT(100))
    created_at = Column(DateTime)
    created_by = Column(Integer,ForeignKey('users.user_id'))
    updated_at = Column(DateTime)
    updated_by = Column(Integer)
    in_active = Column(TINYINT(1),default=1)
    lang = relationship("DbUser", foreign_keys=[created_by])
    organizelangauage = relationship('Dborganiaztion',back_populates='langauageorganize')
    
class Dbuser_assign_role(Base):
    __tablename__ = 'user_assign_role'
    assign_role_id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey('users.user_id'))
    role_id = Column(Integer,ForeignKey('roles.role_id'))
    created_at = Column(DateTime)
    created_by = Column(Integer)
    updated_at = Column(DateTime)
    updated_by = Column(Integer)
    role_created_by = relationship('DbUser',back_populates='assing_role')
    role_by = relationship('Dbroles',back_populates='assign_by')
    
    
class Dbroles(Base):
    __tablename__ = 'roles'
    role_id = Column(Integer,primary_key=True,index=True)
    role_name = Column(VARCHAR(100))
    role_description = Column(Text(100))
    created_at = Column(DateTime)
    created_by = Column(Integer)
    updated_at = Column(DateTime)
    updated_by = Column(Integer,ForeignKey('users.user_id'))
    in_activate = Column(TINYINT(1),default=5)
    created_role_by = relationship('DbUser',back_populates='role_created')
    assign_by = relationship('Dbuser_assign_role',back_populates='role_by')
    
class Dbassets(Base):
    __tablename__='assets'
    asset_id = Column(Integer,primary_key=True,index=True)
    owner = Column(VARCHAR(200)) #Owner Name
    onwer_id = Column(Integer)
    asset_file_name = Column(VARCHAR(200))
    asset_file_type = Column(VARCHAR(200))
    asset_file_size = Column(Integer)
    asset_public_path = Column(VARCHAR(200))
    created_at = Column(DateTime)
    created_by = Column(Integer,ForeignKey('users.user_id'))
    updated_at = Column(DateTime)
    updated_by = Column(Integer)
    in_active = Column(TINYINT(1))
    lang = relationship("DbUser", foreign_keys=[created_by])