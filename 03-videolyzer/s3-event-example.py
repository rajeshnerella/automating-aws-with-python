# coding: utf-8
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2020-04-24T14:29:55.103Z', 'eventName': 'ObjectCreated:CompleteMultipartUpload', 'userIdentity': {'principalId': 'AWS:AIDA474AW6D4QS4KGBNGO'}, 'requestParameters': {'sourceIPAddress': '174.114.237.90'}, 'responseElements': {'x-amz-request-id': 'BE2C938DC43880EE', 'x-amz-id-2': '5HeF7UhlOgdHh33Iy/YuRN88e2EFB2VhONKiLKonb1g4Zit4ihODHg+LPnIYyaoEcU4RQCkqGLpscQXAhQbbA5SP0oD2szZO'}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '9b250bd9-3572-456c-b377-809f42b4cb97', 'bucket': {'name': 'rajeshvideolyzer12345', 'ownerIdentity': {'principalId': 'A2LKWX1QUVLVSA'}, 'arn': 'arn:aws:s3:::rajeshvideolyzer12345'}, 'object': {'key': 'Pexels+Videos+4640.mp4', 'size': 10278716, 'eTag': '6bcf2e76121ff9d1c3bf616c49650be7-2', 'sequencer': 
'005EA2F7E0002AE589'}}}]}
event
event['Records'][0]
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])