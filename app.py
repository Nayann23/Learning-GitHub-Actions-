import json
import os
from datetime import datetime

run_info = {
    "trigger": os.getenv("GITHUB_EVENT_NAME", "unknown"),
    "repository": os.getenv("GITHUB_REPOSITORY", "unknown"),
    "workflow": os.getenv("GITHUB_WORKFLOW", "unknown"),
    "created_at": datetime.utcnow().isoformat()
}

with open("run_info.json", "w") as file:
    json.dump(run_info, file, indent=4)

print("run_info.json created successfully")
print(run_info)