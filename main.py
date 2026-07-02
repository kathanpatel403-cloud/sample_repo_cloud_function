import functions_framework

@functions_framework.cloud_event
def hello_pubsub(cloud_event):
    """
    Sample demo function to respond to a Pub/Sub message or cloud event.
    """
    print(f"Received event: {cloud_event}")
    return f"Hello, user! Got your event: {cloud_event}"
