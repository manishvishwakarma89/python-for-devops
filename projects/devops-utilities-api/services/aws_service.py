import boto3
import sys
from datetime import datetime, timezone,timedelta
from botocore.exceptions import BotoCoreError, ClientError

OLD_INSTANCE_THRESHOLD_DAYS = 30
OUTPUT_FILE = "ec2_report.json"
DRY_RUN = False  # Set to True to simulate termination without actually doing it

def get_bucket_info():
    s3_client = boto3.client("s3")

    buckets = s3_client.list_buckets()["Buckets"]
    current_date = datetime.now(timezone.utc).astimezone()
    new_buckets = []
    old_buckets = []
    for bucket in buckets:
        bucket_name = bucket["Name"]
        creation_date = bucket["CreationDate"]
        days_ago_30 = current_date - timedelta(days=30)
        if creation_date < days_ago_30:
            old_buckets.append(bucket_name)
        else:
            new_buckets.append(bucket_name)

    return {
        "total_buckets":len(buckets),
        "new_buckets":len(new_buckets),
        "old_buckets":len(old_buckets),
        "new_buckets_names":new_buckets,
        "old_buckets_names":old_buckets
    }

def get_ec2_info():
    ec2_client= boto3.client("ec2")
    instances = ec2_client.describe_instances()
    instance_info = []
    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            instance_info.append({
                "InstanceID":instance["InstanceId"],
                "InstanceType":instance["InstanceType"],
                "State":instance["State"]["Name"],
                "LaunchTime":instance["LaunchTime"].strftime("%Y-%m-%d %H:%M:%S")      
            })
    return {
        "total_instances":len(instance_info),
        "instances":instance_info
    }
def terminate_old_instances():
    ec2_client= boto3.client("ec2")
    instances = ec2_client.describe_instances()
    current_date = datetime.now(timezone.utc).astimezone()
    old_instances = []
    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            launch_time = instance["LaunchTime"]
            days_ago_30 = current_date - timedelta(days=OLD_INSTANCE_THRESHOLD_DAYS)
            if launch_time < days_ago_30:
                old_instances.append(instance["InstanceId"])
            if DRY_RUN:
                print(f"Dry Run: Would terminate instance {instance['InstanceId']} launched on {launch_time}")
            else:
                try:
                    ec2_client.terminate_instances(InstanceIds=[instance["InstanceId"]])
                    print(f"Terminated instance {instance['InstanceId']} launched on {launch_time}")
                except (BotoCoreError, ClientError) as e:
                    print(f"Error terminating instance {instance['InstanceId']}: {e}", file=sys.stderr)
    return {
        "total_old_instances":len(old_instances),
        "old_instances":old_instances
    }   

