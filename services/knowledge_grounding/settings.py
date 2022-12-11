import os
import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

SENTRY_DSN = os.getenv("SENTRY_DSN")
MODEL_CKPT = os.getenv("MODEL_CKPT", "1_sent_48_epochs")
INIT_MODEL_PATH = f"/opt/conda/lib/python3.7/site-packages/data/models/topical_chat_blender90_{MODEL_CKPT}/model.checkpoint"
MODEL_PATH = f"/opt/conda/lib/python3.7/site-packages/data/models/topical_chat_blender90_{MODEL_CKPT}/model"
