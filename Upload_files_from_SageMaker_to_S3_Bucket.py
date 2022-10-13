import sagemaker


s3_path_to_data = sagemaker.Session().upload_data(bucket='bucket-name', 
                                                  path='/root/local_folder-path/local_sub-folder-path/local_sub-folder-path/file-name.txt', 
                                                  key_prefix='sub-folder-name')
