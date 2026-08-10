from django.core.management.base import BaseCommand
from django.utils.text import slugify

from core.models import (
    ProductCategory,
    ProductSubCategory,
    ProductType,
)


PRODUCT_STRUCTURE = {
    "Pressure Measurement": {
        "icon": "speedometer2",
        "Pressure Gauges": [
            "Commercial Pressure Gauges",
            "Industrial Pressure Gauges",
            "Process Pressure Gauges",
            "Low Pressure Gauges",
            "Diaphragm Gauges",
            "High Precision Test Gauges",
            "Differential and Duplex Pressure Gauges",
            "Absolute Pressure Gauges",
        ],
        "Pressure Gauges with Transmitter Switches": [
            "Pressure Gauges with Electrical Output Signal",
            "Pressure Gauges with Switch Contacts",
        ],
        "Pressure Switches": [
            "Mechanical Pressure Switches",
        ],
        "Pressure Transmitters": [
            "Pressure Transducer and Transmitter",
            "Submersible Pressure Transmitter",
            "Electronic Pressure Switches",
            "Explosion Proof Pressure Transmitters",
            "Intelligent Bus Compatible",
            "Process Transmitters",
            "Digital Gauge",
        ],
        "Diaphragm Seals": [
            "Threaded Process Connections",
            "Flanged Connection",
            "Sterile Connection",
            "Hydra-Line Diaphragm Seal Systems",
            "Diaphragm Seal Accessories",
        ],
    },

    "Temperature Measurement": {
        "icon": "thermometer-half",
        "Thermowells": [
            "Thermowells",
        ],
        "Mechanical Temperature Measurement": [
            "Bimetallic Thermometers",
            "Expansion Thermometers",
            "Gas Actuated Thermometers",
            "Machine Glass Thermometers",
        ],
        "Temperature Gauges with Transmitter Switches": [
            "Dial Thermometers with Electrical Output Signal",
            "Dial Thermometers with Switch Contacts",
        ],
        "Temperature Switches": [
            "Mechanical Temperature Switches",
        ],
        "Electrical Temperature Measurement": [
            "Temperature Transmitters",
            "Resistance Thermometers",
            "Thermocouples",
            "Electrical Temperature Switches",
        ],
    },

    "Controllers, Indicators and Recorders": {
        "icon": "display",
        "Indicator": [
            "Panel Mounted Digital Indicators",
            "Field Mounted Digital Indicators",
            "Attachable Indicators",
        ],
        "Controllers": [
            "Panel Mounted Controllers",
        ],
        "Recorders": [
            "Videographic Recorders",
            "Circular Chart Recorders",
            "Strip Chart Recorders",
        ],
    },

    "Level Measurement": {
        "icon": "layers",
        "Mechanical Level Measurement": [
            "Magnetic Level Gauges",
            "Mini Tubular Level Gauges",
            "Oil Level Gauge",
            "Float and Board Tank Gauge",
            "Float and Dial Gauge",
            "Weld Pad Flat Glass Level Gauge",
            "Transparent Tubular Level Gauge",
            "Reflex Transparent Flat Glass Level Gauge",
        ],
        "Level Switches": [
            "Buoyancy Level Switches",
            "RF Capacitance Level Switches",
            "Vibrating Fork Level Switches",
            "Conductivity Type Level Switch with Control Unit",
            "Thermal Dispersion Type",
            "Air Operated",
            "Rotary Paddle Level Switch",
            "Vibrating Diamond Blade Level Switch",
            "Vibrating Rod Level Switch",
        ],
        "Level Transmitters": [
            "Magnetic Float Operated Guided",
            "RF Capacitance Type Level Transmitter",
            "Electronic Level Switch with Display",
            "Magnetostrictive Level Transmitters",
            "Guided Wave Radar Level Transmitters",
            "Ultrasonic Level Transmitters and Switches",
            "Laser Level Transmitters",
            "Gauge and Differential Pressure Level Transmitters",
            "Displacer Level Transmitter",
            "Radar Level Transmitter",
        ],
    },

    "Flow Measurement": {
        "icon": "activity",
        "Mechanical Flow Measurement": [
            "Variable Area Flow Meters",
        ],
        "Flow Transmitters": [
            "Coriolis Mass Flow Meters",
            "Inline Mass Flow Meters",
            "Insertion Mass Flow Meters",
            "Electromagnetic Flow Meters",
            "Flow Computer Units",
            "Thermal Mass Flow Meters",
            "Vortex and Swirl Flow Meters",
            "Ultrasonic Flow Meters",
            "Primary Flow Differential Products",
            "Turbine Type Flow Meters",
        ],
    },

    "Calibration Technology": {
        "icon": "sliders",
        "Pressure": [
            "Portable Pressure Generation",
            "Hand-Held Calibrators",
            "Precision Pressure Measuring Instruments",
            "Pressure Controllers",
            "Pressure Balances",
        ],
        "Temperature": [
            "Reference Thermometers",
            "Hand Held Calibrators",
            "Digital Hand-Held Multimeter",
            "Process Calibrator RTD",
            "Process Calibrator Temperature",
            "Process Calibrator Thermocouple",
            "Portable Temperature Calibrators",
            "Calibration Baths",
        ],
        "Current Voltage Resistance": [
            "High Precision Process Calibrator",
            "Hand Held Multifunction Calibrator",
            "Documenting Multi Function Calibrator",
            "Hand Held Temperature Calibrator",
            "Portable Multi-Function Calibrator",
            "Precision Loop Calibrator",
            "Process Calibrator Current Voltage",
        ],
        "Humidity": [
            "High Precision Humidity Calibrator",
            "Humidity Calibration Set",
        ],
    },

    "Valves and Fittings": {
        "icon": "diagram-3",
        "Needle Valve": [
            "Single Bonnet",
            "Double Bonnet",
            "High Pressure",
            "Angle",
            "Medium Pressure",
        ],
        "Gauge Valves": [
            "Gauge Bleed Valve",
            "Gauge Vent Valve",
            "Multiport Gauge Valve",
            "Forged Body Gauge Valve",
        ],
        "Ball Valves": [
            "1000 WOG",
            "3000 WOG",
            "10000 PSI Standard Bore Ball Valves",
        ],
        "Manifold Valves": [
            "Two Valve Manifolds",
            "Three Valve Manifolds",
            "Five Valve Manifolds",
            "Double Block and Bleed Manifolds",
        ],
        "Check Valves": [
            "22,500 PSI Check Valves",
            "High Pressure Check Valves",
            "10,000 PSI Check Valves",
        ],
        "Instrumentation Pipe Fitting": [
            "Straights",
            "Elbows, Tees and Crosses",
        ],
        "Instrumentation Tube Fitting": [
            "Straights",
            "Elbows, Tees and Crosses",
        ],
        "High Pressure Tube Fittings": [
            "Straights",
            "Elbows, Tees and Crosses",
        ],
        "Pressure Gauge Accessories": [
            "Pressure Gauge Cocks",
            "Over Pressure Protectors",
            "Swivel Adaptors",
            "Syphons",
            "Pressure Gauge Snubbers",
        ],
        "Instrumentation Tubes": [
            "Standard",
            "High Pressure",
        ],
        "Relief Valves": [],
    },

    "Food and Pharma": {
        "icon": "droplet-half",
        "Pumps": [
            "Positive Displacement Pumps",
            "Centrifugal Pumps",
            "Side Channel Pumps",
        ],
        "Filters and Sight Glass": [
            "Filters",
            "Sight Glass",
            "Filter Regulator",
        ],
        "Mixing Equipment": [
            "Agitators",
            "Mixers",
            "Blenders",
        ],
        "Fittings": [
            "Unions",
            "Elbows",
            "Tees",
            "Reducers",
            "Tubes",
        ],
        "Valves": [
            "Butterfly Valves",
            "Seat Valves",
            "Diaphragm Valves",
            "Process Valves",
        ],
        "Skids": [
            "Mixing and Blending",
            "CIP Systems",
            "Heat Treatment",
            "Product Recovery",
            "Valve Manifolds",
            "More Skids",
        ],
    },

    "Pressure Regulator": {
        "icon": "sliders2",
        "General": [
            "High Pressure Regulator",
            "Two Stage Regulator",
            "Relief & Back Pressure",
            "UHP Core Valve",
            "Low Pressure Regulator",
            "Precision Regulator",
            "Inline and Y Type Filters",
        ],
    },

    "COVID19 Prevention Products and Tools": {
        "icon": "shield-check",
        "General": [
            "Hygiene Tools",
            "Human Body Temperature Measurement System",
        ],
    },

    "Acid Neutralizer": {
        "icon": "droplet",
        "General": [],
    },

    "GRACO Products": {
        "icon": "box",
        "General": [],
    },

    "Godrej Motors": {
        "icon": "gear",
        "General": [],
    },
}


