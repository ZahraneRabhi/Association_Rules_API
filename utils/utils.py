import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_frequent_items():
    df_items = pd.read_csv('data/Orders.csv')
    df_items = df_items.groupby('OrderId')['MenuItemName'].apply(list).reset_index()

    te = TransactionEncoder()
    te_array = te.fit(df_items['MenuItemName']).transform(df_items['MenuItemName'])
    df_encoded = pd.DataFrame(te_array, columns=te.columns_)

    logging.debug("Raw Data:\n%s", df_items.head())
    logging.debug("Encoded Data:\n%s", df_encoded.head())

    # Lower min_support to capture more frequent itemsets
    frequent_items = apriori(df_encoded, min_support=0.01, use_colnames=True)
    logging.debug("Updated Frequent Items:\n%s", frequent_items)

    # Lower min_threshold for lift to include more rules
    rules = association_rules(frequent_items, metric="lift", min_threshold=0.01)
    logging.debug("Updated Association Rules:\n%s", rules)

    if rules.empty:
        logging.warning("No association rules generated.")
        return {}

    # Sort rules by confidence and take top 5
    rules = rules.sort_values(by="confidence", ascending=False).head(5)

    result_dict = {
        f"Rule {i+1}": {
            "Antecedents": list(rule["antecedents"]),
            "Consequents": list(rule["consequents"]),
            "Confidence": f"{rule['confidence'] * 100:.2f}%"
        }
        for i, (_, rule) in enumerate(rules.iterrows())
    }

    return result_dict