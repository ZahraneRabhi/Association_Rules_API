import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

def get_frequent_items():
    df_items = pd.read_csv('data/Orders.csv')
    df_items = df_items.groupby('OrderId')['MenuItemName'].apply(list).reset_index()

    te = TransactionEncoder()
    te_array = te.fit(df_items['MenuItemName']).transform(df_items['MenuItemName'])
    df_encoded = pd.DataFrame(te_array, columns=te.columns_)

    frequent_items = apriori(df_encoded, min_support=0.1, use_colnames=True)
    frequent_items = frequent_items.sort_values(by='support', ascending=False).head(5)

    rules = association_rules(frequent_items, metric="lift", min_threshold=1.0)

    items_only = []
    for _, rule in rules.iterrows():
        item_pair = {
            "antecedents": list(rule["antecedents"]),
            "consequents": list(rule["consequents"])
        }
        items_only.append(item_pair)

    return items_only
