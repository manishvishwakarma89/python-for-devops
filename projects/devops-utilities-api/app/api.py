from fastapi import FastAPI # Importing FastAPI Class
from routers import metrics, aws

app = FastAPI(
    title="Internal DevOps Utilities API",
    description="This is an Internal API Utitlities App for Monitoring metrics, AWS Usage, Log Analysis, etc",
    version="1.1.0",
    doc_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
def hello():
    """
    This is a Hello API , just for testing
    """
    return {"message":"Hello, This is DevOps Utilites API for Monitoring metrics, AWS Usage, Log Analysis for system admin tasks"}

app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws")