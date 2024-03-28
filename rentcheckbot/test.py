import aiohttp, asyncio, logging, json
import ujson 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


API_KEY = "AIzaSyDwFJLfv2EmdCkTpM4AGVLKVS2HcQjr_WM"


base_url = 'https://content-addressvalidation.googleapis.com/v1:validateAddress'
headers = {
            "authority": "content-addressvalidation.googleapis.com",
            "method": "POST",
            "path": f"/v1:validateAddress?alt=json&key={API_KEY}",
            "accept-encoding": "gzip, deflate, br",
            "Sec-Fetch-Site": "same-origin",
            "X-Goog-Encode-Response-If-Executable": "base64",
            "X-Origin": "https://developers-dot-devsite-v2-prod.appspot.com",
        }

async def validate_address(address_line):
    logging.info("Starting address validation")
    endpoint = f"{base_url}?alt=json&key={API_KEY}"
    payload = f'{{"address": {{"regionCode": "AR", "addressLines": ["{address_line}"]}}}}'
    try:
        async with aiohttp.ClientSession() as session:
            logging.info(f"Sending request to {endpoint}")
            logging.info(f"Sending payload: {payload}")
            async with session.post(endpoint, data=payload, headers=headers) as response:
                logging.info("Received response from the server")
                response_json = await response.json() 
                data = response_json['result']['address']['formattedAddress']
                return data
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise

async def main():
    validated_address = await validate_address("Coronel Morales 1470")
    return validated_address

address = asyncio.run(main())
print(address)
