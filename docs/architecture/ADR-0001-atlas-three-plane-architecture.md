# ADR-0001 — Atlas AI Three-Plane Architecture — 13:02, 04.06.2026

## Status
Accepted; updated by June 2026 website strategy.

## Decision
Atlas AI keeps the three-plane architecture: public/commercial plane, GitHub governance plane, and secure control plane.

## Boundary
The public site must not process secrets, credentials, protected customer artifacts, or confidential/restricted uploads. Ordinary forms are low-risk qualification only. Azure-backed secure orchestration is reserved for qualified Managed Secure / controlled-delivery use cases.
