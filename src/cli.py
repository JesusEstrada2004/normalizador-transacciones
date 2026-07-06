def show_menu():
    print("\n===== Sistema de Normalización de Transacciones =====")
    print("1. Ver todas las transacciones válidas")
    print("2. Ver transacciones inválidas")
    print("3. Ver métricas generales")
    print("4. Filtrar por estado")
    print("5. Filtrar por moneda")
    print("6. Salir")


def print_transaction(transaction):
    print("-" * 60)
    print(f"ID: {transaction['id']}")
    print(f"Monto: {transaction['amount']}")
    print(f"Moneda: {transaction['currency']}")
    print(f"Fecha: {transaction['timestamp']}")
    print(f"Estado: {transaction['status']}")
    print(f"Fuente: {transaction['source']}")


def run_cli(valid_transactions, invalid_transactions, metrics):
    while True:
        show_menu()
        option = input("Selecciona una opción: ")

        if option == "1":
            print("\nTransacciones válidas:")
            for transaction in valid_transactions:
                print_transaction(transaction)

        elif option == "2":
            print("\nTransacciones inválidas:")
            for item in invalid_transactions:
                print("-" * 60)
                print(f"Registro original: {item['original']}")
                print(f"Razón: {item['reason']}")

        elif option == "3":
            print("\nMétricas generales:")
            print(f"Total procesadas: {metrics['total_processed']}")
            print(f"Válidas: {metrics['valid_count']}")
            print(f"Inválidas: {metrics['invalid_count']}")

            print("\nConteo por estado:")
            for status, count in metrics["count_by_status"].items():
                print(f"{status}: {count}")

            print("\nTotales por moneda:")
            for currency, total in metrics["totals_by_currency"].items():
                print(f"{currency}: {round(total, 2)}")

        elif option == "4":
            status_filter = input("Estado a filtrar SUCCESS/FAILED/PENDING: ").upper()

            results = [
                transaction for transaction in valid_transactions
                if transaction["status"] == status_filter
            ]

            print(f"\nResultados para estado {status_filter}:")
            for transaction in results:
                print_transaction(transaction)

            if not results:
                print("No se encontraron transacciones con ese estado.")

        elif option == "5":
            currency_filter = input("Moneda a filtrar USD/EUR: ").upper()

            results = [
                transaction for transaction in valid_transactions
                if transaction["currency"] == currency_filter
            ]

            print(f"\nResultados para moneda {currency_filter}:")
            for transaction in results:
                print_transaction(transaction)

            if not results:
                print("No se encontraron transacciones con esa moneda.")

        elif option == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")