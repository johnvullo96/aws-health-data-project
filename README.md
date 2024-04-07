# Project: STEDI-Human-Balance-Analytics

## Contents

## Project Overview

The following projects processes step trainer application data using AWS S3, Glue, and Athena.

Raw application is taken from fragmented JSON files, loaded into AWS S3 buckets, and processed using AWS Glue and Spark to create a data lakehouse ready to be used for analytics and machine learning.

## Data & Implementation

### Landing Zone

#### Customer

Source: Customer registration and order fulfillment data.

Fields:
* serialnumber
* sharewithpublicasofdate
* birthday
* registrationdate
* sharewithresearchasofdate
* customername
* email
* lastupdatedate
* phone
* sharewithfriendsasofdate

#### Accelerometer

Source: Mobile app data.

Fields:
* timeStamp
* user 
* x
* y
* z

#### Step Trainer

Source: Motion sensor data from wearable device.

Fields:
* sensorReadingTime
* serialNumber
* distanceFromObject

### Trusted Zone

#### Customer

Contains customers who have agreed to share their data for research purposes.

customer_landing_to_trusted.py filters customer landing dataset where sharewithresearchasofdate is true to create trusted customers dataset containing only the customer data from customers who have agreed to share their data for research.

#### Accelerometer

Contains accelerometer data from customers who have agreed to share their data for research.

accelerometer_landing_to_trusted.py joins accelerometer landing dataset with trusted customers dataset to create trusted accelerometer dataset containing only the accelerometer data from customers who have agreed to share their data for research.

#### Step Trainer

Contains step trainer data from customers who have agreed to share their data for research.

step_trainer_landing_to_trusted.py joins step trainer landing dataset with curated customers dataset to create trusted step trainer dataset containing only the step trainer data from customers who have agreed to share their data for research.

### Curated Zone

#### Customer

#### Machine Learning



