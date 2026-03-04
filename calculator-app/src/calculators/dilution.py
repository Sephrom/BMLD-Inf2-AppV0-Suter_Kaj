def calculate_dilution(concentration1: float, volume1: float, concentration2: float) -> float:
    if concentration1 <= 0 or volume1 <= 0 or concentration2 <= 0:
        raise ValueError("Concentrations and volumes must be greater than zero.")
    
    volume2 = (concentration1 * volume1) / concentration2
    return volume2