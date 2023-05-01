#serializeImageData

import json
import boto3
import base64

# Create a low-level client representing Amazon Simple Storage Service (S3)
s3 = boto3.client('s3')

def lambda_handler(event, context):
    """
    This function downloads an image file from S3 using the key and bucket 
    specified in the event input, reads the file as binary data, encodes the 
    binary data as base64, and returns the data as a response to the Step Function.
    """
    
    # Get the s3 key and bucket from the Step Function event input
    key = event['s3_key']
    bucket = event['s3_bucket']
    
    # Download the file from S3 to /tmp/image.png
    s3.download_file(bucket, key, "/tmp/image.png")
    
    # Read the binary data from the file and encode it as base64
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Print the event keys for debugging purposes
    print("Event:", event.keys())
    
    # Return a dictionary containing the image data, bucket, key, and an empty list of inferences
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,      # Bytes data
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }