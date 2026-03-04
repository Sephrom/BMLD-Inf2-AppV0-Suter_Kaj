def calculate_bmi(weight: float, height: float) -> float:
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    bmi = weight / (height ** 2)
    return round(bmi, 2)