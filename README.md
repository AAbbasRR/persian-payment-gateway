# Persian Payment Gateway Package

## Overview

The **Persian Payment Gateway Package** is a Python library designed to simplify the integration of multiple payment
gateways into your application. It provides a unified interface to work with different payment providers like Zarinpal,
PayPal, and others.

## Features

- **Support for Multiple Payment Gateways**: Easily integrate and switch between different payment providers.
- **Unified API**: A consistent interface for creating and verifying payments across different gateways.
- **Customizable**: Set minimum transaction amounts and choose whether to convert amounts to the required currency.

## Supported Payment Gateways

Currently, the package supports the following payment gateways:

1. **Zarinpal**: A popular payment gateway in Iran. It supports payments in both Tomans and Rials, depending on the
   user's preference.

We plan to add support for more gateways in future releases. Contributions for new gateway integrations are welcome!

## Installation

You can install the package via pip:

```bash
pip install payment-gateway-package
```

## Usage

### Setting Up a Payment Gateway

To use a specific payment gateway, you need to create an instance of the corresponding class and provide necessary
credentials.

Example with Zarinpal:

```python
from payment_gateway.zarinpal import ZarinpalGateway

# Initialize the Zarinpal gateway with your merchant ID
zarinpal = ZarinpalGateway(merchant_id="YOUR_MERCHANT_ID")

# Create a payment link
link_info = zarinpal.create_payment_link(
    price=10000,
    description="Test payment",
    callback_url="http://yourcallback.com",
    convert_to_irr=True,
    min_amount=5000
)

print("Payment Link:", link_info["link"])

# Verify payment status
verification_result = zarinpal.verify_payment_status(
    price=10000,
    auth_token=link_info["auth_token"]
)

print("Verification Result:", verification_result)
```

## Available Parameters

- `price`: The amount to be paid (default is in the gateway's base currency).
- `description`: A brief description of the payment.
- `callback_url`: URL to redirect the user after the payment process.
- `convert_to_irr`: Boolean value, if True converts the amount to Iranian Rials (Zarinpal-specific).
- `min_amount_irr`: The minimum amount allowed for the transaction.
- `min_amount_irr`: The maximum amount allowed for the transaction.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author

Abbas Rahimzadeh - [arahimzadeh79@gmail.com](mailto:arahimzadeh79@gmail.com)

## Acknowledgments

Special thanks to the open-source community for their valuable contributions and resources.