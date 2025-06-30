import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ContactForm')  # Replace with your table name

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        name = body.get("name")
        email = body.get("email")
        message = body.get("message")

        if not all([name, email, message]):
            raise ValueError("Missing required fields")

        table.put_item(
            Item={
                'email': email,
                'name': name,
                'message': message
            }
        )

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'message': 'Form submitted successfully'})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Internal Server Error'})
        }
