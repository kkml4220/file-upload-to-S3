import os

from botocore.exceptions import ClientError

from uploader.logger import logger
from uploader.s3client import s3_client
from uploader.settings import AWS_S3_BUCKET_NAME


def get_file_basename(path):
    """ファイルのbasenameを取得"""
    return os.path.basename(path)


def upload_to_s3(filepath):
    """ファイルをS3にアップロード
    Args:
        filepath (str): アップロードするファイルのパス
    """
    basename = get_file_basename(filepath)
    try:
        s3_client.upload_file(filepath, AWS_S3_BUCKET_NAME, basename)
        logger.debug(f'File "{basename}" uploaded to S3.')
    except ClientError as e:
        logger.error(e)
