#!/bin/sh

echo "test ODOO OWL XMLRPC SO"

# Start Odoo service in the background
/usr/bin/odoo -d INV_REQUEST_DB -i base,web &
ODOO_PID=$!

# Wait for Odoo to be ready (you might want to implement a better check here)
sleep 10

# Wait for Odoo process to finish
wait $ODOO_PID