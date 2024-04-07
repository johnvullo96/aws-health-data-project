CREATE EXTERNAL TABLE `customer_trusted`(
  `serialnumber` string, 
  `sharewithpublicasofdate` bigint, 
  `birthday` string, 
  `registrationdate` bigint, 
  `sharewithresearchasofdate` bigint, 
  `customername` string, 
  `sharewithfriendsasofdate` bigint, 
  `email` string, 
  `lastupdatedate` bigint, 
  `phone` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://jv-stedi-project/customer/trusted/'
TBLPROPERTIES (
  'CreatedByJob'='STEDI_Customer Landing to Trusted', 
  'CreatedByJobRun'='jr_b269ce88337e335ef8a0ce9e795f1d289884636d40124d5747211f19ac2a541d', 
  'classification'='parquet', 
  'useGlueParquetWriter'='true')
