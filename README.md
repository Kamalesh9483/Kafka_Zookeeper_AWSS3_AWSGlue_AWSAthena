# ETL Data Engineering Project
### This project demonstrates a comprehensive Extract, Transform, Load (ETL) pipeline using modern data engineering tools and services. The goal is to illustrate the flow of data from producers to consumers, its storage in AWS S3, and subsequent SQL querying using AWS Athena.

![image](https://github.com/user-attachments/assets/bb88305a-a2e2-4c19-a49b-6bdefd150549)

https://github.com/user-attachments/assets/0ee8811d-9d44-472c-b7b7-11e04c67f509

## Tools used:
### 1. Kafka & Zookeeper
### 2. AWS EC2
### 3. AWS Glue, Crawler
### 4. AWS Athena

## Project Flow
## 1. Data Production and Consumption:
### Data is produced and sent to Kafka topics by producers.
### Consumers receive the data from Kafka topics.

## 2. Data Storage:
### Data is stored in Amazon S3 buckets for persistent storage ### and further processing.

## 3. Data Transformation and Cataloging:
### AWS Glue performs data transformation tasks, cleaning, and 
### structuring data as needed.
### AWS Glue Crawler is used to discover and catalog metadata from the data ### stored in S3.

## 4. Data Querying:
### AWS Athena is used to perform SQL queries on the data stored in S3, ### enabling analysis and reporting.




