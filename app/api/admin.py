from fastapi import APIRouter
from app.services.lead import leads

router = APIRouter()

# Get all leads
@router.get("/leads")
def get_all_leads():
    return {
        "total_leads": len(leads),
        "data": leads
    }


# Filter leads by category
@router.get("/leads/{category}")
def get_leads_by_category(category: str):
    filtered = [l for l in leads if l.get("category", "").lower().startswith(category.lower())]

    return {
        "category": category,
        "count": len(filtered),
        "data": filtered
    }