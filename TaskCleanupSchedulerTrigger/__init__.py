import logging
import datetime

from services.task_service import cleanup_stale_tasks


def main(mytimer) -> None:

    logging.info("Task cleanup scheduler started")

    # Scheduled cleanup execution
    cleanup_result = cleanup_stale_tasks()

    logging.info(f"Cleanup Result: {cleanup_result}")

    logging.info(
        f"Scheduler completed at {datetime.datetime.utcnow().isoformat()}"
    )