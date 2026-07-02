

def log_to_firestore(data):
    """
    Logs the provided data to Firestore.
    """
    from google.cloud import firestore

    db = firestore.Client()
    doc_ref = db.collection('logs').document()
    success = doc_ref.set(data)
    print(f"Logged data to Firestore with document ID: {doc_ref.id} and success status: {success}")
    return success
