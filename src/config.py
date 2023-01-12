import os
import json
from logging import Logger

from dotenv import load_dotenv

load_dotenv()


PROJECT_NAME = "RL_PROJECT"
PROJECT_ROOT = os.getenv("RL_PROJECT_PATH")
DATA_PATH = os.path.join(PROJECT_ROOT, "data/")

with open(os.path.join(PROJECT_ROOT, "config.json")) as file:
    _config_dict = json.load(file)

_logger = Logger(PROJECT_NAME)


def log(meesage):
    _logger.log(meesage)
