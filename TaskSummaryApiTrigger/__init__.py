import json
import logging
import azure.functions as func

from services.task_service import get_task_summary
from config import Config


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info("Task summary API triggered")

    team_name = req.params.get("team")

    # Validate query parameter
    if not team_name:
        return func.HttpResponse(
            "Please provide team query parameter",
            status_code=400
        )

    response = get_task_summary(team_name)

    response["environment"] = Config.ENV
    response["application"] = Config.APP_NAME

    return func.HttpResponse(
        json.dumps(response),
        mimetype="application/json",
        status_code=200
    )