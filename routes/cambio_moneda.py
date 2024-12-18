from fastapi import APIRouter, HTTPException, Query
from services.services import get_latest_rates, get_historical_rates

router = APIRouter()

@router.get("/latest", summary="Obtener tasas de cambio actuales")
async def latest_rates(base: str = Query("USD", description="Moneda base"),
                       symbols: str = Query(None, description="Monedas destino separadas por coma")):
    """
    Devuelve las tasas de cambio actuales utilizando Frankfurter API.
    """
    try:
        rates = get_latest_rates(base=base, symbols=symbols)
        return rates
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/historical/{date}", summary="Obtener tasas de cambio históricas")
async def historical_rates(date: str,
                           base: str = Query("USD", description="Moneda base"),
                           symbols: str = Query(None, description="Monedas destino separadas por coma")):
    """
    Devuelve las tasas de cambio para una fecha específica.
    """
    try:
        rates = get_historical_rates(date=date, base=base, symbols=symbols)
        return rates
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
