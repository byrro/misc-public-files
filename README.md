
# Miscellaneous Public Files

This repo is used to share miscellaneous files publicly for whatever purposes come to mind.

This is a [CDK project](https://aws.amazon.com/cdk/) hosted on AWS [S3](https://aws.amazon.com/s3/) and [Cloudfront](https://aws.amazon.com/cloudfront/). The Cloudfront distribution root URL is: [d20p74l5mne5au.cloudfront.net](https://d20p74l5mne5au.cloudfront.net/).

Changes to `master/public` directory are uploaded to S3 and also invalidate Cloudfront cache automatically.

To redeploy the entire app on AWS, follow these steps:

Make sure you have Python 3.6+, pip, nodejs, and the [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#getting_started_install) installed.

1. Fork/clone the repo and `cd misc-public-files`
1. Run `pip install -r requirements.txt`
1. Create a `secret.py` file at the root directory and declare two variables: `AWS_ACCOUNT_ID` (e.g. "123456789000") and `AWS_REGION` (e.g. "us-west-2") - this information is used in `app.py`
1. Run `cdk deploy`
