from datetime import datetime
import pytz




def halbwertszeit(N0, t_half, t):
    """
    Berechnet die verbleibende Menge nach Halbwertszeit.
    
    Formel: N(t) = N₀ · (1/2)^(t / t_half)
    
    Args:
        N0 (float): Anfangsmenge
        t_half (float): Halbwertszeit
        t (float): Verstrichene Zeit
    
    Returns:
        float: Verbleibende Menge
    """
    return N0 * (0.5) ** (t / t_half)


def berechne_zeit_bis_menge(N0, N, t_half):
    """
    Berechnet die Zeit, bis eine bestimmte Menge erreicht ist.
    
    Formel: t = t_half · log₂(N₀ / N)
    
    Args:
        N0 (float): Anfangsmenge
        N (float): Zielmenge
        t_half (float): Halbwertszeit
    
    Returns:
        float: Zeit bis zur Zielmenge
    """
    import math
    if N <= 0 or N > N0:
        raise ValueError("N muss zwischen 0 und N0 liegen")
    return t_half * math.log2(N0 / N)
 

