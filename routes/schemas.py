
from typing import List
from datetime import datetime

from pydantic import BaseModel

class organiaztionSetting(BaseModel):
    setting_id : int
    reject_req_day : int
    class Config():
        orm_mode = True

class organiaztion(BaseModel):
    organiaztion_id : int
    company_id : int
    organization_name : str
    class Config():
        orm_mode = True
      
      

class langauage(BaseModel):
    language_id : int
    language_name : str
    class Config():
        orm_mode = True
        
class theme(BaseModel):
    theme_id : int 
    theme_name : str
    class Config():
        orm_mode = True
    
class UserBase(BaseModel):
    company_id : int
    organization_id : int
    current_organization_id : int
    user_name : str
    user_position : str
    user_email : str
    user_password : str
    user_available : int
 
    language_id : int
    theme_id : int
 
    created_by : int
 
    updated_by : int
    in_active : int
    
    
class UserDisplay(BaseModel):
    company_id : int
    org : organiaztion
    current_organization_id : int
    user_name : str
    user_position : str
    user_email : str
    user_password : str
    user_available : int
    activate_at : datetime
    lan : langauage
    thene : theme
    created_at : datetime
    created_by : int
    updated_at : datetime
    updated_by : int
    in_active : int
    class Config():
        orm_mode = True
            
class UserSet(BaseModel):
    user_id : int
    user_name : str
    class Config():
        orm_mode = True

class organiaztionBase(BaseModel):
    company_id : int
    organization_name : str
    organization_parent : int
    langauage_id : int
    theme_id : int
    created_by_id : int
    updated_by : int
    in_active : int
    
class organiaztioDisplay(BaseModel):
    organiaztion_id : int
    company_id : int
    organization_name : str
    organization_parent : int
    langauageorganize : langauage
    themeid : theme
    create_at : datetime
    use : UserSet
    updated_at : datetime
    updated_by : int
    in_active : int
    class Config():
        orm_mode = True
        

        
class organiaztiosettingBase(BaseModel):
    reject_req_day : int
    reject_req_day_flag : int
    created_by : int
    updated_by : int
    in_active : int
    
class organiaztiosettingDisplay(BaseModel):
    reject_req_day : int
    reject_req_day_flag : int
    created_at : datetime
    organiaztionSetting_created : UserSet
    updated_at : datetime
    updated_by : int
    in_active : int
    class Config():
        orm_mode = True
        
class systhemThemeBase(BaseModel):
    theme_name : str
    theme_logo : int
    theme_color : str
    external_email_logo : int
    external_email_theme_color : str
    internal_email_logo : int
    internal_email_theme_color : str
    internal_email_footer : str
    created_by : int
    updated_by : int
    in_activae : int
      
      
class systhemThemeDisplay(BaseModel):
    theme_name : str
    theme_logo : int
    theme_color : str
    external_email_logo : int
    external_email_theme_color : str
    internal_email_logo : int
    internal_email_theme_color : str
    internal_email_footer : str
    created_at : datetime
    lange : UserSet
    updated_at : datetime
    updated_by : int
    in_activae : int
    class Config():
        orm_mode = True
    
class systemlangaueBase(BaseModel):
    language_name : str
    language_code : str
    language_desciption : str
    created_by : int
    updated_by : int
    in_active : int
    
class systemlangaueDisplay(BaseModel):
    language_name : str
    language_code : str
    language_desciption : str
    created_at : datetime
    created_by : int
    updated_at : datetime
    updated_by : int
    in_active : int
    class Config():
        orm_mode = True
        
class role(BaseModel):
    role_name : str
    class Config():
        orm_mode = True
        
class assignRole(BaseModel):
    assign_role_id : int 
    class Config():
        orm_mode = True
        
class user_assign_roleBase(BaseModel):
    user_id : int
    role_id : int
    created_by : int
    updated_by : int

class user_assign_roleDisplay(BaseModel):
    role_created_by : UserSet
    role_by : role
    created_at : datetime
    created_by : int
    updated_at : datetime
    updated_by : int
    class Config():
        orm_mode = True
        
        
class rolesBase(BaseModel):
    role_name : str
    role_description : int
    created_by : int
    updated_by : int
    in_activate : int

        
class rolesDisplay(BaseModel):
    role_id:int
    role_name : str
    role_description : int
    created_at : datetime
    created_by : int
    updated_at : datetime
    updated_by : int
    in_activate : int
    class Config():
        orm_mode = True
        
        
class assetsBase(BaseModel):
    owner : str
    onwer_id : int
    asset_file_name : str
    asset_file_type : str
    asset_file_size : int
    asset_public_path : str
    created_by : int
    updated_by : int
    in_active : int
    class Config():
        orm_mode = True
        
class assetsDisplay(BaseModel):
    asset_id: int
    owner : str
    onwer_id : int
    asset_file_name : str
    asset_file_type : str
    asset_file_size : int
    asset_public_path : str
    created_at : datetime
    lang : UserSet
    updated_at : datetime
    updated_by : int
    in_active : int
    class Config():
        orm_mode = True