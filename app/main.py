from fastapi import FastAPI, HTTPException, Depends
from app.load_service import get_load_by_reference
from app.validation import validate_reference_number, get_api_key

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/loads/{reference_number_input}")
def get_load(
    api_key: str = Depends(get_api_key),
    validated_ref_number: str = Depends(validate_reference_number)
):
    load = get_load_by_reference(validated_ref_number)
    if not load:
        raise HTTPException(status_code=404, detail=f"Load not found for reference: {validated_ref_number}")
    return load
