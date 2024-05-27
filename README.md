# online_order
An online ordering system

HTTP REST API Endpoints:

**Method**

POST /Orders

**Headers**
'Content-Type: application/json'

**Body** 

{"customer_id":"","items":[{"product_code":"","quantity":0,"price":0}],"order_date":null,"payment_info":{"saved_payment_method":0,"payment_method":{"type":"card","card":{"number":"4242424242424242","expiry_month":8,"expiry_year":2026,"cvc":"314"},"save_for_future":true}},"billing_address":{"first_name":"","last_name":"","house_number":"","street_name":"","address_line_1":"","address_line_2":"","city":"","post_code":"","country":""},"shipping_address":{"first_name":"","last_name":"","house_number":"","street_name":"","address_line_1":"","address_line_2":"","city":"","post_code":"","country":""}}

**Response:**
Status: 200

Body:
{
  "order_id": "",
  "order_date": null,
  "order_status": "pending"
}

