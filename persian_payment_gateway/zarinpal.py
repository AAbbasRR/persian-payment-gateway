from .base import PaymentGateway
import requests
import json


class ZarinpalGateway(PaymentGateway):
    def __init__(self, merchant_id):
        super().__init__("zarinpal", merchant_id)
        self.links["create_link"] = "https://api.zarinpal.com/pg/v4/payment/request.json"
        self.links["verify_payment"] = "https://api.zarinpal.com/pg/v4/payment/verify.json"

    def create_payment_link(
            self,
            price,
            description,
            callback_url,
            convert_to_irr=False,
            min_amount_irr=1000,
            max_amount_irr=1000000000
    ):
        if convert_to_irr:
            price = int(price) * 10

        if price < min_amount_irr:
            raise ValueError(f"The amount must be greater than {min_amount_irr}")

        if price > max_amount_irr:
            raise ValueError(f"The amount may not be greater than {max_amount_irr}")

        result = requests.post(
            url=self.links["create_link"],
            data={
                "merchant_id": self.merchant_id,
                "amount": price,
                "description": description,
                "callback_url": f"{callback_url}/payment-redirect",
            },
        )
        response_data = json.loads(result.content)["data"]
        if response_data["code"] == 100:
            return {
                "link": f"https://www.zarinpal.com/pg/StartPay/{response_data['authority']}",
                "auth_token": response_data["authority"],
            }
        return None

    def verify_payment_status(self, price, auth_token):
        result = requests.post(
            url=self.links["verify_payment"],
            data={
                "merchant_id": self.merchant_id,
                "authority": auth_token,
                "amount": int(price) * 10,
            },
        )
        response_data = json.loads(result.content)["data"]
        try:
            if response_data["code"] == 100:
                return response_data["ref_id"]
        except TypeError:
            return None
