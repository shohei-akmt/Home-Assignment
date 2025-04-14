from fastapi import FastAPI, HTTPException, Path
from app.load_service import get_load_by_reference

app = FastAPI()

@app.get("/loads/{reference_number_input}")
# TODO: write the validation logic out
def get_load(
    reference_number_input: str = Path(
        ...,
        title="Load Reference Number",
        description="The reference number (e.g., REF12345 or 12345) of the load to retrieve."
    )
):
    validated_ref_number = None

    if reference_number_input.isdigit():
        if len(reference_number_input) == 5:
            validated_ref_number = "REF" + reference_number_input
        else:
            raise HTTPException(status_code=400, detail="Invalid format: Numeric input must be exactly 5 digits.")
    elif reference_number_input.startswith("REF"):
        numeric_part = reference_number_input[3:]
        if numeric_part.isdigit() and len(numeric_part) == 5:
            validated_ref_number = reference_number_input
        else:
            raise HTTPException(status_code=400, detail="Invalid format: REF input must be followed by exactly 5 digits.")
    else:
        raise HTTPException(status_code=400, detail="Invalid format: Input must be 5 digits (e.g., 12345) or start with 'REF' followed by 5 digits (e.g., REF12345).")    

    if validated_ref_number is None:
        raise HTTPException(status_code=500, detail="Internal validation error.") # should not be called but just in case

    load = get_load_by_reference(validated_ref_number)
    if not load:
        raise HTTPException(status_code=404, detail=f"Load not found for reference: {validated_ref_number}")
    return load
