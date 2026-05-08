from datetime import datetime

# Mock task data for task summary simulation
mock_tasks = [
    {"id": 1, "team": "backend", "status": "completed"},
    {"id": 2, "team": "backend", "status": "pending"},
    {"id": 3, "team": "backend", "status": "completed"},
    {"id": 4, "team": "frontend", "status": "pending"},
    {"id": 5, "team": "frontend", "status": "completed"},
]


def get_task_summary(team_name):
    filtered_tasks = [t for t in mock_tasks if t["team"] == team_name]

    total_tasks = len(filtered_tasks)

    completed_tasks = len(
        [t for t in filtered_tasks if t["status"] == "completed"]
    )

    pending_tasks = len(
        [t for t in filtered_tasks if t["status"] == "pending"]
    )

    return {
        "team": team_name,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "generated_at": datetime.utcnow().isoformat()
    }


def cleanup_stale_tasks():
    stale_tasks = [t for t in mock_tasks if t["status"] == "pending"]

    return {
        "stale_tasks_found": len(stale_tasks),
        "cleanup_run_at": datetime.utcnow().isoformat()
    }