from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.ConferenceOut])
def read_conferences(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve items.
    """
    items = crud.conference.get_multi(db=db)
    return items


@router.post("/", response_model=schemas.ConferenceOut, status_code=status.HTTP_201_CREATED)
def create_conference(
    *,
    db: Session = Depends(deps.get_db),
    conference_in: schemas.ConferenceCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    conference = crud.conference.create(db=db, obj_in=conference_in)
    return conference


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_conference(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    conference_in: schemas.ConferenceUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an conference.
    """
    conference = crud.conference.get(db=db, id=id)
    if not conference:
        raise HTTPException(status_code=404, detail="Conference not found")

    conference = crud.conference.update(db=db, db_obj=conference, obj_in=conference_in)

    return {"detail": "conference updated"}








@router.get("/{id}", response_model=schemas.ConferenceOut)
def read_conference(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get conference by ID.
    """
    conference = crud.conference.get(db=db, id=id)
    if not conference:
        raise HTTPException(status_code=404, detail="conference not found")
    return conference


@router.delete("/{id}")
def delete_conference(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an conference.
    """
    conference = crud.conference.get(db=db, id=id)
    if not conference:
        raise HTTPException(status_code=404, detail="conference not found")
    crud.conference.remove(db=db, id=id)
    return Response("conference deleted", status_code=status.HTTP_204_NO_CONTENT)
