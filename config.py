import os

class Config:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    CHECKPOINT_DIR = os.path.join(ROOT_DIR, "checkpoints")
    MODEL_PATH = os.path.join(CHECKPOINT_DIR, "model-lr.pkl")
    LOG_PATH = os.path.join(CHECKPOINT_DIR, "model-log.log")

    TRAIN_PATH = os.path.join(ROOT_DIR, "virtual_singer_data.csv")
    TEST_PATH = os.path.join(ROOT_DIR, "virtual_singer_data.csv")

    IMG_DIR = os.path.join(ROOT_DIR, "images")