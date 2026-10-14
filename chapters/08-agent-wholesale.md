# Delivery desk

A commercial order may split into several deliveries. Each needs its own warehouse reference, tracking and finance document.

Read the order, warehouse status and carrier events. Resolve the invoice by explicit document reference. An order reference may not uniquely identify payment, and tracking does not prove receipt.

Keep preparation, dispatch, delivery and exceptions distinct. Show missing references and timestamp source checks.

Prepare an invoice or collection task, but require approval for accounting writes and shipment release. Payment state comes from finance, not a message saying the customer paid.

Test split deliveries, partial fulfilment, missing stock, returned parcels and unmatched invoices. [Explore the fictional delivery desk](https://usecompai.com/projects/delivery-desk.html).
