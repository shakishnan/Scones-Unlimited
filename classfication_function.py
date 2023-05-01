#classfication_function
import json
import base64
import boto3

# Using client representing Amazon SageMaker Runtime ( To invoke endpoint)
runtime_client = boto3.client('sagemaker-runtime')                   

# name of deployed model
ENDPOINT = "image-classification-2023-05-01-13-17-24-538"

def lambda_handler(event, context):
    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])
    
    # Send the image to the SageMaker endpoint 
    response = runtime_client.invoke_endpoint(
        EndpointName=ENDPOINT,    # Endpoint Name
        Body=image,               # Decoded Image Data as Input (class:'Bytes') Image Data
        ContentType='image/png'   # Type of input 
    )
    
    # Decode the response from the SageMaker endpoint
    inferences = json.loads(response['Body'].read().decode('utf-8'))
  
    # We return the data back to the Step Function    
    event['body']['inferences'] = inferences               
    return {
        'statusCode': 200,
        'body': event['body']
    }