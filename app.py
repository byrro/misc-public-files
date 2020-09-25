#!/usr/bin/python3.8 python3

from aws_cdk import core

from misc_public_files.misc_public_files_stack import MiscPublicFilesStack

from secret import AWS_ACCOUNT_ID, AWS_REGION


app = core.App()
MiscPublicFilesStack(
    app,
    "misc-public-files",
    env=core.Environment(
        account=AWS_ACCOUNT_ID,
        region=AWS_REGION,
    ),
)

app.synth()
