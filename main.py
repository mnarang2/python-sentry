from fastapi import FastAPI, HTTPException
import sentry_sdk
import random

# 🔧 Replace this with your actual DSN from Sentry project settings
sentry_sdk.init(
    dsn="https://a692f9696858fcc596a9de2c36fa4524@o4509388628361216.ingest.us.sentry.io/4509388634062848",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profile_session_sample_rate to 1.0 to profile 100%
    # of profile sessions.
    profile_session_sample_rate=1.0,
    # Set profile_lifecycle to "trace" to automatically
    # run the profiler on when there is an active transaction
    profile_lifecycle="trace",
)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Peppy Gold - Bug Finder Agent!"}

@app.get("/trigger-error")
def trigger_error():
    # Simulate a random bug
    options = ["divide_by_zero", "key_error", "type_error"]
    bug_type = random.choice(options)

    if bug_type == "divide_by_zero":
        return 1 / 0  # ZeroDivisionError
    elif bug_type == "key_error":
        return {"name": "Aarav"}["age"]  # KeyError
    elif bug_type == "type_error":
        return len(None)  # TypeError

    return {"status": "No bug this time.Yippeee"}
