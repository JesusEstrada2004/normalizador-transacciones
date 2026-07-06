from datetime import datetime


def detect_source(transaction):
    if "id" in transaction and "timestamp" in transaction:
        return "source_a"

    if "transaction_id" in transaction and "created_at" in transaction:
        return "source_b"

    if "ref" in transaction and "date" in transaction:
        return "source_c"

    return "unknown"


def normalize_amount(value):
    if value is None or value == "":
        raise ValueError("Monto vacío o inexistente")

    if isinstance(value, int) or isinstance(value, float):
        return float(value)

    value = str(value).strip()
    value = value.replace("€", "")
    value = value.replace("$", "")
    value = value.replace(",", ".")

    return float(value)


def normalize_currency(value):
    if value is None or value == "":
        raise ValueError("Moneda vacía o inexistente")

    return str(value).upper().strip()


def normalize_date(value, date_formats):
    if value is None or value == "":
        raise ValueError("Fecha vacía o inexistente")

    for date_format in date_formats:
        try:
            parsed_date = datetime.strptime(value, date_format)
            return parsed_date.isoformat()
        except ValueError:
            continue

    raise ValueError(f"Formato de fecha no soportado: {value}")


def normalize_status(value, status_mapping):
    if value is None or value == "":
        raise ValueError("Estado vacío o inexistente")

    if value in status_mapping:
        return status_mapping[value]

    value_lower = str(value).lower()

    if value_lower in status_mapping:
        return status_mapping[value_lower]

    raise ValueError(f"Estado no reconocido: {value}")


def normalize_transaction(transaction, rules):
    source = detect_source(transaction)

    if source == "source_a":
        normalized = {
            "id": str(transaction.get("id")),
            "amount": normalize_amount(transaction.get("amount")),
            "currency": normalize_currency(transaction.get("currency")),
            "timestamp": normalize_date(
                transaction.get("timestamp"),
                rules["date_formats"]
            ),
            "status": normalize_status(
                transaction.get("status"),
                rules["status_mapping"]
            ),
            "source": source
        }

    elif source == "source_b":
        normalized = {
            "id": str(transaction.get("transaction_id")),
            "amount": normalize_amount(transaction.get("total")),
            "currency": normalize_currency(transaction.get("currency_code")),
            "timestamp": normalize_date(
                transaction.get("created_at"),
                rules["date_formats"]
            ),
            "status": normalize_status(
                transaction.get("state"),
                rules["status_mapping"]
            ),
            "source": source
        }

    elif source == "source_c":
        normalized = {
            "id": str(transaction.get("ref")),
            "amount": normalize_amount(transaction.get("amount")),
            "currency": normalize_currency("EUR"),
            "timestamp": normalize_date(
                transaction.get("date"),
                rules["date_formats"]
            ),
            "status": normalize_status(
                transaction.get("result"),
                rules["status_mapping"]
            ),
            "source": source
        }

    else:
        raise ValueError("Fuente de transacción no reconocida")

    return normalized