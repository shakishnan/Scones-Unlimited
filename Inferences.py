#Inferences
import json

# Threshold for confidence level
THRESHOLD = 0.90

def lambda_handler(event, context):
    
    # Get the inferences from the event body
    inferences = event['body']['inferences']
    
    # Check if any value in the inferences list is above the threshold
    meets_threshold = max(inferences) > THRESHOLD
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        # Pass the event dictionary back out of the Step Function
        return {
            'statusCode': 200,
            'body': event
        }
    else:
        # End the Step Function with an error
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")
