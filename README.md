# nyc_taxi_data_analysis

|Column|Description|Figure|
|------|---|---|
|VenderID|A code indicating the TPEP provider that provided the record <br> 1.Creative Mobile Technologies <br> 2. VeriFone Inc <br> *TPEP: Taxi Passenger Enhancements Program|![vendorID](https://github.com/user-attachments/assets/b847a4ee-1f00-459f-9312-21d336e14551)"vendorID")|
|tpep_pickup_datetime|The date and time when the meter was engaged|![Distribution_of_pickup_date](https://github.com/user-attachments/assets/4feb35d4-235c-4750-ab9b-87abbbbc5f0f)|
|tpep_dropoff_datetime|The date and time when the meter was disengaged|테스트3|
|passenger_count|The number of passengers in the vehicle. This is a driver-entered value|![Image](https://github.com/user-attachments/assets/a4d1a057-9a76-4b26-89ed-a4ffd5cbdaf1)|
|trip_distance|The elapsed trip distance in miles reported by the taximeter|image|
|pickup_location|location where the meter was engaged|![pickup_loc](https://github.com/user-attachments/assets/8cfae76a-9d2a-4b66-945f-439de301059c "pickup_loc")|
|dropoff_location|location where the meter was disengaged|![dropoff_loc](https://github.com/user-attachments/assets/12631b94-a945-4f63-87cd-efcb03df573e "dropoff_loc")|
|RateCodeID|The final rate code in effect at the end of the trip<br>1. Standard rate<br>2. JFK<br>3. Newark<br>4. Nassau or Westcheter<br>5. Negotiated fare<br>6. Group ride|image|
|store_and_fwd_flag|This flag indicates whether the trip record was held in vehicle memory before sending to the vendor,aka “store and forward,” because the vehicle did not have a connection to the server.<br>Y= store and forward trip<br>N= not a store and forward trip|image|
|payment_type|A numeric code signifying how the passenger paid for the trip<br>1. Credit card<br>2. Cash<br>3. No Charge<br>4. Dispute<br>5. Unknown<br>6. Voided trip|image|
|fare_amount|The time-and-distance fare calculated by the meter|image|
|extra|Miscellaneous extras and surcharges. Currently, this only includes. the $0.50 and $1 rush hour and overnight charges|image|
|mta_tax|0.50 MTA tax that is automatically triggered based on the metered rate in use|image|
|improvement_surcharge|0.30 improvement surcharge assessed trips at the flag drop. the improvement surcharge began being levied in 2015|image|
|tip_amount|Tip amount – This field is automatically populated for credit card tips.Cash tips are not included|image|
|tolls_amount|Total amount of all tolls paid in trip|image|
|total_amount|The total amount charged to passengers. Does not include cash tips|image|

