from .base import PaymentGateway
import requests
import json


class ZarinpalGateway(PaymentGateway):
    """
    Zarinpal Gateway class for managing payments through the Zarinpal payment gateway.

    Args:
        merchant_id (str): The merchant ID provided by Zarinpal.
    """

    def __init__(self, merchant_id: str):
        super().__init__("zarinpal", merchant_id)
        self.links["create_link"] = "https://api.zarinpal.com/pg/v4/payment/request.json"
        self.links["verify_payment"] = "https://api.zarinpal.com/pg/v4/payment/verify.json"

    def create_payment_link(
            self,
            price: int,
            description: str,
            callback_url: str,
            convert_to_irr: bool = False,
            min_amount_irr: int = 1000,
            max_amount_irr: int = 1000000000
    ) -> dict:
        """
        Creates a payment link for the Zarinpal gateway.

        Args:
            price (int): The amount to be paid (in Toman if convert_to_irr is False, otherwise in IRR).
            description (str): A brief description of the payment.
            callback_url (str): The URL to which the user will be redirected after payment.
            convert_to_irr (bool, optional): If True, the amount will be converted to IRR (Rials). Defaults to False.
            min_amount_irr (int, optional): The minimum amount in IRR. Defaults to 1000.
            max_amount_irr (int, optional): The maximum amount in IRR. Defaults to 1000000000.

        Returns:
            dict: A dictionary containing the payment link and authority token, or None if the creation failed.

        Raises:
            ValueError: If the amount is less than `min_amount_irr` or greater than `max_amount_irr`.
        """
        # Convert the price to IRR if specified
        if convert_to_irr:
            price = int(price) * 10

        # Check if the price is within the allowed range
        if price < min_amount_irr:
            raise ValueError(f"The amount must be greater than {min_amount_irr}")
        if price > max_amount_irr:
            raise ValueError(f"The amount may not be greater than {max_amount_irr}")

        # Send the request to Zarinpal to create the payment link
        response = requests.post(
            url=self.links["create_link"],
            data={
                "merchant_id": self.merchant_id,
                "amount": price,
                "description": description,
                "callback_url": f"{callback_url}/payment-redirect",
            },
        )

        # Parse the response and return the payment link and authority token
        response_data = json.loads(response.content).get("data", {})
        if response_data.get("code") == 100:
            return {
                "link": f"https://www.zarinpal.com/pg/StartPay/{response_data['authority']}",
                "auth_token": response_data["authority"],
            }
        return None

    def verify_payment_status(self, price: int, auth_token: str, convert_to_irr: bool = False) -> str:
        """
        Verifies the status of a payment.

        Args:
            price (int): The amount to be paid (in Toman if convert_to_irr is False, otherwise in IRR).
            auth_token (str): The authority token received from the payment link.
            convert_to_irr (bool, optional): If True, the amount will be converted to IRR (Rials). Defaults to False.

        Returns:
            str: The reference ID of the transaction if successful, or None if verification failed.
        """
        # Convert the price to IRR if specified
        if convert_to_irr:
            price = int(price) * 10

        # Send the request to Zarinpal to verify the payment status
        response = requests.post(
            url=self.links["verify_payment"],
            data={
                "merchant_id": self.merchant_id,
                "authority": auth_token,
                "amount": price,
            },
        )

        # Parse the response and return the reference ID if the payment was successful
        response_data = json.loads(response.content).get("data", {})
        if response_data.get("code") == 100:
            return response_data.get("ref_id")
        return None
