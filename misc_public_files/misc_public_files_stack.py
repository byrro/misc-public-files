#! /usr/bin/python3.8 Python3.8
import aws_cdk.core as core
import aws_cdk.aws_s3 as aws_s3
import aws_cdk.aws_s3_deployment as aws_s3_deployment
import aws_cdk.aws_cloudfront as aws_cloudfront


class MiscPublicFilesStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        static_bucket = aws_s3.Bucket(
            self,
            'MiscPublicFilesBucket',
            removal_policy=core.RemovalPolicy.RETAIN,
        )

        origin = aws_cloudfront.OriginAccessIdentity(
            self,
            'MiscPublicFilesOrigin',
            comment='CDN origin for miscellaneous public files',
        )

        cdn = aws_cloudfront.CloudFrontWebDistribution(
            self,
            'MiscPublicFilesCDN',
            comment='CDN for miscellaneous public files',
            origin_configs=[
                aws_cloudfront.SourceConfiguration(
                    s3_origin_source=aws_cloudfront.S3OriginConfig(
                        s3_bucket_source=static_bucket,
                        origin_access_identity=origin,
                    ),
                    behaviors=[
                        aws_cloudfront.Behavior(
                            is_default_behavior=True,
                            min_ttl=core.Duration.days(90),
                            max_ttl=core.Duration.days(360),
                            default_ttl=core.Duration.days(180),
                            compress=True,
                        )
                    ],
                )
            ],
            default_root_object='index.html',
            enable_ip_v6=True,
            http_version=aws_cloudfront.HttpVersion.HTTP2,
            price_class=aws_cloudfront.PriceClass.PRICE_CLASS_100,
            viewer_protocol_policy=aws_cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,  # NOQA
        )

        aws_s3_deployment.BucketDeployment(
            self,
            'MiscPublicFilesDeployment',
            sources=[aws_s3_deployment.Source.asset('public')],
            destination_bucket=static_bucket,
            distribution=cdn,
        )
