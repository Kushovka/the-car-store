"""Write fuller, equipment-led descriptions for the current inventory.

Revision ID: 20261009_0019
Revises: 20261009_0018
Create Date: 2026-10-09
"""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import re

from alembic import op
import sqlalchemy as sa


revision = "20261009_0019"
down_revision = "20261009_0018"
branch_labels = None
depends_on = None


def vehicles_table():
    return sa.table(
        "vehicles",
        sa.column("slug", sa.String),
        sa.column("title", sa.String),
        sa.column("body_type", sa.String),
        sa.column("engine", sa.String),
        sa.column("transmission", sa.String),
        sa.column("drivetrain", sa.String),
        sa.column("exterior_color", sa.String),
        sa.column("interior_color", sa.String),
        sa.column("features", sa.JSON),
        sa.column("description", sa.Text),
    )


def _load_migration(filename, module_name):
    path = Path(__file__).with_name(filename)
    spec = spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {filename}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _restore_previous_descriptions(connection, table):
    sources = (
        ("20261009_0017_import_csc_site_photos_and_info.py", "previous_photos"),
        ("20261008_0015_inventory_from_exotic_car_trader.py", "previous_sheet"),
    )
    for filename, module_name in sources:
        module = _load_migration(filename, module_name)
        for item in module.VEHICLES:
            connection.execute(
                table.update().where(table.c.slug == item["slug"]).values(description=item["description"])
            )


def _clean_features(features, title, engine, transmission, drivetrain, exterior, interior):
    excluded = [title, engine, transmission, drivetrain, exterior, interior]
    selected = []
    for feature in features or []:
        value = str(feature).strip()
        lowered = value.lower()
        if not value or any(lowered == str(item or "").strip().lower() for item in excluded):
            continue
        if value.lower().startswith(("exterior:", "interior:", "engine:", "transmission:", "drivetrain:")):
            continue
        if re.search(r"\b(AWD|RWD|FWD|4WD)\b", value, re.IGNORECASE):
            continue
        if any(term in lowered for term in (" exterior", " interior", "transmission", "drivetrain", "wheel drive", " engine", "wrap")):
            continue
        if engine and (lowered in str(engine).lower() or str(engine).lower() in lowered):
            continue
        if exterior and str(exterior).lower() in lowered:
            continue
        if interior and str(interior).lower() in lowered:
            continue
        if "speed" in lowered and ("automatic" in lowered or "dual-clutch" in lowered):
            continue
        if len(value) > 80 or value.endswith(":"):
            continue
        if engine and "battery" in str(engine).lower() and "motor" in lowered:
            continue
        if value[:4].isdigit() or lowered.startswith(("tesla ", "bmw ", "cadillac ", "gmc ", "lexus ", "mercedes", "chevrolet ")):
            continue
        value = re.sub(r"\s*-\s*might require activation.*$", "", value, flags=re.IGNORECASE).strip()
        if value not in selected:
            selected.append(value)
        if len(selected) == 3:
            break
    return selected


def _description(vehicle):
    title = vehicle["title"]
    engine = vehicle["engine"]
    transmission = vehicle["transmission"]
    drivetrain = vehicle["drivetrain"]
    exterior = vehicle["exterior_color"]
    interior = vehicle["interior_color"]
    if interior and any(term in interior.lower() for term in ("package", "not listed", "unknown")):
        interior = None
    if "cybertruck foundation series" in title.lower() and "cyberbeast" not in title.lower():
        exterior = "Army Green wrap over stainless steel"
    options = _clean_features(
        vehicle["features"], title, engine, transmission, drivetrain, exterior, interior
    )

    feature_values = [str(item) for item in (vehicle["features"] or [])]
    displacement = re.search(r"\d+(?:\.\d+)?L", engine or "", re.IGNORECASE)
    detailed_engine = next(
        (
            item
            for item in feature_values
            if displacement
            and displacement.group(0).lower() in item.lower()
            and any(term in item.lower() for term in ("supercharged", "turbo", "mild-hybrid", "electric motor"))
        ),
        engine,
    )
    if detailed_engine:
        detailed_engine = re.sub(r"\s+engine$", "", detailed_engine, flags=re.IGNORECASE)
    if "cyberbeast" in title.lower():
        detailed_engine = "tri-motor electric powertrain"
        transmission = "direct-drive transmission"
        drivetrain = "all-wheel drive"
    elif "cybertruck" in title.lower():
        detailed_engine = "dual-motor electric powertrain"
        transmission = "single-speed transmission"
        drivetrain = "all-wheel drive"
    elif engine and "battery" in engine.lower():
        motors = next((item for item in feature_values if "motor" in item.lower()), "dual electric motors")
        detailed_engine = f"electric propulsion with a {engine} and {motors.lower()}"
    elif "g63" in title.lower():
        detailed_engine = "4.0L twin-turbocharged V8"
    elif "m760i" in title.lower():
        detailed_engine = "6.6L twin-turbocharged V12"

    if drivetrain == "Front-Wheel Drive (FWD)" and "cybertruck" in title.lower():
        drivetrain = "all-wheel drive"
    detailed_transmission = next(
        (
            str(item)
            for item in feature_values
            if "speed" in str(item).lower()
            and ("automatic" in str(item).lower() or "dual-clutch" in str(item).lower())
        ),
        transmission,
    )
    if "cyberbeast" in title.lower():
        detailed_transmission = "direct-drive transmission"
    elif "cybertruck" in title.lower():
        detailed_transmission = "single-speed transmission"
    elif detailed_transmission == "Automatic":
        detailed_transmission = "automatic transmission"
    opening = f"The {title} is powered by {detailed_engine or 'its listed powertrain'}"
    if detailed_transmission:
        opening += f"; {detailed_transmission} sends power"
        if drivetrain:
            opening += f" to {drivetrain}"
    elif drivetrain:
        opening += f" with {drivetrain}"
    opening += "."

    if exterior and interior:
        second = f"It is finished in {exterior} with a {interior} cabin"
    elif exterior:
        second = f"It is finished in {exterior}"
    elif interior:
        second = f"Its cabin is trimmed in {interior}"
    else:
        second = "It is presented in its listed factory configuration"

    if options:
        equipment = ", ".join(options[:-1])
        if len(options) > 1:
            equipment += f" and {options[-1]}"
        else:
            equipment = options[0]
        second += f"; listed equipment includes {equipment}."
    elif vehicle["body_type"]:
        second += f". The listing identifies it as a {str(vehicle['body_type']).lower()} in {vehicle['title'].split()[-1]} specification."
    else:
        second += ". Contact us for more information about its equipment."

    return f"{opening} {second}"


def upgrade():
    connection = op.get_bind()
    table = vehicles_table()
    rows = connection.execute(sa.select(*table.c)).mappings().all()
    for vehicle in rows:
        connection.execute(
            table.update()
            .where(table.c.slug == vehicle["slug"])
            .values(description=_description(vehicle))
        )


def downgrade():
    connection = op.get_bind()
    _restore_previous_descriptions(connection, vehicles_table())
