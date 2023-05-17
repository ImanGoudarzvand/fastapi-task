from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.conference import Conference
from app.schemas.conference import ConferenceCreate, ConferenceUpdate


class CRUDconference(CRUDBase[Conference, ConferenceCreate, ConferenceUpdate]):

    pass


conference = CRUDconference(Conference)
