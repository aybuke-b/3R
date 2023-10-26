from dataclasses import dataclass
from serde import serialize


@serialize
@dataclass
class Smartphone:
    """`Smartphone`: represents an abstract class of a Smartphone with different characteristics.

    ---------
    `Class Attributes`
    --------- ::

        model: str
        color: str
        os: str
        sim_type: str
        sim_number: str
        cpu: str
        cpu_details: str
        battery: str
        charging_type: str
        fast_charging: str
        screen_size: str
        screen_tech: str
        screen_resolution: str
        screen_type: str
        refresh_rate: str
        network: str
        bluetooth: str
        wifi: str
        usb_type_c: str
        storage: str
        upgrade_storage: str
        ram: str
        sensor: str
        sensor_resolution: str
        repairability_index: str
        warranty: str
        made_in: str
        brand: str
        das_head: str
        das_chest: str
        das_limbs: str
        height: str
        width: str
        thickness: str
        net_weight: str
        price: str
        stars: str
        reviews: str

    `Example(s)`
    ---------

    >>> Smartphone("a","b","c","d")
    ... Smartphone(model="a", color="b",sim_type="c", sim_number="d",...)"""

    model: str
    color: str
    os: str
    sim_type: str
    sim_number: str
    cpu: str
    cpu_details: str
    battery: str
    charging_type: str
    fast_charging: str
    screen_size: str
    screen_tech: str
    screen_resolution: str
    screen_type: str
    refresh_rate: str
    network: str
    bluetooth: str
    wifi: str
    usb_type_c: str
    storage: str
    upgrade_storage: str
    ram: str
    sensor: str
    sensor_resolution: str
    repairability_index: str
    warranty: str
    made_in: str
    brand: str
    das_head: str
    das_chest: str
    das_limbs: str
    height: str
    width: str
    thickness: str
    net_weight: str
    price: str
    stars: str
    reviews: str
