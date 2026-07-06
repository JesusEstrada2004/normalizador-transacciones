from src.loader import load_json_file, load_rules
from src.normalizer import normalize_transaction
from src.validator import process_transactions
from src.metrics import calculate_metrics
from src.cli import run_cli


def main():
    transactions_file = "data/transactions.json"
    rules_file = "config/rules.json"

    raw_transactions = load_json_file(transactions_file)
    rules = load_rules(rules_file)

    valid_transactions, invalid_transactions = process_transactions(
        raw_transactions,
        rules,
        normalize_transaction
    )

    metrics = calculate_metrics(valid_transactions, invalid_transactions)

    run_cli(valid_transactions, invalid_transactions, metrics)


if __name__ == "__main__":
    main()