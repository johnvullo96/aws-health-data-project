CREATE EXTERNAL TABLE `customer_curated`(
  `serialnumber` string COMMENT '', 
  `birthday` string COMMENT '', 
  `sharewithpublicasofdate` bigint COMMENT '', 
  `sharewithresearchasofdate` bigint COMMENT '', 
  `registrationdate` bigint COMMENT '', 
  `customername` string COMMENT '', 
  `sharewithfriendsasofdate` bigint COMMENT '', 
  `email` string COMMENT '', 
  `lastupdatedate` bigint COMMENT '', 
  `phone` string COMMENT '')
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://jv-stedi-project/customer/curated/'
TBLPROPERTIES (
  'CreatedByJob'='STEDI_Customer Curated', 
  'CreatedByJobRun'='jr_f76faff584c58ee6ac0c405c4e04925a7a5c71e58498373f2780ca0875f2531a', 
  'classification'='parquet', 
  'useGlueParquetWriter'='true')
