import os
import json

from dotenv import load_dotenv

load_dotenv()

config = json.load(open(os.path.join(os.getenv("RL_PROJECT_ROOT"), "config.json")))

project_root = os.getenv("RL_PROJECT_ROOT")
