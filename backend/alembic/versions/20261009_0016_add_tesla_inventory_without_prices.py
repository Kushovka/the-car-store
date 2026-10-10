"""Add Tesla inventory entries before prices are available.

Revision ID: 20261009_0016
Revises: 20261008_0015
Create Date: 2026-10-09
"""

from datetime import datetime

from alembic import op
import sqlalchemy as sa


revision = "20261009_0016"
down_revision = "20261008_0015"
branch_labels = None
depends_on = None

CREATED_AT = datetime(2026, 10, 9)
LOCATION = "Cherryville, NC"


def vehicle(slug, title, model, trim, year, vin, body_type):
    description = f"Call for current pricing and details on this {year} Tesla {model} {trim}."
    return {
        "id": slug,
        "slug": slug,
        "title": title,
        "make": "Tesla",
        "model": model,
        "trim": trim,
        "year": year,
        "status": "Available",
        "stock_number": None,
        "vin": vin,
        # Zero is the existing UI sentinel for "Call for Price".
        "price": 0,
        "mileage": 0,
        "body_type": body_type,
        "transmission": None,
        "drivetrain": None,
        "engine": None,
        "exterior_color": None,
        "interior_color": None,
        "location": LOCATION,
        "short_description": description,
        "description": description,
        "images": [],
        "features": [],
        "specs": {},
        "details": {},
        "featured": False,
        "financing_available": False,
        "warranty_available": True,
        "delivery_available": True,
    }


VEHICLES = [
    vehicle("2026-tesla-model-y-launch-edition", "2026 Tesla Model Y Launch Edition", "Model Y", "Launch Edition", 2026, "7SAYGDEE7TF329068", "SUV"),
    vehicle("2025-tesla-model-y-performance", "2025 Tesla Model Y Performance", "Model Y", "Performance", 2025, "7SAYGDEF4SA353302", "SUV"),
    vehicle("2024-tesla-cybertruck-cyberbeast-foundation", "2024 Tesla Cybertruck Cyberbeast Foundation", "Cybertruck", "Cyberbeast Foundation", 2024, "7G2CEHEE1RA010160", "Truck"),
    vehicle("2024-tesla-cybertruck-foundation-series", "2024 Tesla Cybertruck Foundation Series", "Cybertruck", "Foundation Series", 2024, "7G2CEHED9RA011502", "Truck"),
]


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


def upgrade():
    op.bulk_insert(vehicles_table(), [{**item, "created_at": CREATED_AT} for item in VEHICLES])


def downgrade():
    table = vehicles_table()
    slugs = [item["slug"] for item in VEHICLES]
    op.execute(sa.delete(table).where(table.c.slug.in_(slugs)))
