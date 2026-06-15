import boto3

def get_connnection(service):
    return boto3.client(service)

def show_buckets(s3_client):
    response = s3_client.list_buckets()
    for bucket in response['Buckets']:
        print(bucket['Name'])
def show_regions(s3_client):
    response = ec2.describe_regions()
    for region in response['Regions']:
        print(region['RegionName'])
        
def upload_file_to_bucket(s3_client,bucket_name,file_name,key_name):
    try:
        response = s3_client.upload_file(file_name, bucket_name, key_name)
    except Exception as e:
        print(f"Error occurred while uploading file {file_name} to bucket {bucket_name}: {e}")
        return None

    print(f"File {file_name} uploaded successfully to bucket {bucket_name} with key {key_name}.")
    return response

def create_bucket(s3_client, bucket_name):
    try:
        response = s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-2',
        }
        )
    except Exception as e:
        print(f"Error occurred while creating bucket {bucket_name}: {e}")
        return None

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:       
        print(f"Bucket {bucket_name} created successfully.")
    else:
        print(f"Failed to create bucket {bucket_name}.")   

    print(response)
    return response

    
s3=get_connnection("s3")
ec2=get_connnection("ec2")



show_buckets(s3)
show_regions(ec2)
create_bucket(s3, "daikat-bucket-2026")
upload_file_to_bucket(s3, "rehman-bucket-2026", "output1.json", "outputs.json")
