# Cash position

A treasury view brings connected account balances and reviewed manual entries together. Available cash and recoverable amounts remain separate. Saved daily snapshots provide a history of the recorded position.

## Reading the position

Show the source and date beside each balance. Mark manual entries as manual. A failed connection is a gap, not a zero. Comparing recorded days can reveal an unusual change, but it does not explain the cause or authorise a transfer.

The current position, historical reads and change checks were tested on 16 October 2026. The history repair connects the company tool to the existing private service API. Stored decimal amounts are compared without treating absent days as balances. Private snapshot files remain private.

The scheduled snapshot flow is running. These checks establish working reads, not how often people open the interface. This is not a cash-flow forecast, payment engine or substitute for bank reconciliation.

[Explore cash position](https://usecompai.com/projects/cash-position.html). The preview uses fictional account labels and states. No balance, bank identifier or private history is published.

## Applying the method elsewhere

Separate fresh source reads from saved snapshots. Keep original records unchanged. Test decimal amounts, missing days, unavailable sources and access restrictions. A service failure must not return a reassuring empty chart.
