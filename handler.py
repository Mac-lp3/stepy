import json
from functions.validate import validate_event

def validate(event, context):
    print("heres an event", event)
    print("heres the context", context.__dict__)
    response = validate_event(event, context)
    return response

def process(event, context):
    print("heres an event", event)
    print("heres the context", context.__dict__)
    return {
        "body": "been processed ty"
    }

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
