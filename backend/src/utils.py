from src import db
from src.models.user_model import User
from src.models.learner_model import Learner
from src.models.tutor_model import Tutor
import base64

time = "%Y-%m-%dT%H:%M:%S"
classes = {"user": User, "learner": Learner, "tutor": Tutor}

def to_dict(self):
    """returns a dictionary containing all keys/values of the instance"""
    new_dict = self.__dict__.copy()
    if 'profile_picture_blob' in new_dict and new_dict['profile_picture_blob'] is not None:
        new_dict['profile_picture_blob'] = base64.b64encode(new_dict['profile_picture_blob']).decode('utf-8')
    if "birthdate" in new_dict and new_dict["birthdate"] is not None:
        new_dict["birthdate"] = new_dict["birthdate"].strftime(time)
    if "last_time_online" in new_dict and new_dict["last_time_online"] is not None:
        new_dict["last_time_online"] = new_dict["last_time_online"].strftime(time)
    if "_sa_instance_state" in new_dict:
        del new_dict["_sa_instance_state"]
    return new_dict

def all(cls=None):
    """query on the current database session"""
    new_list = []
    # for clss in classes:
     #     if cls is None or cls is classes[clss] or cls is clss:
    if cls is not None:
        objs = cls.query.all()
        for obj in objs:
            # key = obj.__class__.__name__ + '.' + str(obj.id)
            new_list.append(to_dict(obj))
    return (new_list)

def get_by_id(cls, id):
    """query on the current database session"""
    if cls is not None:
        obj = cls.query.get(id)
        if obj is not None:
            return to_dict(obj)
    return None

def add(obj):
    """add an object to the current database session"""
    db.session.add(obj)
    db.session.commit()
    return obj

def delete(obj):
    """delete an object from the current database session"""
    db.session.delete(obj)
    db.session.commit()
    return obj

def update(obj):
    """update an object in the current database session"""
    db.session.commit()
    return obj
