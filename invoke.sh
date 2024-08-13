curl -X POST http://0.0.0.0:8080/predict \
     -H "Content-Type: application/json" \
     -d '{
  "distance_from_home": 2.921681,
  "distance_from_last_transaction":  0.877478,
  "ratio_to_median_purchase_price": -0.415702,
  "repeat_retailer": 0.0,
  "used_chip": 0.0,
  "used_pin_number": 0.0,
  "online_order": 1.0
}'