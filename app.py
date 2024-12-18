from fastapi import FastAPI
from routes.cambio_moneda import router as cambio_moneda_router
import uvicorn

#instancias de fastapi
app=FastAPI(
    title="Tasa de cambios API",
    description= "API que consume Frankfurter API para obtener tasas de cambio de divisas.",
    version="1.0.0")

app.include_router(cambio_moneda_router)

#ejecuta la app
if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

