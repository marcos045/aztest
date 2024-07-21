import datetime
# import os
# import uuid
from flask import Flask, render_template, request
# from pymongo import MongoClient
# from azure.storage.blob import BlobServiceClient
# from dotenv import load_dotenv
# from werkzeug.utils import secure_filename

# load_dotenv()

entry = []
app = Flask(__name__)

# Azure Cosmos DB for MongoDB API setup
# mongodb_uri = os.getenv("MONGODB_URI")
# print(mongodb_uri)
# client = MongoClient(mongodb_uri)
# app.db = client.get_database("microblog")  # Replace with your database name

# Azure Blob Storage setup
# connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
# blob_service_client = BlobServiceClient.from_connection_string(connect_str)
# container_name = "images"
# container_client = blob_service_client.get_container_client(container_name)
# if not container_client.exists():
#     container_client.create_container(public_access="container")
# app.blob_container_client = container_client

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        image = request.files.get("image")
        
        formatted_date1 = datetime.datetime.utcnow().strftime("%Y-%m-%d")
        formatted_date2 = datetime.datetime.utcnow().strftime("%b-%d")
        
        entry_data = {
            "content": entry_content,
            "date": formatted_date1,
            "show_date": formatted_date2
        }
        
        entry.append(entry_data)
        # if image:
        #     original_filename = secure_filename(image.filename)
        #     unique_filename = f"{uuid.uuid4()}_{original_filename}"
        #     blob_client = app.blob_container_client.get_blob_client(unique_filename)
        #     blob_client.upload_blob(image)
        #     entry_data["image_url"] = blob_client.url
        #     print(f"Image uploaded successfully. URL: {entry_data['image_url']}")

        # app.db.entries.insert_one(entry_data)  # Use the collection name (e.g., 'entries')

    entries = [
        (
            item["content"],
            item["date"],
            item["show_date"],
        )
        for item in entry  # Use .find() for MongoDB queries
    ]
    return render_template("index.html", entries=entries)

if __name__ == '__main__':
    app.run(debug=True)