from fastapi import APIRouter
from domain.models import *
from infrastructure.odoo_xmlrpc import OdooXMLRPCClient
from use_cases.sale_order_service import SaleOrderService

router = APIRouter()
odoo = OdooXMLRPCClient("http://web:8069", "INV_REQUEST_DB", "admin", "admin")
so_service = SaleOrderService(odoo)

@router.post("/so/create")
def create_so(payload: SaleOrderCreate):
    data = payload.dict()
    return {"id": so_service.create(data["partner_id"], data["order_lines"])}

@router.get("/so/{so_id}")
def get_so(so_id: int):
    return so_service.read(so_id)

@router.get("/so")
def get_all_so():
    return so_service.search()

@router.post("/so/{so_id}/confirm")
def confirm_so(so_id: int):
    return {"status": so_service.confirm(so_id)}

@router.post("/so/{so_id}/cancel")
def cancel_so(so_id: int):
    return {"status": so_service.cancel(so_id)}

@router.post("/so/{so_id}/reset")
def reset_so(so_id: int):
    return {"status": so_service.reset_draft(so_id)}

@router.post("/so/update")
def update_so(payload: SaleOrderUpdate):
    return {
        "status": so_service.update(payload.sale_order_id, payload.updates)
    }
