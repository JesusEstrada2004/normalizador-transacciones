# Normalización y Exploración de Transacciones Multifuente

## Descripción

Este proyecto normaliza transacciones provenientes de múltiples fuentes con estructuras distintas y permite explorarlas mediante una interfaz CLI interactiva.

## Modelo normalizado

Cada transacción válida se convierte al siguiente formato:

```json
{
  "id": "string",
  "amount": 99.99,
  "currency": "USD",
  "timestamp": "ISO-8601",
  "status": "SUCCESS | FAILED | PENDING",
  "source": "string"
}