from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from config.db import get_db
from models.index import users
from schemas.index import User
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

user = APIRouter()

@user.get("/{username}", response_model=User)
async def read_data(username: str, db: Session = Depends(get_db)):
    try:
        query = users.select().where(users.c.username == username)
        return db.execute(query).fetchone()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@user.post("/", response_model=User)
async def write_data(user: User, db: Session = Depends(get_db)):
    try:
        new_user = users.insert().values(
            username=user.username,
            firstname=user.firstname,
            lastname=user.lastname,
            pincode=user.pincode,
            email=user.email
        )
        db.execute(new_user)
        db.commit()
        return user
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@user.put("/{username}", response_model=User)
async def update_data(username: str, user: User, db: Session = Depends(get_db)):
    try:
        updated_user = users.update().values(
            username=user.username,
            firstname=user.firstname,
            lastname=user.lastname,
            pincode=user.pincode,
            email=user.email
        ).where(users.c.username == username)
        db.execute(updated_user)
        db.commit()
        return user
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@user.delete("/{username}", response_model=dict)
async def delete_data(username: str, db: Session = Depends(get_db)):
    try:
        deleted_user = users.delete().where(users.c.username == username)
        db.execute(deleted_user)
        db.commit()
        return {"message": f"Successfully deleted user {username}"}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
