from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.conference.ConferenceOut])
def read_conferences(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.user.User = Depends(deps.get_current_active_user),
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


@router.post("/", response_model=schemas.conference.ConferenceOut)
def create_conference(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.conference.ConferenceCreate,
    current_user: models.user.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    item = crud.conference.create(db=db, obj_in=item_in)
    return item


@router.put("/{id}", response_model=schemas.conference.ConferenceOut)
def update_conference(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.conference.ConferenceUpdate,
    current_user: models.user.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an item.
    """
    item = crud.conference.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = crud.item.update(db=db, db_obj=item, obj_in=item_in)
    return item


@router.get("/{id}", response_model=schemas.conference.ConferenceOut)
def read_conference(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.user.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get item by ID.
    """
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return item


@router.delete("/{id}")
def delete_conference(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.user.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = crud.item.remove(db=db, id=id)
    return item
