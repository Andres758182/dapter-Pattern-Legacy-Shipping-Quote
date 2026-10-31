from .legacy_carrier import LegacyCarrier
from .shipping_quote_provider import ShippingQuoteProvider


class LegacyCarrierAdapter(ShippingQuoteProvider):
    KG_TO_LB = 2.20462

    def __init__(self, legacy_carrier: LegacyCarrier):
        self.legacy_carrier = legacy_carrier

    def quote(self, destination: str, weight_kg: float) -> float:
        weight_lb = weight_kg * self.KG_TO_LB
        return self.legacy_carrier.get_price(destination, weight_lb)