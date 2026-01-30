from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import FeatureFlag
from schemas.feature_flags import (
    FeatureFlagCreateSchema,
    FeatureFlagReadSchema,
    FeatureFlagUpdateSchema,
)

feature_flag_router = APIRouter()
router = feature_flag_router


@router.post("", response_model=FeatureFlagReadSchema)
def feature_flag_create(
    data: FeatureFlagCreateSchema,
    db: Session = Depends(get_db),
):
    feature_flag = FeatureFlag(**data.model_dump())

    db.add(feature_flag)
    db.commit()
    db.refresh(feature_flag)

    return feature_flag


@router.get("", response_model=list[FeatureFlagReadSchema])
def feature_flag_get_all(db: Session = Depends(get_db)):
    feature_flags = db.query(FeatureFlag).order_by(FeatureFlag.id).all()
    return feature_flags


@router.get("/{feature_flag_id}", response_model=FeatureFlagReadSchema)
def feature_flag_get_one(feature_flag_id: int, db: Session = Depends(get_db)):

    feature_flag = db.get(FeatureFlag, feature_flag_id)

    if not feature_flag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Feature Flag not found!"
        )

    return feature_flag


@router.patch("/{feature_flag_id}", response_model=FeatureFlagReadSchema)
def feature_flag_update(
    feature_flag_id: int,
    update_data: FeatureFlagUpdateSchema,
    db: Session = Depends(get_db),
):

    feature_flag = db.get(FeatureFlag, feature_flag_id)

    if not feature_flag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Feature Flag not found!"
        )

    update_dict = update_data.model_dump(exclude_unset=True)
    for key, value in update_dict.items():
        setattr(feature_flag, key, value)

    db.commit()
    db.refresh(feature_flag)

    return feature_flag


@router.delete("/{feature_flag_id}", status_code=status.HTTP_204_NO_CONTENT)
def feature_flag_delete(feature_flag_id: int, db: Session = Depends(get_db)):

    feature_flag = db.get(FeatureFlag, feature_flag_id)

    if not feature_flag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Feature Flag not found!"
        )

    db.delete(feature_flag)
    db.commit()
