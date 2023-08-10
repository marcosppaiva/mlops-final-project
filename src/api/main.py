import logging

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse

from src.entities.models import Imovel
from src.utils.predictions_utils import predict, load_model, save_predictions

logging.basicConfig(
    level=logging.INFO, format='FASTAPI_APP - %(asctime)s - %(levelname)s - %(message)s'
)


try:
    model, preprocessor, run_id = load_model()
except IndexError as index_error:
    raise HTTPException(
        status_code=500, detail='There is no model to load. Check you mlflow register'
    ) from index_error

app = FastAPI()


@app.get("/")
async def alive():
    return {"message": "alive"}


@app.post('/predict')
async def predict_endpoint(
    imovel: Imovel, background_tasks: BackgroundTasks
) -> JSONResponse:
    try:
        price_predict, df_data = predict(imovel, model, preprocessor)

        df_data['price_predicted'] = round(price_predict[0])  # type: ignore
        df_data['model_version'] = run_id

        background_tasks.add_task(save_predictions, df_data)

        return JSONResponse(content={'predictions': df_data.to_json()})

    except Exception as error:
        logging.error(error, exc_info=True)
        raise HTTPException(status_code=500, detail=f'{str(error)}') from error
