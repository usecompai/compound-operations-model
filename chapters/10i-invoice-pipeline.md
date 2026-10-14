# Invoice validator

The deployed invoice validator shows an original PDF beside editable extracted fields. A reviewer checks the supplier, invoice details and duplicate warnings before validating the record.

Duplicate warnings distinguish a match in the pending queue from an invoice already in the validated register. A warning does not discard a document automatically. The validated record remains linked to its document.

The service, current validation code and recently processed entries in the validated register were checked on 14 October 2026. This supports document review and validation. It does not establish autonomous accounting, payment or error-free extraction.

The public preview uses fictional documents and fields. [Explore the invoice validator](https://usecompai.com/projects/invoice-validator.html).

## Applying the method elsewhere

Keep extraction separate from approval. Test missing fields, duplicate invoices and failed writes. Read back the saved record before marking it complete. Any accounting export, posting or payment needs its own verified integration and authority; saving to a review register is not that outcome.
