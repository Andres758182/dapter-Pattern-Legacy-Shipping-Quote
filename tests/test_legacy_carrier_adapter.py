from shipping_adapter.checkout import Checkout
from shipping_adapter.legacy_carrier import LegacyCarrier
from shipping_adapter.legacy_carrier_adapter import LegacyCarrierAdapter


def test_checkout_can_use_legacy_carrier_through_adapter():
    adapter = LegacyCarrierAdapter(LegacyCarrier())
    checkout = Checkout(adapter)

    # 10 kg = 22.0462 lb -> 6.0 + 22.0462 * 1.25 = 33.56
    price = checkout.shipping_quote("45000", 10.0)

    assert price == 33.56