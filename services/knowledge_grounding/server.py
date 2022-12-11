import logging
import time

import sentry_sdk
from fastapi import FastAPI

import schema
from service import KnowledgeGroundingService
from settings import SENTRY_DSN, MODEL_PATH, INIT_MODEL_PATH, MODEL_CKPT


logger = logging.getLogger(__name__)

sentry_sdk.init(dsn=SENTRY_DSN, traces_sample_rate=1.0)

kg_service = KnowledgeGroundingService(model_path=MODEL_PATH, init_model_path=INIT_MODEL_PATH)

logger.info(f"knowledge grounding model {MODEL_CKPT} is set to run on {kg_service.cuda_device}")


app = FastAPI()


@app.post("/respond")
def respond(batch_req: schema.BatchRequest):
    st_time = time.time()
    responses = []

    try:
        responses = kg_service.perform(batch_req.batch)
        logger.info(f"Current sample responses: {responses}")
    except Exception as e:
        sentry_sdk.capture_exception(e)
        logger.exception(e)

    total_time = time.time() - st_time
    logger.info(f"knowledge grounding one batch exec time: {total_time:.3f}s")

    return responses
