import boto3

# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id="xxxxxxxx",
    aws_secret_access_key="xxxxxxxxx",
    region_name="us-west-1"
)

# Create the topic
topic = client.create_topic(Name="notifications")
topic_arn = topic['TopicArn']  # get its Amazon Resource Name

# Add email subscribers
client.subscribe(
    TopicArn=topic_arn,
    Protocol='email-json',
    Endpoint="contact@xxx.com"
)

# Publish a message.
client.publish(Message="First message !", TopicArn=topic_arn)
