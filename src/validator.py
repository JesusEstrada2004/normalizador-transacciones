def validate_transaction(transaction, supported_currencies):
    required_fields = ["id", "amount", "currency", "timestamp", "status", "source"]

    for field in required_fields:
        if field not in transaction:
            return False, f"Falta el campo obligatorio: {field}"

        if transaction[field] is None or transaction[field] == "":
            return False, f"Campo vacío: {field}"

    if transaction["amount"] <= 0:
        return False, "El monto debe ser mayor que cero"

    if transaction["currency"] not in supported_currencies:
        return False, f"Moneda no soportada: {transaction['currency']}"

    if transaction["status"] not in ["SUCCESS", "FAILED", "PENDING"]:
        return False, f"Estado no válido: {transaction['status']}"

    return True, "Transacción válida"


def process_transactions(raw_transactions, rules, normalizer_function):
    valid_transactions = []
    invalid_transactions = []

    for transaction in raw_transactions:
        try:
            normalized_transaction = normalizer_function(transaction, rules)
            is_valid, message = validate_transaction(
                normalized_transaction,
                rules["supported_currencies"]
            )

            if is_valid:
                valid_transactions.append(normalized_transaction)
            else:
                invalid_transactions.append({
                    "original": transaction,
                    "reason": message
                })

        except Exception as error:
            invalid_transactions.append({
                "original": transaction,
                "reason": str(error)
            })

    return valid_transactions, invalid_transactions