import requests
import json

def fraud_api_request(ip:str, api_key:str):
    headers = {'X-API-KEY': api_key}
    payload = {
    "config": {
        "ip": {
        "include": "flags,history,id",
        "version": "v1.1"
        },
        "email": {
        "include": "flags,history,id",
        "version": "v2.2"
        },
        "phone": {
        "include": "flags,history,id",
        "version": "v1.4"
        },
        "ip_api": True,
        "email_api": False,
        "phone_api": False,
        "device_fingerprinting": True
    },
            "ip": ip,
            "action_type": "withdrawal",
            "transaction_id": "",
            "affiliate_id": "",
            "order_memo": "",
            "email": "",
            "email_domain": "",
            "password_hash": "",
            "user_bank_account": "",
            "user_bank_name": "",
            "user_balance": "",
            "user_category": "",
            "user_fullname": "",
            "user_name": "",
            "user_id": "",
            "user_dob": "",
            "user_created": "",
            "user_country": "",
            "user_city": "",
            "user_region": "",
            "user_zip": "",
            "user_street": "",
            "user_street2": "",
            "session": "",
            "payment_mode": "",
            "payment_provider": "",
            "phone_number": "",
            "transaction_type": "",
            "transaction_amount": "",
            "transaction_currency": "",
            "billing_country": "",
            "billing_city": "",
            "billing_region": "",
            "billing_zip": "",
            "billing_street": "",
            "billing_street2": "",
            "billing_phone": "",
            "merchant_id": "",
            "merchant_category": "",
            "details_url": "",
            "custom_fields": { 
    }
    }
    response = requests.post('https://api.seon.io/SeonRestService/fraud-api/v2.0', headers=headers, data=json.dumps(payload)).json()
    if response["success"]:
        data = {
            "latitude" : response["data"]["ip_details"]["latitude"],
            "longitude" : response["data"]["ip_details"]["longitude"],
            "fraud_score" : response["data"]["fraud_score"],
            "vpn" : response["data"]["ip_details"]["vpn"],
            "tor" : response["data"]["ip_details"]["tor"],
            "proxy" : response["data"]["ip_details"]["web_proxy"]
        }
        return data
    else:
        return response["error"]