import boto3

# When running on SageMaker, need execution role
from sagemaker import get_execution_role
role = get_execution_role()

# Declare bucket name, remote file, and destination
my_bucket = 'bucket_name'
orig_file = 'folder-name/sub-folder-name/file-name.zip'
dest_file = '/root/destination_folder-name/destination_sub-folder-name/file-name.zip'

# Connect to S3 bucket and download file
s3 = boto3.resource('s3')
s3.Bucket(my_bucket).download_file(orig_file, dest_file)
print("Done!")
