"""
Structured site copy, kept separate from views/templates so it is easy to
update without touching presentation code. Sourced from the public content
of accutech.ae (Accutech Middle East FZCO / Abdulla Bin Hamid Trading LLC).
"""

SOLUTIONS = [
    {
        "slug": "pressure",
        "icon": "gauge",
        "title": "Pressure Measurement",
        "summary": "Transmitters, switches, gauges and deadweight testers rated "
                    "from vacuum to 100,000 psi for gauge, absolute and "
                    "differential pressure duties.",
        "detail": "Built for the harshest process conditions across oil & gas, "
                   "power and process plants, with HART and fieldbus "
                   "communication options for full plant integration.",
    },
    {
        "slug": "temperature",
        "icon": "thermometer",
        "title": "Temperature Measurement",
        "summary": "RTDs, thermocouples, transmitters and calibration baths for "
                    "precise, repeatable temperature control.",
        "detail": "Engineered for continuous duty in demanding industrial "
                   "environments, backed by our in-house calibration lab.",
    },
    {
        "slug": "force-level",
        "icon": "layers",
        "title": "Force & Level Measurement",
        "summary": "Load cells, force gauges and point/continuous level "
                    "instrumentation for tanks, hoppers and process vessels.",
        "detail": "Covers roto, tuning fork, RF/capacitance, ultrasonic and "
                   "load-cell based technologies for liquids and solids.",
    },
    {
        "slug": "flow",
        "icon": "activity",
        "title": "Flow Measurement",
        "summary": "Advanced digital and traditional mechanical flow meters "
                    "matched to your accuracy and process requirements.",
        "detail": "Sized and specified by our instrumentation engineers across "
                    "oil & gas, water treatment and process industries.",
    },
    {
        "slug": "calibration",
        "icon": "sliders",
        "title": "Calibration Services",
        "summary": "In-house calibration facility accredited to "
                   "ISO/IEC 17025:2005 (DAC) and certified to ISO 9001:2015 (BAS), "
                   "approved by WIKA.",
        "detail": "Full traceability from bidding through commissioning, keeping "
                   "your critical instruments accurate at every stage of a "
                   "project's life.",
    },
    {
        "slug": "sf6-gas",
        "icon": "wind",
        "title": "SF6 Gas Solutions",
        "summary": "Handling, monitoring and analysis equipment for SF6 gas used "
                    "in high-voltage switchgear.",
        "detail": "Complete lifecycle support for utilities and power "
                    "infrastructure customers across the region.",
    },
]

PRODUCT_CATEGORIES = [
    {
        "slug": "pressure-measurement",
        "icon": "speedometer2",
        "title": "Pressure Measurement",
        "subcategories": [
            "Pressure Gauges", "Pressure Gauges with Transmitter Switches",
            "Pressure Switches", "Pressure Transmitters", "Diaphragm Seals",
        ],
    },
    {
        "slug": "temperature-measurement",
        "icon": "thermometer-half",
        "title": "Temperature Measurement",
        "subcategories": [
            "Thermowells", "Mechanical Temperature Measurement",
            "Temperature Gauges with Transmitter Switches",
            "Temperature Switches", "Electrical Temperature Measurement",
        ],
    },
    {
        "slug": "controllers-indicators-recorders",
        "icon": "display",
        "title": "Controllers, Indicators & Recorders",
        "subcategories": ["Indicators", "Controllers", "Recorders"],
    },
    {
        "slug": "level-measurement",
        "icon": "layers",
        "title": "Level Measurement",
        "subcategories": [
            "Mechanical Level Measurement", "Level Switches", "Level Transmitters",
        ],
    },
    {
        "slug": "flow-measurement",
        "icon": "activity",
        "title": "Flow Measurement",
        "subcategories": ["Mechanical Flow Measurement", "Flow Transmitters"],
    },
    {
        "slug": "calibration-technology",
        "icon": "sliders",
        "title": "Calibration Technology",
        "subcategories": [
            "Pressure Calibration", "Temperature Calibration",
            "Current, Voltage & Resistance", "Humidity Calibration",
        ],
    },
    {
        "slug": "valves-and-fittings",
        "icon": "diagram-3",
        "title": "Valves & Fittings",
        "subcategories": [
            "Needle Valves", "Gauge Valves", "Ball Valves", "Manifold Valves",
            "Check Valves", "Instrumentation Tube & Pipe Fittings", "Relief Valves",
        ],
    },
    {
        "slug": "food-and-pharma",
        "icon": "droplet-half",
        "title": "Food & Pharma",
        "subcategories": [
            "Pumps", "Filters & Sight Glass", "Mixing Equipment",
            "Fittings", "Valves", "Skids",
        ],
    },
    {
        "slug": "pressure-regulator",
        "icon": "sliders2",
        "title": "Pressure Regulators",
        "subcategories": [
            "High Pressure Regulator", "Two Stage Regulator",
            "Relief & Back Pressure", "Low Pressure Regulator", "Precision Regulator",
        ],
    },
]

