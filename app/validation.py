from fastapi import HTTPException, Path, Depends

def validate_reference_number(
    reference_number_input: str = Path(
        ...,
        title="Load Reference Number",
        description="The reference number (e.g., REF12345 or 12345) of the load to retrieve."
    )
) -> str:
    """
    Validates and normalizes the reference number input.
    Accepts 5 digits (e.g., 12345) or 'REF' followed by 5 digits (e.g., REF12345).
    Returns the normalized reference number (REFXXXXX) or raises HTTPException.
    """
    if reference_number_input is None:
        raise HTTPException(status_code=500, detail="Internal validation error.")

    if reference_number_input.isdigit():
        if len(reference_number_input) == 5:
            return "REF" + reference_number_input
        else:
            raise HTTPException(
                status_code=400,
                detail="Invalid format: Numeric input must be exactly 5 digits."
            )
    elif reference_number_input.startswith("REF"):
        numeric_part = reference_number_input[3:]
        if numeric_part.isdigit() and len(numeric_part) == 5:
            return reference_number_input
        else:
            raise HTTPException(
                status_code=400,
                detail="Invalid format: Input starting with 'REF' must be followed by exactly 5 digits (e.g., REF12345)."
            )
    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid format: Input must be 5 digits (e.g., 12345) or start with 'REF' followed by 5 digits (e.g., REF12345)."
        )