class Command(BaseCommand):
    help = "Populate the Accutech product category hierarchy."

    def handle(self, *args, **options):
        category_count = 0
        subcategory_count = 0
        type_count = 0

        for category_order, (category_name, category_data) in enumerate(
            PRODUCT_STRUCTURE.items(),
            start=1
        ):
            category, created = ProductCategory.objects.get_or_create(
                slug=slugify(category_name),
                defaults={
                    "name": category_name,
                    "icon": category_data.get("icon", ""),
                    "order": category_order,
                },
            )

            if not created:
                category.name = category_name
                category.icon = category_data.get("icon", "")
                category.order = category_order
                category.is_active = True
                category.save()

            category_count += 1

            for sub_order, (subcategory_name, product_types) in enumerate(
                (
                    (key, value)
                    for key, value in category_data.items()
                    if key != "icon"
                ),
                start=1
            ):
                subcategory, created = ProductSubCategory.objects.get_or_create(
                    category=category,
                    slug=slugify(subcategory_name),
                    defaults={
                        "name": subcategory_name,
                        "order": sub_order,
                    },
                )

                if not created:
                    subcategory.name = subcategory_name
                    subcategory.order = sub_order
                    subcategory.is_active = True
                    subcategory.save()

                subcategory_count += 1

                for type_order, type_name in enumerate(
                    product_types,
                    start=1
                ):
                    product_type, created = ProductType.objects.get_or_create(
                        subcategory=subcategory,
                        slug=slugify(type_name),
                        defaults={
                            "name": type_name,
                            "order": type_order,
                        },
                    )

                    if not created:
                        product_type.name = type_name
                        product_type.order = type_order
                        product_type.is_active = True
                        product_type.save()

                    type_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Product hierarchy populated successfully.\n"
                f"Categories: {category_count}\n"
                f"Subcategories: {subcategory_count}\n"
                f"Product types: {type_count}"
            )
        )