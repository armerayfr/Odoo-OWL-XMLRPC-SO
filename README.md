
# 🧾 Odoo XML-RPC Invoice Request Project

Project ini merupakan integrasi antara Odoo dan backend client eksternal menggunakan **XML-RPC**, yang menyediakan API untuk membuat dan mengelola Sales Order secara terpisah dari Odoo.

## 📦 Struktur Project

```
project-root/
├── docker-compose.yml
├── odoo/
│   ├── config/
│   └── addons/
└── client_app/
    ├── main.py
    ├── requirements.txt
    ├── domain/
    ├── use_cases/
    ├── infrastructure/
    └── interfaces/
```

## ⚙️ a. Cara Setup Odoo dan Client Backend

1. **Persiapkan folder:**
   - `odoo/addons` berisi module custom seperti `ar_invoice_request`
   - `odoo/config/odoo.conf` (opsional) untuk konfigurasi Odoo

2. **Jalankan semua service:**

```bash
docker-compose up --build
```

3. **Akses Odoo:**
   - URL: http://localhost:8095
   - Login: `admin` / `admin`
   - Install addon `ar_invoice_request`

4. **Akses FastAPI Client:**
   - URL: http://localhost:8000/docs

## 🧪 b. Penjelasan Endpoint & Contoh Payload

### POST /so/create

```json
{
  "partner_id": 7,
  "order_lines": [
    { "product_id": 4, "quantity": 2 },
    { "product_id": 5, "quantity": 1 }
  ]
}
```

### GET /so/{so_id}

Ambil detail sales order berdasarkan ID.

### GET /so

Ambil semua sales order.

### POST /so/update

```json
{
  "sale_order_id": 12,
  "updates": {
    "note": "Diperbarui oleh API",
    "payment_term_id": 1
  }
}
```

### POST /so/{so_id}/confirm

Konfirmasi SO.

### POST /so/{so_id}/cancel

Cancel SO (gunakan context: `disable_cancel_warning=True`).

### POST /so/{so_id}/reset

Reset ke draft.

## 📬 c. Cara Menjalankan dengan Postman

1. Import file `odoo_xmlrpc_client.postman_collection.json`
2. Pastikan FastAPI jalan di `http://localhost:8000`
3. Jalankan API via tab Postman Collection

## 🐳 d. Docker Compose File

```yaml
version: '3.1'
services:
  web:
    build: ./odoo
    depends_on:
      - db
    ports:
      - "5680:5680"
      - "8095:8069"
    volumes:
      - "./odoo/config:/etc/odoo"
      - "./odoo/addons:/mnt/extra-addons/addons"
      - odoo-web-data:/var/lib/odoo

  db:
    image: postgres:14
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_PASSWORD=pass
      - POSTGRES_USER=odoo17
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - odoo-db-data:/var/lib/postgresql/data/pgdata
    ports:
      - "5495:5432"

  client:
    build:
      context: ./client_app
    ports:
      - "8000:8000"
    depends_on:
      - web

volumes:
  odoo-web-data:
  odoo-db-data:
```

## 📎 Catatan Tambahan

- Pastikan Odoo sudah jalan penuh sebelum client mengaksesnya
- Untuk extensibility, struktur sudah clean (infrastructure, use_cases, domain)
