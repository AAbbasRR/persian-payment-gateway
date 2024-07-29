class PaymentGateway:
    """
    Base class for all payment gateways.

    Args:
        portal_name (str): The name of the payment gateway.
        merchant_id (str): The merchant ID provided by the payment gateway.
    """

    def __init__(self, portal_name: str, merchant_id: str):
        self.portal_name = portal_name
        self.merchant_id = merchant_id
        self.links = {
            "create_link": "",
            "verify_payment": "",
        }

    def create_payment_link(self, price: int, description: str, callback_url: str) -> dict:
        """
        Creates a payment link. This method should be implemented by subclasses.

        Args:
            price (int): The amount to be paid.
            description (str): A brief description of the payment.
            callback_url (str): The URL to which the user will be redirected after payment.

        Returns:
            dict: A dictionary containing the payment link and other relevant data.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        raise NotImplementedError("Subclasses should implement this method")

    def verify_payment_status(self, price: int, auth_token: str) -> str:
        """
        Verifies the status of a payment. This method should be implemented by subclasses.

        Args:
            price (int): The amount to be verified.
            auth_token (str): The authorization token received from the payment link.

        Returns:
            str: The reference ID of the transaction if successful.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        raise NotImplementedError("Subclasses should implement this method")
