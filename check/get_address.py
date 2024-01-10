import requests
import json
from settings import settings

API_KEY = settings.bots.api_key

class AddressValidator:
    def __init__(self, api_key=API_KEY):
        self.base_url = 'https://content-addressvalidation.googleapis.com/v1:validateAddress'
        self.api_key = api_key
        self.headers = {
            "authority": "content-addressvalidation.googleapis.com",
            "method": "POST",
            "path": f"/v1:validateAddress?alt=json&key={api_key}",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "ru-RU,ru;q=0.9,en;q=0.8",
            "content-length": "63",
            "content-type": "application/json",
            "origin": "https://content-addressvalidation.googleapis.com",
            "referer": f"https://content-addressvalidation.googleapis.com/static/proxy.html?usegapi=1&jsh=m%3B%2F_%2Fscs%2Fabc-static%2F_%2Fjs%2Fk%3Dgapi.lb.ru.C5jFMFtB6Ok.O%2Fd%3D1%2Frs%3DAHpOoo8M2DKqBqYv0_Ok_sPDuNyHeeGLtw%2Fm%3D__features__",
            "Sec-Ch-Ua": f"\"Opera\";v=\"105\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
            "X-Clientdetails": f"appVersion=5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F119.0.0.0%20Safari%2F537.36%20OPR%2F105.0.0.0&platform=Win32&userAgent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F119.0.0.0%20Safari%2F537.36%20OPR%2F105.0.0.0",
            "X-Goog-Encode-Response-If-Executable": "base64",
            "X-Javascript-User-Agent": "google-api-javascript-client/1.1.0",
            "X-Origin": "https://developers-dot-devsite-v2-prod.appspot.com",
            "X-Referer": "https://developers-dot-devsite-v2-prod.appspot.com",
            "X-Requested-With": "XMLHttpRequest"
        }

    def validate_address(self, address_line, region_code="AR"):
        endpoint = f"{self.base_url}?alt=json&key={self.api_key}"
        payload = {"address": {"regionCode": region_code, "addressLines": [address_line]}}
        response = requests.post(endpoint, data=json.dumps(payload), headers=self.headers)
        data = response.json()
        return data.get('result', {}).get('address', {}).get('formattedAddress')

    def get_validation_granularity(self, address_line, region_code="AR"):
        endpoint = f"{self.base_url}?alt=json&key={self.api_key}"
        payload = {"address": {"regionCode": region_code, "addressLines": [address_line]}}
        response = requests.post(endpoint, data=json.dumps(payload), headers=self.headers)
        data = response.json()
        return data.get('result', {}).get('verdict', {}).get('validationGranularity')
