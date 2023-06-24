import os

from sys import argv

from uploader.upload import upload_to_s3
from uploader.logger import logger

from uploader.settings import AWS_S3_BUCKET_NAME


def main():
    if len(argv) < 2:
        return

    filepath = os.path.abspath(argv[1])
    while not os.path.exists(filepath):
        filepath = input("アップロードするファイルのパスを入力してください：")

    logger.info(f"開始：{filepath}を{AWS_S3_BUCKET_NAME}にアップロード")
    upload_to_s3(filepath)
    logger.info(f"終了：{filepath}を{AWS_S3_BUCKET_NAME}にアップロード")


if __name__ == "__main__":
    main()
