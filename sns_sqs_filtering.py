import boto3


# Create an SNS client
sns_client = boto3.client(
    "sns",
    aws_access_key_id="***********",
    aws_secret_access_key="***********",
    region_name="eu-central-1"
)

# Create SNS topic
topic = sns_client.create_topic(Name="notifications")['TopicArn']
topic_arn = topic['TopicArn']  # get its Amazon Resource Name

subscription_arn = sns_client.subscribe(
    TopicArn = topic_arn,
    Protocol = 'sqs',
    Endpoint = ''
)['SubscriptionArn']

sns_client.set_subscription_attributes(
    SubscriptionArn = subscription_arn,
    AttributeName = 'FilterPolicy',
    AttributeValue = '{"event_type": ["email_notification", "client_notification"]}'
)

# create message up to 10 attributes
message = '{"notification": {"id": 1, "email_text": "welcome to archii"}'


response = sns_client.publish(
    TopicArn = topic_arn,
    Subject = 'New user',
    Message = message,
    MessageAttributes = {
        'event_type': {
            'DataType': 'String',
            'StringValue': 'email_notification'
        }
    }
)

print("Response: {}".format(response))