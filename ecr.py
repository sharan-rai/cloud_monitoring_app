import boto3

ecr_client = boto3.client('ecr')
repsitory_name = "cloud-native-repo"
response = ecr_client.create_repository(repositoryName = repsitory_name)

respository_uri = response['repository']['repositoryUri']
print(respository_uri)