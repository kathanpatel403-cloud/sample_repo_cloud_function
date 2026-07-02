import functions_framework

from app.service import log_to_firestore

@functions_framework.cloud_event
def hello_pubsub(cloud_event):
    """
    Sample demo function to respond to a Pub/Sub message or cloud event.
    """
    print(f"Received event: {cloud_event}")
    
    data = cloud_event.data
    print("Data received:", data)

    bucket_name = data["bucket"]
    file_name = data["name"]
    print(f"Processing file: {file_name} from bucket: {bucket_name}")

    return log_to_firestore({
        "bucket": bucket_name,
        "file": file_name
    })
