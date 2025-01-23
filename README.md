# nyc_taxi_data_analysis

|Column|Description|Figure|
|------|---|---|
|VenderID|A code indicating the TPEP provider that provided the record <br> 1.Creative Mobile Technologies <br> 2. VeriFone Inc <br> *TPEP: Taxi Passenger Enhancements Program|![대체 텍스트(alt)](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgv0WnC1hJDGCnFY9bLVNCubV_SH5CZ-vhzovfDVveELaWSO09AEsDSLQD2CNBZxfi2Ok&usqp=CAU "이미지 설명(title)")|
|tpep_pickup_datetime|The date and time when the meter was engaged|테스트3|
|tpep_dropoff_datetime|The date and time when the meter was disengaged|테스트3|
|passenger_count|The number of passengers in the vehicle. This is a driver-entered value|![Passenger count table](https://www.notion.so/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F6338ab29-186a-433a-be2b-dcb9f6964414%2F2b79da58-2520-41c4-918f-708274cb9312%2Fimage.png?id=18429dbc-7846-80d1-81ec-ca4374addc1b&table=block&spaceId=6338ab29-186a-433a-be2b-dcb9f6964414&width=1660&userId=c4677a11-c3ff-4727-9a3e-da98ca7fc224&cache=v2 "Passenger count")|
|trip_distance|The elapsed trip distance in miles reported by the taximeter|image|
|pickup_longitude|Longitude where the meter was engaged|image|
|pickup_latitude|Latitude where the meter was engaged|image|
|RateCodeID|The final rate code in effect at the end of the trip<br>1. Standard rate<br>2. JFK<br>3. Newark<br>4. Nassau or Westcheter<br>5. Negotiated fare<br>6. Group ride|image|
|store_and_fwd_flag|This flag indicates whether the trip record was held in vehicle memory before sending to the vendor,aka “store and forward,” because the vehicle did not have a connection to the server.<br>Y= store and forward trip<br>N= not a store and forward trip|image|
|dropoff_longitude|Longitude where the meter was disengaged|image|
|dropoff_latitude|Latitude where the meter was disengaged|image|
|payment_type|A numeric code signifying how the passenger paid for the trip<br>1. Credit card<br>2. Cash<br>3. No Charge<br>4. Dispute<br>5. Unknown<br>6. Voided trip|image|
|fare_amount|The time-and-distance fare calculated by the meter|image|
|extra|Miscellaneous extras and surcharges. Currently, this only includes. the $0.50 and $1 rush hour and overnight charges|image|
|mta_tax|0.50 MTA tax that is automatically triggered based on the metered rate in use|image|
|improvement_surcharge|0.30 improvement surcharge assessed trips at the flag drop. the improvement surcharge began being levied in 2015|image|
|tip_amount|Tip amount – This field is automatically populated for credit card tips.Cash tips are not included|image|
|tolls_amount|Total amount of all tolls paid in trip|image|
|total_amount|The total amount charged to passengers. Does not include cash tips|image|

