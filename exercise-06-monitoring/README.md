# Exercise 6: Real-Time Operations Monitoring

## Goal

Simulate delivery metrics, scrape them with Prometheus, display them in Grafana, and define an alert rule.

## Work

The app, Dockerfile, Compose stack, Prometheus configuration, alert rule, Grafana datasource, and provisioned dashboard are included here. The Grafana password is supplied through a local ignored `.env` file rather than committed.

## Verification

The Compose stack started successfully with the exporter, Prometheus, and Grafana containers healthy. Prometheus reported the `delivery-metrics` target as `up`, and its `pending_deliveries` query returned live samples. Grafana's API confirmed the provisioned Prometheus datasource and the `Quick Commerce Delivery Operations` dashboard.

To verify alert behavior, I temporarily held the simulated pending-delivery value above 15, observed `PendingDeliveriesHigh` transition from pending to firing, then restored the original random simulation and rebuilt the exporter. No forced metric value remains in the submitted source. Rule evaluation runs every 5 seconds with a 10-second firing duration.

The dashboard is available locally at `http://127.0.0.1:3000` while the stack is running. The Prometheus UI is at `http://127.0.0.1:9090`.
