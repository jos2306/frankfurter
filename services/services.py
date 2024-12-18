import requests


BASE_URL = "https://api.frankfurter.dev"

def get_latest_rates(base: str = "USD", symbols: str = ""):
    """Obtiene las tasas de cambio más recientes."""
    url = f"{BASE_URL}/v1/latest"
    params = {"base": base}
    if symbols:
        params["symbols"] = symbols
    
    response = requests.get(url, params=params)
    response.raise_for_status()  # Lanza excepción si falla la solicitud
    return response.json()

def get_historical_rates(date: str, base: str = "USD", symbols: str = ""):
    """Obtiene tasas de cambio históricas para una fecha específica."""
    url = f"{BASE_URL}/v1/{date}"
    params = {"base": base}
    if symbols:
        params["symbols"] = symbols

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
