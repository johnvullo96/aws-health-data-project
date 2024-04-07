# Project: STEDI-Human-Balance-Analytics

## Project Summary

The following projects processes step trainer application data using AWS S3, Glue, and Athena. Raw application is taken from fragmented JSON files, loaded into AWS S3 buckets, and processed using AWS Glue and Spark to create a data lakehouse ready to be used for analytics and machine learning.

## Background and Application Context

The STEDI step trainer was created with the following components:

* Trains the user to do a STEDI balance exercise.
* Has sensors on the device that collect data to train a machine-learning algorithm to detect steps.
* Has a companion mobile app that collects customer data and interacts with the device sensors.

The Step Trainer is a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions.

The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used. Some of the early adopters have agreed to share their data for research purposes. Only these customers’ Step Trainer and accelerometer data should be used in the training data for the machine learning model.

## Source Data & Data Lakehouse Creation

### Landing Zone

#### Customer

Table Name: customer_landing

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

Table Name: accelerometer_landing

Source: Mobile app data.

Fields:
* timeStamp
* user 
* x
* y
* z

#### Step Trainer

Table Name: step_trainer_landing

Source: Motion sensor data from wearable device.

Fields:
* sensorReadingTime
* serialNumber
* distanceFromObject

### Trusted Zone

#### Customer

Table Name: customer_trusted

customer_landing_to_trusted.py filters customer landing dataset where sharewithresearchasofdate is true to create trusted customers dataset containing only the customer data from customers who have agreed to share their data for research.

#### Accelerometer

Table Name: accelerometer_trusted

accelerometer_landing_to_trusted.py joins accelerometer_landing with customer_trusted using the email/username to create a trusted accelerometer dataset containing only the accelerometer data from customers who have agreed to share their data for research.

#### Step Trainer

Table Name: step_trainer_trusted

step_trainer_landing_to_trusted.py joins step_trainer_landing with customer_curated using the serial number of the step trainer device to create a trusted step trainer dataset containing only the step trainer data from customers who have agreed to share their data for research.

### Curated Zone

#### Customer

Table Name: customer_curated

customer_trusted_to_curated.py joins customer_trusted with accelerometer_trusted using the email/username to create a curated dataset of customers who have agreed to share their data for research purposes and have accelerometer data.

#### Machine Learning

Table Name: machine_learning_curated

step_trainer_trusted_to_curated.py joins step_trainer_trusted and accelerometer_trusted using the user and timestamp of the step trainer and accelerometer data. The resulting dataset shows a combined view of the accelerometer and step trainer data at a certain timestamp for customers who have agreed to share their data for research purposes.







