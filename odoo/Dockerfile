FROM odoo:17.0

USER root

# COPY ./config/requirements.txt /etc/odoo/requirements.txt
# COPY ./addons/addons /usr/lib/python3/dist-packages/odoo/addons

# RUN pip3 install -r /etc/odoo/requirements.txt

# Copy entrypoint script
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER odoo

ENTRYPOINT ["/entrypoint.sh"]