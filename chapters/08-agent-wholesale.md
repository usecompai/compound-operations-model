# Wholesale invoicing

The internal tool reads warehouse orders, matches products and checks an approved price list. An operator reviews the proposed proforma or invoice before creating it in accounting.

After creation, the workflow reads the document back and records its identifier, quantities and totals. Missing products or unapproved prices stop the process. A successful preview is not a created document.

On 14 October 2026, the deployed service, current code and recent invoice and proforma records were checked. A recent invoice was independently found through the accounting API. This is an operator-led production workflow, not unattended order-to-cash.

[Explore wholesale invoicing](https://usecompai.com/projects/wholesale-invoicing.html). The public preview uses fictional orders and creates no document. It does not represent carrier selection, shipment release or payment collection. The earlier Delivery desk illustration remains withdrawn.

## Applying the method elsewhere

Keep the warehouse order, commercial terms and accounting document linked. Preserve price approvals. Check the destination before retrying an uncertain creation so a timeout cannot become a duplicate invoice. Share the method, not customer records or price lists.
