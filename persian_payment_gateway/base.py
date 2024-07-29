class PaymentGateway:
    def __init__(self, portal_name, merchant_id):
        self.portal_name = portal_name
        self.merchant_id = merchant_id
        self.links = {
            "create_link": "",
            "verify_payment": "",
        }

    def create_payment_link(self, price, description, callback_url):
        raise NotImplementedError("Subclasses should implement this method")

    def verify_payment_status(self, price, auth_token):
        raise NotImplementedError("Subclasses should implement this method")
