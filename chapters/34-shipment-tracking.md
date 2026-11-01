# Shipment tracking

A customer asks where an order is. The agent needs the right parcel history, not a guess based on the order date.

## What connects

The support conversation links to an exact commerce order. That order identifies the warehouse shipment and its carrier events. Each event keeps its time, parcel and direction: outbound delivery and a return are different journeys.

## What the agent does

It reads the available events, checks the latest observation and prepares an explanation for the support team. Missing events stay missing. An empty response does not prove that the parcel has not moved; a tracking event does not authorise a refund.

Reads have a time limit, a retry limit and a cooldown when the provider asks the client to slow down. Cached evidence retains its timestamp.

## What comes out

A dated parcel history beside the draft reply. A person reviews the explanation and decides whether to contact the carrier or customer.

## What we checked

The deployed connection returned real outbound events from multiple carriers. An empty carrier response was kept distinct from a delivery status. Return-direction handling was tested with fictional records, not independently confirmed with a real return journey. Coverage is not universal.

[Try the fictional example](https://usecompai.com/live.html?example=shipment-tracking#try). See how it fits into the [customer care workspace](04-agent-cs.md).
