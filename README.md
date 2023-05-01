# Scones-Unlimited
# Project Overview

Scones Unlimited, a logistics company, is looking for an image classification model to help with their operations. The task was to build an image classification model that can automatically detect whether delivery drivers have a bicycle or a motorcycle, and route them accordingly. 

This project will be built using AWS Sagemaker, with the model being deployed using AWS Lambda functions and AWS Step Functions. The end goal is to create a scalable and safe model that can meet demand, while also monitoring for drift and degraded performance. 

## Project Steps Overview
1. **Data Staging**: Prepare and stage the data required for training the model
2. **Model Training and Deployment**: Train and deploy the image classification model using AWS Sagemaker
3. **Lambdas and Step Function Workflow**: Create Lambda functions and use AWS Step Functions to compose the model and services into an event-driven application
4. **Testing and Evaluation**: Test and evaluate the performance of the model
5. **Optional Challenge**: Implement additional features or improvements to the model
6. **Cleanup Cloud Resources**: Cleanup the AWS resources used in the project to avoid incurring further costs

## Background
Image classification is a powerful technique used in computer vision to identify the content of an image. It has a broad range of applications, from advanced technologies like autonomous vehicles and augmented reality, to eCommerce platforms and diagnostic medicine. 

As an MLE, it is important to ship a scalable and safe model. This means that the model should be able to scale to meet demand, and safeguards should be in place to monitor and control for drift or degraded performance. This project provides an opportunity to build and compose scalable, ML-enabled AWS applications. 

## Project Introduction
This project focuses on building an image classification model to detect the type of vehicle delivery drivers have. This will help Scones Unlimited optimize their operations by assigning delivery professionals who have a bicycle to nearby orders, and giving motorcyclists orders that are farther away. The project will also detect defects in the scones and detect people and vehicles in video feeds from roadways. 

## Repository Information
This repository contains all the files required for the project submission. The files include the image classification model code, the AWS Lambda functions, and the AWS Step Functions that compose the model and services into an event-driven application. 

