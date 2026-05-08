# Azure Task Monitoring Function App

## Project Overview

This project is a Python-based Azure Function App developed to demonstrate the implementation of:

- HTTP Trigger
- Timer Trigger
- GitHub Actions CI/CD deployment
- Azure Deployment Center integration
- Application Insights monitoring

The application simulates a simple task monitoring system that provides task summary details through an API and performs scheduled cleanup operations using a timer-based trigger.

---

# Features Implemented

## 1. TaskSummaryApiTrigger (HTTP Trigger)

This trigger exposes an API endpoint that:

- Accepts a query parameter (`team`)
- Returns task summary details in JSON format
- Performs basic request validation
- Logs request execution details

### Sample Endpoint

```bash
GET /api/TaskSummaryApiTrigger?team=backend

Sample Response

{
    "team": "backend",
    "total_tasks": 2,
    "completed_tasks": 1,
    "pending_tasks": 1,
    "generated_at": "2026-05-07T12:43:41.579991",
    "environment": "local",
    "application": "TaskMonitorFunctionApp"
}

2. TaskCleanupSchedulerTrigger (Timer Trigger)

This trigger executes automatically based on a CRON schedule.

Functionality
Simulates stale task cleanup process
Logs cleanup execution details
Demonstrates scheduled background processing using Azure Functions

"schedule": "0 */5 * * * *"

Run at second 0, every 5 minutes