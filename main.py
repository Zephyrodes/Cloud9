from fastapi import FastAPI
import boto3

app = FastAPI()

# Cliente de S3 (usa credenciales de AWS configuradas en EC2/Cloud9 con `aws configure`)
s3_client = boto3.client("s3")

@app.get("/")
def root():
    return {"message": "API de S3 con FastAPI 🚀"}

@app.get("/buckets")
def listar_buckets():
    try:
        response = s3_client.list_buckets()
        buckets = [bucket["Name"] for bucket in response["Buckets"]]
        return {"buckets": buckets}
    except Exception as e:
        return {"error": str(e)}

