# nyc_taxi_data_analysis

|Column|Description|Figure|
|------|---|---|
|VenderID|A code indicating the TPEP provider that provided the record <br> 1.Creative Mobile Technologies <br> 2. VeriFone Inc <br> *TPEP: Taxi Passenger Enhancements Program|![vendorID](https://github.com/user-attachments/assets/b847a4ee-1f00-459f-9312-21d336e14551)"vendorID")|
|tpep_pickup_datetime|The date and time when the meter was engaged|![Distribution_of_pickup_date](https://github.com/user-attachments/assets/4feb35d4-235c-4750-ab9b-87abbbbc5f0f)|
|tpep_dropoff_datetime|The date and time when the meter was disengaged|![Distribution_of_dropoff_date](https://github.com/user-attachments/assets/df6cd918-3f88-4a69-bbf7-38199717b93a)|
|passenger_count|The number of passengers in the vehicle. This is a driver-entered value|![passenger_count](https://github.com/user-attachments/assets/ee618060-24c3-43b2-902f-a5d6de5823e7)|
|trip_distance|The elapsed trip distance in miles reported by the taximeter|![Distribution_of_trip_dist](https://github.com/user-attachments/assets/d0d83cb3-45dd-456a-b4fa-0148053dc86f)|
|pickup_location|location where the meter was engaged|![pickup_loc](https://github.com/user-attachments/assets/8cfae76a-9d2a-4b66-945f-439de301059c "pickup_loc")|
|dropoff_location|location where the meter was disengaged|![dropoff_loc](https://github.com/user-attachments/assets/12631b94-a945-4f63-87cd-efcb03df573e "dropoff_loc")|
|RateCodeID|The final rate code in effect at the end of the trip<br>1. Standard rate<br>2. JFK<br>3. Newark<br>4. Nassau or Westcheter<br>5. Negotiated fare<br>6. Group ride|![Distribution_of_ratecode_ID](https://github.com/user-attachments/assets/2ab3d1c3-494b-472c-992a-77db7e700044)|
|store_and_fwd_flag|This flag indicates whether the trip record was held in vehicle memory before sending to the vendor,aka “store and forward,” because the vehicle did not have a connection to the server.<br>Y= store and forward trip<br>N= not a store and forward trip|![Distribution_of_store_and_fwd_flag](https://github.com/user-attachments/assets/eb8ea700-7cd1-4803-ab92-430f795f4041)|
|payment_type|A numeric code signifying how the passenger paid for the trip<br>1. Credit card<br>2. Cash<br>3. No Charge<br>4. Dispute<br>5. Unknown<br>6. Voided trip|![Distribution_of_payment_type](https://github.com/user-attachments/assets/43e2f8bd-3c15-41a5-9151-09206b704deb)
|
|fare_amount|The time-and-distance fare calculated by the meter|![Distribution_of_fare_amount](https://github.com/user-attachments/assets/e8881dc4-fbaa-4873-bc5d-034364866a96)|
|extra|Miscellaneous extras and surcharges. Currently, this only includes. the $0.50 and $1 rush hour and overnight charges|image|
|mta_tax|0.50 MTA tax that is automatically triggered based on the metered rate in use|image|
|improvement_surcharge|0.30 improvement surcharge assessed trips at the flag drop. the improvement surcharge began being levied in 2015|image|
|tip_amount|Tip amount – This field is automatically populated for credit card tips.Cash tips are not included|image|
|tolls_amount|Total amount of all tolls paid in trip|image|
|total_amount|The total amount charged to passengers. Does not include cash tips|image|

