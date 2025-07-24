/** @odoo-module **/

import { mount } from "@odoo/owl";
import { ExternalSaleInvoiceForm } from "./external_invoice_form";

console.log("🚀 Waiting for DOM to mount OWL...");

document.addEventListener("DOMContentLoaded", () => {
  const mountEl = document.getElementById("external_invoice_mount");
  if (!mountEl) {
    console.error("❌ Element #external_invoice_mount not found");
    return;
  }

  const token = mountEl.dataset.token;
  console.log("✅ Mounting OWL with token:", token);

  mount(ExternalSaleInvoiceForm, {
    target: mountEl,
    props: { token },
  });
});
