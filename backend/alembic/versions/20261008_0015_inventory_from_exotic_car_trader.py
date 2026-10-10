"""Replace the inherited inventory with the current Car Store spreadsheet.

Revision ID: 20261008_0015
Revises: 20261001_0014
Create Date: 2026-10-08
"""

from datetime import datetime

from alembic import op
import sqlalchemy as sa


revision = "20261008_0015"
down_revision = "20261001_0014"
branch_labels = None
depends_on = None

CREATED_AT = datetime(2026, 10, 8)
LOCATION = "Cherryville, NC"


def vehicle(slug, title, make, model, trim, year, price, vin, body_type,
            engine, transmission, drivetrain, exterior, interior, listing,
            carfax, features, description):
    info = [
        {"label": "Mileage", "value": "Contact us for current mileage"},
        {"label": "Engine", "value": engine},
        {"label": "Transmission", "value": transmission},
        {"label": "Drivetrain", "value": drivetrain},
        {"label": "Exterior Color", "value": exterior},
        {"label": "Interior Color", "value": interior},
        {"label": "Listing", "value": listing},
        {"label": "Vehicle History", "value": carfax},
    ]
    return {
        "id": slug,
        "slug": slug,
        "title": title,
        "make": make,
        "model": model,
        "trim": trim,
        "year": year,
        "status": "Available",
        "stock_number": None,
        "vin": vin,
        "price": price,
        # The sheet has no current odometer values. Avoid copying stale figures
        # from the third-party listings; the UI treats zero as unlisted.
        "mileage": 0,
        "body_type": body_type,
        "transmission": transmission,
        "drivetrain": drivetrain,
        "engine": engine,
        "exterior_color": exterior,
        "interior_color": interior,
        "location": LOCATION,
        "short_description": description,
        "description": description,
        "images": [],
        "features": features,
        "specs": {"listing_url": listing, "carfax_url": carfax},
        "details": {"info": info},
        "featured": False,
        "financing_available": False,
        "warranty_available": True,
        "delivery_available": True,
    }


