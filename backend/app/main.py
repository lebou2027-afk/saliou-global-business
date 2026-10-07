from __future__ import annotations

from sqlalchemy.orm import Session

from .models import Client, Invoice, Product, Sale, User, Vendor


def seed_demo_data(db: Session) -> None:
    if db.query(User).first() is not None:
        return

    admin = User(
        full_name="Administrateur SALIOU",
        email="admin@saliou.com",
        password="admin123",
        role="admin",
    )
    db.add(admin)

    client_1 = Client(name="Mouhamed Diop", email="m.diop@client.com", phone="+221 77 000 0001", city="Dakar", company="Asteria")
    client_2 = Client(name="Awa Sarr", email="a.sarr@client.com", phone="+221 77 000 0002", city="Saint-Louis", company="Nori Commerce")
    client_3 = Client(name="Baba Ba", email="b.ba@client.com", phone="+221 77 000 0003", city="Thiès", company="Sunrise Ltd")
    db.add_all([client_1, client_2, client_3])

    vendor_1 = Vendor(name="Keur Supply", contact="M. Fall", phone="+221 78 111 1111", city="Dakar")
    vendor_2 = Vendor(name="Global Feed", contact="Mme Ndiaye", phone="+221 78 222 2222", city="Kaolack")
    db.add_all([vendor_1, vendor_2])

    product_1 = Product(name="Ordinateur Portable Pro", sku="LAP-001", category="Technologie", unit_price=450000, cost_price=320000, stock_quantity=12, low_stock_threshold=5)
    product_2 = Product(name="Imprimante Laser", sku="PRN-002", category="Office", unit_price=260000, cost_price=180000, stock_quantity=7, low_stock_threshold=4)
    product_3 = Product(name="Scanner Portable", sku="SCN-003", category="Office", unit_price=180000, cost_price=120000, stock_quantity=3, low_stock_threshold=5)
    product_4 = Product(name="Accessoires Bureau", sku="ACC-004", category="Divers", unit_price=9000, cost_price=5000, stock_quantity=40, low_stock_threshold=10)
    db.add_all([product_1, product_2, product_3, product_4])

    db.flush()

    sale_1 = Sale(client_id=client_1.id, product_id=product_1.id, quantity=2, unit_price=450000, total_amount=900000, status="paid")
    sale_2 = Sale(client_id=client_2.id, product_id=product_2.id, quantity=1, unit_price=260000, total_amount=260000, status="paid")
    sale_3 = Sale(client_id=client_3.id, product_id=product_4.id, quantity=15, unit_price=9000, total_amount=135000, status="pending")
    db.add_all([sale_1, sale_2, sale_3])

    invoice_1 = Invoice(client_id=client_1.id, total_amount=900000, status="paid")
    invoice_2 = Invoice(client_id=client_2.id, total_amount=260000, status="pending")
    db.add_all([invoice_1, invoice_2])

    db.commit()