PROJECT_CATEGORIES = [
    {
        "slug": "mep",
        "icon": "building",
        "title": "MEP & District Cooling Jobs",
        "description": "Instrumentation and control solutions supplied and "
                        "commissioned across mechanical, electrical and "
                        "plumbing (MEP) works and district cooling plants "
                        "throughout the UAE.",
    },
    {
        "slug": "power",
        "icon": "lightning-charge",
        "title": "Power Generation, Distribution, Waste Water & Desalination",
        "description": "Measurement and control instrumentation for power "
                        "generation and distribution networks, waste water "
                        "treatment facilities, and desalination plants "
                        "across the region.",
    },
    {
        "slug": "oil",
        "icon": "fuel-pump",
        "title": "Oil & Gas",
        "description": "Pressure, temperature, flow and level instrumentation "
                        "engineered for upstream, midstream and downstream "
                        "oil & gas facilities.",
    },
]

BRAND_ROSTER = [
    "WIKA", "Winters", "Accutech", "Trafag", "ABB", "WIKA / Cella", "E+E",
    "Techtrol", "Kirchner & Tochter", "Racine", "Mueller", "Inoxpa",
    "Alco-Valves", "Maximator", "Alco", "Insert Deal", "Drastar",
    "Land Ametek", "AccuClean",
]


BRANDS = [
    {
        "name": "ABB",
        "role": "Confirmed ABB Value Provider",
        "note": "Authorized reseller and support partner for ABB's "
                "measurement product lines across the Middle East.",
    },
    {
        "name": "WIKA",
        "role": "Regional Partner",
        "note": "Our calibration lab is approved by WIKA, reinforcing the "
                "accuracy behind every instrument we supply.",
    },
    {
        "name": "Trafag",
        "role": "Sole Middle East Partner",
        "note": "Accutech is the only Trafag partner in the region, bringing "
                "Swiss-engineered pressure and level technology to local "
                "industry.",
    },
]

STATS = [
    {"value": "1996", "label": "Founded in the UAE"},
    {"value": "60+", "label": "Engineering & technical staff"},
    {"value": "17025", "label": "ISO/IEC accredited calibration lab"},
    {"value": "3", "label": "Decades of regional plant experience"},
]

CERTIFICATIONS = [
    "ISO/IEC 17025:2005 — DAC Accredited Calibration Laboratory",
    "ISO 9001:2015 — BAS Certified Quality Management",
    "Approved Calibration Partner of WIKA",
]

COMPANY = {
    "name": "Accutech",
    "legal_name": "Abdulla Bin Hamid Trading LLC (Accutech)",
    "tagline": "Precision instrumentation, engineered for industry.",
    "address": "Warehouse G-1, High Bay, Dubai Silicon Oasis, Dubai, United Arab Emirates",
    "phone": "+971 4 320 7944",
    "email": "sales@accutech.ae",
}
