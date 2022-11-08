# Blue/Green Deployment for ECS Fargate application using CloudFormation and CodePipeline

This repository provides a solution for orchestrating Blue/Green deployment for ECS Fargate based application using AWS CodeDeploy. The solution consists of a CodePipeline to build, validate, deploy infrastructure and deploy application on ECS Fargate cluster using AWS CodeDeploy. The artifacts provides as part of this repository can be used by applications teams as a reference solution to setup a blue/green deployment pipeline for their application running on ECS Fargate.

## Architecture

![Diagram](images/CodeDeploy_BlueGreen_ECSFargate-CICD-Pipeline.jpg)

## Solution Deployment

### Deployment Prerequisites
1. VPC with atleast two public and two private subnets. 
2. Route53 public hosted zone available in the account where the application will be deployed
3. Amazon Certificate Manager (ACM) certificate valid for the Route53 domain created in step 2.
4. Email address where application alerts will be sent to

### Depolyment steps
1. Ensure that you have setup everything that is listed in the pre-requisites section
2. Download source code from this repo
2. Update the ecs-bg-params.json under iac/app/params folder with the values for resources listed in the pre-requisite section
4. Deploy the CodePipeline CloudFormation template under iac/pipeline/code-pipeline.yaml
5. The above CodePipeline template will create a Code Commit repository. Retrieve the repository clone url from the output of the CodePipeline stack deployed in step #4
6. Push the updated code to this code commit repository which will trigger the code pipeline. Wait till pipeline successfully deploys and then verify the application is functional by going to the application URL. The application URL can be obtained from the Output of the CloudFormation application infrastructure stack (ecsfargate-sampleapp-infra-stack) that is deployed by Code pipeline execution.

