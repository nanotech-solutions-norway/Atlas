# ADR-0001 — Atlas Three-Plane Architecture — 12:45, 01.06.2026

## Status
Accepted.

## Decision
Atlas uses three platform planes: public presentation, GitHub engineering governance, and future Azure secure execution/control.

## Boundary
This repo may publish public static information and govern implementation artifacts. It must not store backend secrets, customer-sensitive data, entitlement data, or confidential deliverables.

## Rationale
The architecture reduces drift, supports rollback, keeps launch delivery simple, and preserves a future path toward Managed Secure Mode.