VEHICLES = [
    vehicle("2021-lexus-lx570-inspiration-series", "2021 Lexus LX570 Inspiration Series", "Lexus", "LX570", "Inspiration Series", 2021, 49999, "JTJDY7AX9M4338202", "SUV", "5.7L Naturally Aspirated V8", "8-Speed Automatic", "AWD", "Black Onyx", "Black/Red", "https://www.exoticcartrader.com/listing/2021-lexus-lx570-260557794", "https://autohelperbot.com/en/carfax/4f9f9be4915faa678b3f76c28dcdb168", ["Inspiration Series Package", "Luxury Package", "Mark Levinson surround sound", "Head-up display", "Wireless charger", "Cool box"], "Black Onyx Lexus LX570 Inspiration Series with a 5.7L V8, all-wheel drive, and premium Inspiration Series equipment."),
    vehicle("2025-mercedes-benz-gle63-s-amg-coupe", "2025 Mercedes-Benz GLE63 S AMG Coupe", "Mercedes-Benz", "GLE63 S AMG", "Coupe", 2025, 78499, "4JGFD8KB1SB276556", "SUV", "4.0L Twin-Turbocharged V8", "9-Speed AMG SPEEDSHIFT Automatic", "AWD", "Cirrus Silver Metallic", "Macchiato Beige/Black", "https://www.exoticcartrader.com/listing/2025-mercedes-benz-gle63-s-amg-260556906", "https://autohelperbot.com/en/carfax/b946ab4b3057543fe1680955ff1f487d", ["AMG Night Package", "Driver Assistance Package", "4-zone climate control", "STEK DYNOmatte satin paint protection film", "Larte Design carbon-fiber aero pieces"], "Cirrus Silver AMG GLE 63 S Coupe with a hand-built twin-turbo V8 and 4MATIC all-wheel drive."),
    vehicle("2025-bmw-m4-competition-xdrive", "2025 BMW M4 Competition xDrive", "BMW", "M4", "Competition xDrive", 2025, 63999, "WBS33HK05SCS26674", "Coupe", "3.0L Twin-Turbocharged I6", "8-Speed M Steptronic Automatic", "AWD", "Tanzanite Blue II Metallic", "Tartufo Merino Leather", "https://www.exoticcartrader.com/listing/2025-bmw-m4-260353522", "https://autohelperbot.com/en/carfax/c929f436f7bccc2f8fcfd68324a2e0bc", ["Competition Package", "M xDrive", "Executive Package", "Driving Assistance Professional", "Parking Assistance Package", "Carbon fiber trim"], "Tanzanite Blue M4 Competition with a twin-turbo inline-six, M Steptronic transmission, and xDrive."),
    vehicle("2025-bmw-m3-competition-xdrive", "2025 BMW M3 Competition xDrive", "BMW", "M3", "Competition xDrive", 2025, 59999, "WBS33HJ07SFT92789", "Sedan", "3.0L Twin-Turbocharged I6", "8-Speed M Steptronic Automatic", "AWD", "Grey Black", "Ivory White Full Merino Leather", "https://www.exoticcartrader.com/listing/2025-bmw-m3-260251832", "https://autohelperbot.com/en/carfax/42e0a962f5a839cae2cb386426be0415", ["M Carbon Exterior Package", "M Carbon Bucket Seats", "Executive Package", "Driving Assistance Professional", "M Drive Professional"], "BMW M3 Competition with a twin-turbo inline-six, xDrive all-wheel drive, and M performance equipment."),
    vehicle("2025-bmw-x5-xdrive40i-silver-anniversary", "2025 BMW X5 xDrive40i Silver Anniversary Edition", "BMW", "X5", "xDrive40i Silver Anniversary Edition", 2025, 42999, "5UX23EU09S9Z65783", "SUV", "3.0L Twin-Turbocharged I6 with 48V Mild-Hybrid", "8-Speed Automatic", "AWD", "Lime Rock Grey Metallic", "Cognac Sensafin", "https://www.exoticcartrader.com/listing/2025-bmw-x5-250941883", "https://autohelperbot.com/en/carfax/c79a4aff8fbc7f361d6316322d62120b", ["Silver Anniversary Edition", "Off-Road Package", "Parking Assistance Package", "2-axle air suspension", "Harman Kardon audio", "Head-up display"], "X5 xDrive40i Silver Anniversary Edition with a mild-hybrid turbo inline-six and all-wheel drive."),
    vehicle("2020-bmw-m760i-xdrive", "2020 BMW M760i xDrive", "BMW", "7 Series", "M760i xDrive", 2020, 40999, "WBA7U6C03LBM63001", "Sedan", "6.6L Twin-Turbocharged V12", "8-Speed Automatic", "AWD", "Bernina Grey Amber Effect", "Black Nappa Leather", "https://www.exoticcartrader.com/listing/2020-bmw-m760i-xdrive-1", "https://autohelperbot.com/en/carfax/68b06c9429a6414d314f2aa5d19f4362", ["Driving Assistance Professional", "Panoramic Sky Lounge LED roof", "Bowers & Wilkins audio", "Icon Adaptive LED headlights", "Ambient Air Package"], "BMW M760i xDrive luxury sedan with a twin-turbo V12 and all-wheel drive."),
    vehicle("2024-bmw-m4-competition-xdrive-convertible", "2024 BMW M4 Competition xDrive Convertible", "BMW", "M4", "Competition xDrive Convertible", 2024, 56999, "WBS33BA07RCN40223", "Convertible", "3.0L Twin-Turbocharged I6", "8-Speed M Steptronic Automatic", "AWD", "Black Sapphire Metallic", "Black Extended Merino Leather", "https://www.exoticcartrader.com/listing/2024-bmw-m4-260252751", "https://autohelperbot.com/en/carfax/4ed66d9c7e91d9d7b0dbc87e85357573", ["Driving Assistance Professional", "Executive Package", "Parking Assistance Package", "Neck warmer", "M Compound brakes", "Carbon fiber trim"], "M4 Competition xDrive Convertible with a twin-turbo inline-six and retractable hardtop."),
    vehicle("2024-gmc-sierra-2500-at4", "2024 GMC Sierra 2500 AT4", "GMC", "Sierra 2500HD", "AT4 Crew Cab", 2024, 51999, "1GT49PEY0RF312814", "Truck", "6.6L Duramax Turbo-Diesel V8", "10-Speed Allison Automatic", "4WD", "Summit White", "Jet Black with Kalahari Accents", "https://www.exoticcartrader.com/listing/2024-gmc-sierra-2500-260149223", "https://autohelperbot.com/en/carfax/b89db26ca1e2130d99dcc284867109c0", ["AT4 Premium Plus Package", "Gooseneck/5th Wheel Package", "Camper Package", "MultiPro tailgate", "6.5-inch lift", "FOX shocks"], "Sierra 2500HD AT4 Crew Cab with a Duramax diesel V8, Allison transmission, and four-wheel drive."),
    vehicle("2025-chevrolet-corvette-z06-convertible-2lz", "2025 Chevrolet Corvette Z06 Convertible 2LZ", "Chevrolet", "Corvette Z06", "Convertible 2LZ", 2025, 86999, "1G1YE3D32S5601984", "Convertible", "5.5L Naturally Aspirated V8", "8-Speed Dual-Clutch Automatic", "RWD", "Red Mist Metallic Tintcoat", "Jet Black", "https://www.exoticcartrader.com/listing/2025-chevrolet-corvette-251247726", "https://autohelperbot.com/en/carfax/579d5b0602af05fb918fe4f32578c73c", ["Front lift with memory", "GT2 bucket seats", "Carbon Flash convertible roof", "Forged aluminum wheels", "Performance Data Recorder"], "Corvette Z06 Convertible with a naturally aspirated 5.5L V8 and dual-clutch transmission."),
    vehicle("2022-gmc-sierra-1500-elevation", "2022 GMC Sierra 1500 Elevation", "GMC", "Sierra 1500", "Elevation", 2022, 29999, "3GTUUCETXNG505475", "Truck", "3.0L Duramax Turbo-Diesel I6", "10-Speed Automatic", "4WD", "Onyx Black", "Jet Black", "https://www.exoticcartrader.com/listing/2022-gmc-sierra-1500-251247495", "https://autohelperbot.com/en/carfax/effce80d915daef1ed0b3b777b45e0c8", ["Elevation Premium Package", "X31 Off-Road & Protection Package", "Elevation Black Package", "Front bucket seats", "20-inch black aluminum wheels"], "Sierra 1500 Elevation with a Duramax turbo-diesel inline-six and four-wheel drive."),
    vehicle("2021-gmc-sierra-1500-denali", "2021 GMC Sierra 1500 Denali", "GMC", "Sierra 1500", "Denali", 2021, 26999, "3GTU9FED5MG279159", "Truck", "5.3L EcoTec3 V8", "10-Speed Automatic", "4WD", "Satin Steel Metallic", "Jet Black Leather", "https://www.exoticcartrader.com/listing/2021-gmc-sierra-250331649", "https://autohelperbot.com/en/carfax/ec8a0c7f951f9e810ba7c668ca0ca250", ["Technology Package", "Driver Alert Package II", "Power sunroof", "DiamondBack bed cover", "Aftermarket wheels and lift"], "Sierra 1500 Denali Crew Cab with a 5.3L V8, four-wheel drive, and premium Denali equipment."),
    vehicle("2025-cadillac-ct5-v-blackwing", "2025 Cadillac CT5-V Blackwing", "Cadillac", "CT5-V", "Blackwing", 2025, 82999, "1G6D35R60S0810411", "Sedan", "6.2L Supercharged V8", "10-Speed Automatic", "RWD", "Typhoon Metallic", "Natural Tan/Jet Black", "https://www.exoticcartrader.com/listing/2025-cadillac-ct5-v-250839960", "https://autohelperbot.com/en/carfax/a2e899f4df8194d11032c39457e7f7c5", ["Precision Package", "Super Cruise 1 Package", "Performance Data & Video Recorder", "Tech Bronze wheels", "Ultra View sunroof"], "CT5-V Blackwing with a supercharged 6.2L V8, rear-wheel drive, and performance equipment."),
    vehicle("2023-cadillac-ct5-v-blackwing-edition", "2023 Cadillac CT5-V Blackwing Edition", "Cadillac", "CT5-V", "Blackwing Edition", 2023, 63999, "1G6DY5R66P0810390", "Sedan", "6.2L Supercharged V8", "10-Speed Automatic", "RWD", "Summit White", "Not listed", "https://www.exoticcartrader.com/listing/2023-cadillac-ct5-v-blackwing-edition-1", "https://autohelperbot.com/en/carfax/f158f464b376d79e80d3d97c0f34af78", ["Driver Assist Package", "Brembo brakes", "Magnetic Ride Control", "AKG 16-speaker audio", "Torch Red seat belts", "Head-up display"], "CT5-V Blackwing Edition performance sedan with a supercharged V8 and rear-wheel drive."),
    vehicle("2022-cadillac-escalade-premium-luxury-4wd", "2022 Cadillac Escalade 4WD Premium Luxury", "Cadillac", "Escalade", "Premium Luxury 4WD", 2022, 47999, "1GYS4BKLXNR221456", "SUV", "6.2L V8", "10-Speed Automatic", "4WD", "Black Raven", "Brandy/Dark Atmosphere", "https://www.exoticcartrader.com/listing/2022-cadillac-escalade-4wd-premium-luxury-1", "https://autohelperbot.com/en/carfax/c7c89c8c31108289c420543d487ef552", ["Premium Luxury trim", "Super Cruise", "Full leather seats", "2-way lumbar front seats", "10-speed automatic"], "Escalade Premium Luxury with a 6.2L V8, four-wheel drive, and Super Cruise capability."),
    vehicle("2023-cadillac-escalade-sport-platinum-onyx", "2023 Cadillac Escalade Sport Platinum 4WD Onyx Package", "Cadillac", "Escalade", "Sport Platinum 4WD Onyx Package", 2023, 64999, "1GYS4GKL9PR444569", "SUV", "6.2L V8", "10-Speed Automatic", "4WD", "Black Raven", "Dark Auburn/Black Accents", "https://www.exoticcartrader.com/listing/2023-cadillac-escalade-sport-platinum-4wd-onyx-package-1", "https://autohelperbot.com/en/carfax/a9c05e611cac5b6310309a938b4f669d", ["Onyx Package", "Rear-seat entertainment", "AKG 36-speaker audio", "Super Cruise", "Power-retractable assist steps"], "Escalade Sport Platinum with Onyx Package, a 6.2L V8, and four-wheel drive."),
    vehicle("2024-cadillac-escalade-v", "2024 Cadillac Escalade V", "Cadillac", "Escalade-V", "V-Series", 2024, 94999, "1GYS4HK9XRR161093", "SUV", "6.2L Supercharged V8", "10-Speed Automatic", "AWD", "Dark Emerald Metallic", "Jet Black", "https://www.exoticcartrader.com/listing/2024-cadillac-escalade-v-1", "https://autohelperbot.com/en/carfax/36077374d79e1519a8cc0d88e8b8297f", ["20th Anniversary V-Series Package", "Onyx Package", "22-inch forged wheels", "Console refrigerator/freezer", "Head-up display"], "Escalade-V with a supercharged 6.2L V8, 10-speed automatic, and all-wheel drive."),
    vehicle("2020-mercedes-benz-g63-amg-4matic", "2020 Mercedes-Benz G63 AMG 4MATIC", "Mercedes-Benz", "G-Class", "AMG G63 4MATIC", 2020, 94999, "W1NYC7HJ8LX360573", "SUV", "4.0L Twin-Turbocharged V8", "9-Speed AMG SPEEDSHIFT Automatic", "AWD", "G Manufaktur Monza Grey Magno", "Designo Classic Red/Black Nappa Leather", "https://www.exoticcartrader.com/listing/2020-mercedes-benz-amg-g63-4matic-1", "https://autohelperbot.com/en/carfax/e2905d868ac66c5b307a86fc6c5f17c2", ["AMG Night Package", "Exclusive Interior Package", "AMG carbon-fiber trim", "Forged AMG wheels", "Three locking differentials"], "Mercedes-AMG G63 4MATIC with a twin-turbo V8, all-wheel drive, and distinctive Monza Grey Magno finish."),
    vehicle("2025-chevrolet-corvette-e-ray-convertible-3lz", "2025 Chevrolet Corvette E-Ray Convertible 3LZ", "Chevrolet", "Corvette E-Ray", "Convertible 3LZ", 2025, 89999, "1G1YM3D48S5500458", "Convertible", "6.2L V8 with Front Electric Motor", "8-Speed Dual-Clutch Automatic", "eAWD", "Red Mist Metallic", "Jet Black with Adrenaline Red", "https://www.exoticcartrader.com/listing/2025-chevrolet-corvette-250434052", "https://autohelperbot.com/en/carfax/f62b7df3c6d1784b0b4d73a6f8501cc1", ["Front-axle electric motor", "Carbon-fiber interior trim", "Front lift with memory", "GT2 bucket seats", "Power-retractable hardtop"], "Corvette E-Ray Convertible with a 6.2L V8, front electric motor, and eAWD hybrid drivetrain."),
]

