"""
Vegetables Catalog Router
Provides access to scientific profiles, planting guides, and maturity schedules.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.data.vegetable_database import VEGETABLE_DATA, get_vegetable_by_id, search_vegetables

router = APIRouter(prefix="/api/vegetables", tags=["Vegetables"])

@router.get("")
async def list_vegetables(query: Optional[str] = Query(None, description="Search by common or scientific name")):
    if query:
        return search_vegetables(query)
    return VEGETABLE_DATA

@router.get("/families")
async def list_families():
    families = set(veg["family"] for veg in VEGETABLE_DATA)
    return sorted(list(families))

@router.get("/{veg_id}")
async def get_vegetable(veg_id: str):
    veg = get_vegetable_by_id(veg_id)
    if not veg:
        raise HTTPException(status_code=404, detail=f"Vegetable '{veg_id}' not found in catalog.")
    return veg
