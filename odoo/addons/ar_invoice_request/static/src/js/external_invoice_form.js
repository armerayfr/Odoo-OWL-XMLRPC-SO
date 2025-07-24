/** @odoo-module **/

import { Component, useState } from "@odoo/owl";

export class ExternalSaleInvoiceForm extends Component {
    setup() {
        this.state = useState({
            message: "Hello from OWL!",
        });
    }

    logMessage() {
        console.log(this.state.message);
        alert(this.state.message);
    }
}

ExternalSaleInvoiceForm.template = "external_invoice_form_template";
