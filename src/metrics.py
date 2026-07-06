def calculate_metrics(valid_transactions, invalid_transactions):
    metrics = {
        "total_processed": len(valid_transactions) + len(invalid_transactions),
        "valid_count": len(valid_transactions),
        "invalid_count": len(invalid_transactions),
        "count_by_status": {},
        "totals_by_currency": {}
    }

    for transaction in valid_transactions:
        status = transaction["status"]
        currency = transaction["currency"]
        amount = transaction["amount"]

        if status not in metrics["count_by_status"]:
            metrics["count_by_status"][status] = 0

        metrics["count_by_status"][status] += 1

        if currency not in metrics["totals_by_currency"]:
            metrics["totals_by_currency"][currency] = 0

        metrics["totals_by_currency"][currency] += amount

    return metrics