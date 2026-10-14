# Invoice inbox

Keep the original invoice beside the extracted draft. A reviewer needs evidence, not just parser confidence.

Read an approved mailbox. Deduplicate by identifier and file hash. Extract supplier, invoice reference, dates, currency, lines and tax. Match the supplier and check for existing invoices.

Missing fields, uncertain extraction and possible duplicates go to review. A person validates before posting. Archive the checked document and read back the authorised accounting write.

Each stage needs an idempotency key. If a write times out, inspect the destination before retrying. Failed items must remain visible.

Test duplicate attachments, credit notes, mixed tax, unsupported currency and partial failures. [See the fictional interface](https://usecompai.com/projects/invoice-inbox.html).
