"""Minio client implementation."""

import io
from logging import Logger

import aioboto3
from pydantic import AnyUrl, PositiveInt, SecretStr


from app.pkg.logger import get_logger


class MinioClient:
    """Minio client."""

    __logger: Logger = get_logger(__name__)
    __s3_session: aioboto3.Session
    __access_key_id: SecretStr
    __secret_access_key: SecretStr
    __endpoint_url: AnyUrl
    __bucket_name: str

    def __init__(
        self,
        access_key_id: SecretStr,
        secret_access_key: SecretStr,
        host: str,
        port: PositiveInt,
        bucket_name: str,
    ):

        self.__access_key_id = access_key_id
        self.__secret_access_key = secret_access_key
        self.__endpoint_url = f"{host}:{port}"
        self.__bucket_name = bucket_name
        self.__s3_session = aioboto3.Session()

    async def upload_file_to_bucket(
        self,
        file: bytes,
        filename: str,
    ):
        """Upload file to bucket."""

        async with self.__s3_session.client(
            "s3",
            endpoint_url=self.__endpoint_url,
            aws_access_key_id=self.__access_key_id.get_secret_value(),
            aws_secret_access_key=self.__secret_access_key.get_secret_value(),
        ) as client:

            await client.upload_fileobj(
                file,
                self.__bucket_name,
                filename,
            )

    async def download_file_from_bucket(
        self,
        destination: io.BytesIO,
        key: str,
    ):
        """Download file from bucket."""

        async with self.__s3_session.client(
            "s3",
            endpoint_url=self.__endpoint_url,
            aws_access_key_id=self.__access_key_id.get_secret_value(),
            aws_secret_access_key=self.__secret_access_key.get_secret_value(),
        ) as client:
            await client.download_fileobj(
                self.__bucket_name,
                key,
                destination,
            )

    async def generate_presigned_url(
        self,
        key: str,
        expiration: PositiveInt = 3600,
    ) -> str:
        """Generate a presigned URL for an object in the bucket."""

        async with self.__s3_session.client(
            "s3",
            endpoint_url=self.__endpoint_url,
            aws_access_key_id=self.__access_key_id.get_secret_value(),
            aws_secret_access_key=self.__secret_access_key.get_secret_value(),
        ) as client:
            url = await client.generate_presigned_url(
                "get_object",
                Params={"Bucket": self.__bucket_name, "Key": key},
                ExpiresIn=expiration,
            )
            return url