for index, item in enumerate(VEHICLES):
    item["featured"] = index < 4


def vehicles_table():
    return sa.table(
        "vehicles",
        sa.column("id", sa.String), sa.column("slug", sa.String), sa.column("title", sa.String),
        sa.column("make", sa.String), sa.column("model", sa.String), sa.column("trim", sa.String),
        sa.column("year", sa.Integer), sa.column("status", sa.String), sa.column("stock_number", sa.String),
        sa.column("vin", sa.String), sa.column("price", sa.Integer), sa.column("mileage", sa.Integer),
        sa.column("body_type", sa.String), sa.column("transmission", sa.String), sa.column("drivetrain", sa.String),
        sa.column("engine", sa.String), sa.column("exterior_color", sa.String), sa.column("interior_color", sa.String),
        sa.column("location", sa.String), sa.column("short_description", sa.String), sa.column("description", sa.Text),
        sa.column("images", sa.JSON), sa.column("features", sa.JSON), sa.column("specs", sa.JSON),
        sa.column("details", sa.JSON), sa.column("featured", sa.Boolean), sa.column("financing_available", sa.Boolean),
        sa.column("warranty_available", sa.Boolean), sa.column("delivery_available", sa.Boolean), sa.column("created_at", sa.DateTime),
    )


def _previous_inventory():
    from importlib.util import module_from_spec, spec_from_file_location
    from pathlib import Path

    path = Path(__file__).with_name("20260928_0013_inventory_from_sheet.py")
    spec = spec_from_file_location("previous_car_store_inventory", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load the prior inventory migration for downgrade")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.VEHICLES


def upgrade():
    connection = op.get_bind()
    connection.execute(sa.text("UPDATE leads SET vehicle_id = NULL WHERE vehicle_id IS NOT NULL"))
    connection.execute(sa.text("DELETE FROM vehicles"))
    op.bulk_insert(vehicles_table(), [{**item, "created_at": CREATED_AT} for item in VEHICLES])


def downgrade():
    connection = op.get_bind()
    connection.execute(sa.text("UPDATE leads SET vehicle_id = NULL WHERE vehicle_id IS NOT NULL"))
    connection.execute(sa.text("DELETE FROM vehicles"))
    op.bulk_insert(vehicles_table(), [
        {**item, "created_at": datetime(2026, 9, 28)} for item in _previous_inventory()
    ])
