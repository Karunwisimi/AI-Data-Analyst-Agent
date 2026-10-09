
from data_loader import load_transaction_chunks


def get_customer_count():
    customers = set()

    for chunk in load_transaction_chunks():
        customers.update(
            chunk["PERSON_PUBLIC_KEY"].dropna().unique()
        )

    return len(customers)


def get_top_categories(n=10):
    category_counts = {}

    for chunk in load_transaction_chunks():
        counts = chunk["PRODUCT_CATEGORY"].value_counts()

        for category, count in counts.items():
            category_counts[category] = (
                category_counts.get(category, 0) + int(count)
            )

    return dict(
        sorted(
            category_counts.items(),
            key=lambda item: item[1],
            reverse=True
        )[:n]
    )


def get_channel_count(channel):
    channel = channel.upper()
    total = 0

    for chunk in load_transaction_chunks():
        total += int((chunk["CHANNEL"] == channel).sum())

    return total