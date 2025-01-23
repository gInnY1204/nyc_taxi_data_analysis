# nyc_taxi_data_analysis

|Column|Description|Figure|
|------|---|---|
|VenderID|A code indicating the TPEP provider that provided the record <br> &ensp;1.Creative Mobile Technologies <br> &ensp;2. VeriFone Inc <br><br>  *TPEP: Taxi Passenger Enhancements Program|![vendorID](https://github.com/user-attachments/assets/b847a4ee-1f00-459f-9312-21d336e14551)"vendorID")|
|tpep_pickup_datetime|The date and time when the meter was engaged|![Distribution_of_pickup_date](https://github.com/user-attachments/assets/4feb35d4-235c-4750-ab9b-87abbbbc5f0f)|
|tpep_dropoff_datetime|The date and time when the meter was disengaged|![Distribution_of_dropoff_date](https://github.com/user-attachments/assets/df6cd918-3f88-4a69-bbf7-38199717b93a)|
|passenger_count|The number of passengers in the vehicle. This is a driver-entered value|![passenger_count](https://github.com/user-attachments/assets/ee618060-24c3-43b2-902f-a5d6de5823e7)|
|trip_distance|The elapsed trip distance in miles reported by the taximeter|![trip_distance](https://github.com/user-attachments/assets/4ba4d1bd-a3d8-4edf-90eb-3b85fa168146)|
|pickup_location|location where the meter was engaged|![pickup_loc](https://github.com/user-attachments/assets/8cfae76a-9d2a-4b66-945f-439de301059c "pickup_loc")|
|dropoff_location|location where the meter was disengaged|![dropoff_loc](https://github.com/user-attachments/assets/12631b94-a945-4f63-87cd-efcb03df573e "dropoff_loc")|
|RateCodeID|The final rate code in effect at the end of the trip<br><br>&ensp;1. Standard rate<br>&ensp;2. JFK<br>&ensp;3. Newark<br>&ensp;4. Nassau or Westcheter<br>&ensp;5. Negotiated fare<br>&ensp;6. Group ride|![RateCode_ID](https://github.com/user-attachments/assets/00316c46-1cfc-4d4e-a259-2a3baacb2410)|
|store_and_fwd_flag|This flag indicates whether the trip record was held in vehicle memory before sending to the vendor,aka “store and forward,” because the vehicle did not have a connection to the server.<br><br>&ensp;Y= store and forward trip<br>&ensp;N= not a store and forward trip|![store_and_fwd_flag](https://github.com/user-attachments/assets/8cf4f6e7-2222-4ca0-8f54-b7298da843ec)|
|payment_type|A numeric code signifying how the passenger paid for the trip<br><br>&ensp;1. Credit card<br>&ensp;2. Cash<br>&ensp;3. No Charge<br>&ensp;4. Dispute<br>&ensp;5. Unknown<br>&ensp;6. Voided trip|![payment_type](https://github.com/user-attachments/assets/b5fbde1f-f2b4-47c1-af3e-e73e228a70d4)|
|fare_amount|The time-and-distance fare calculated by the meter|![Distribution_of_fare_amount](https://github.com/user-attachments/assets/e8881dc4-fbaa-4873-bc5d-034364866a96)|
|extra|Miscellaneous extras and surcharges. Currently, this only includes. the $0.50 and $1 rush hour and overnight charges|![extra](https://github.com/user-attachments/assets/045e46cb-0cf1-4794-bf00-22156fab3af1)|
|mta_tax|0.50 MTA tax that is automatically triggered based on the metered rate in use|![mta_tax](https://github.com/user-attachments/assets/e80c130e-c708-4128-999f-9d3c0b271a45)|
|improvement_surcharge|0.30 improvement surcharge assessed trips at the flag drop. the improvement surcharge began being levied in 2015|![improvement_surcharge](https://github.com/user-attachments/assets/849a73d4-e446-4b5f-8277-7bcff546d33a)|
|tip_amount|Tip amount – This field is automatically populated for credit card tips.Cash tips are not included|![tip_amount](https://github.com/user-attachments/assets/df364826-b411-4ed7-a82c-4f0c44fb89ec)|
|tolls_amount|Total amount of all tolls paid in trip|![tolls_amount](https://github.com/user-attachments/assets/33cb5ba9-0c5d-4ddb-897b-f59957b4fcad)|
|total_amount|The total amount charged to passengers. Does not include cash tips|![total_amount](https://github.com/user-attachments/assets/3012fa5e-deb0-4791-aec7-5bbdc3755328)|

