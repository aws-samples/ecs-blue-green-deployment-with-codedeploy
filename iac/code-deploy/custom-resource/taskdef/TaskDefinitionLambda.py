"""
Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import json
import cf_response
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
client = boto3.client('ecs')

def lambda_handler(event, context):
  logger.info('Event received:')
  logger.info(json.dumps(event, indent=2))
  responseData = {}
  physicalResourceId = ''
  try:
    request_type = event['RequestType']
    task_definition = event['ResourceProperties']['TaskDefinition']
    if request_type == 'Update':
        physicalResourceId = event['PhysicalResourceId']
        responseData['TaskDefinition'] = physicalResourceId
        print(responseData['TaskDefinition'])
    elif request_type == 'Create':
        responseData['TaskDefinition'] = task_definition
        physicalResourceId = task_definition
        print(responseData['TaskDefinition'])
    else:
      print("Did not recieve a create or update event, skipping.. ")
    
    cf_response.send(event, context, cf_response.SUCCESS, responseData, physicalResourceId)

  except Exception as e:
    print("ERROR creating the deployment, Error: %s" %(str(e)))
    cf_response.send(event, context, cf_response.FAILED, responseData, "CustomResourcePhysicalID")
