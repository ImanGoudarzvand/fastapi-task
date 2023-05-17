from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
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
    # if crud.user.is_superuser(current_user):
    #     items = crud.item.get_multi(db, skip=skip, limit=limit)
    # else:
    #     items = crud.item.get_multi_by_owner(
    #         db=db, owner_id=current_user.id, skip=skip, limit=limit
    #     )
    items = crud.conference.get_multi(db=db)
    return items


@router.post("/", response_model=schemas.ConferenceOut)
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


@router.put("/{id}", response_model=schemas.ConferenceOut)
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
    return conference


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
    conference = crud.conference.remove(db=db, id=id)
    return conference
