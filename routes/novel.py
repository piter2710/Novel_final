from schemas.novel import NovelOut, NovelCreate, NovelUpdate
from models.novel import Novel as NovelModel
from fastapi import APIRouter, Depends, HTTPException
from database import database_connection
from starlette import status
from sqlalchemy import select, update, delete
router = APIRouter(prefix="/novels", tags=["Novels"])

@router.get("/", response_model=list[NovelOut])
async def get_all_novels(db: database_connection):
    stmt = select(NovelModel)
    results = await db.execute(stmt)
    novels = results.scalars().all()
    return novels

@router.get("/{novel_id}", response_model=NovelOut)
async def get_single_novel(novel_id: int, 
                           db: database_connection):
    stmt = select(NovelModel).where(NovelModel.novel_id == novel_id)
    results = await db.execute(stmt)
    novel = results.scalar_one_or_none()
    if not novel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Novel not found")
    return novel

@router.post("/", response_model=NovelOut, status_code=status.HTTP_201_CREATED)
async def create_novel(novel: NovelCreate,
                       db: database_connection):
    new_novel = NovelModel(**novel.model_dump())
    db.add(new_novel)
    await db.commit()
    await db.refresh(new_novel)
    return new_novel

@router.put("/{novel_id}", response_model=NovelOut)
async def update_novel(novel_id: int,
                       novel: NovelUpdate,
                       db: database_connection):
    stmt = update(NovelModel).where(NovelModel.novel_id == novel_id).values(**novel.model_dump(exclude_unset=True)).returning(NovelModel)
    results = await db.execute(stmt)
    updated_novel = results.scalar_one_or_none()
    if not updated_novel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Novel not found")
    await db.commit()
    return updated_novel

@router.delete("/{novel_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_novel(novel_id: int,
                       db: database_connection):
    stmt = delete(NovelModel).where(NovelModel.novel_id == novel_id)
    results = await db.execute(stmt)
    if results.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Novel not found")
    await db.commit()
    return None
