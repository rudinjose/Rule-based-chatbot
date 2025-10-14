"""Rule based chatbot.ipynb"""
"""I am testing"""

import pandas as pd
df = pd.read_excel("/content/December.xlsx")

def chatbot():
    print("Welcome to Sales Chatbot! Ask me about sales.")
    print("You can try: 'total sales', 'sales by branch', 'sales of Idli', 'quantity of Phulka'")

    while True:
        query = input("\nYou: ").lower()

        if "exit" in query or "quit" in query:
            print("Chatbot: Goodbye!")
            break

        elif "total sales" in query:
            total = df["sales"].sum()
            print(f"Chatbot: The total sales amount is {total:.2f}")

        elif "sales by branch" in query:
            branch_sales = df.groupby("Branch")["sales"].sum()
            print("Chatbot: Sales by branch:\n", branch_sales)

        elif "sales of" in query:
            item = query.replace("sales of", "").strip().title()
            item_sales = df[df["Item Name"] == item]["sales"].sum()
            if item_sales > 0:
                print(f"Chatbot: Total sales for {item} is {item_sales:.2f}")
            else:
                print(f"Chatbot: Sorry, no sales found for {item}.")

        elif "quantity of" in query:
            item = query.replace("quantity of", "").strip().title()
            qty = df[df["Item Name"] == item]["quantity"].sum()
            if qty > 0:
                print(f"Chatbot: Total quantity sold for {item} is {qty}")
            else:
                print(f"Chatbot: Sorry, no data found for {item}.")

        else:
            print("Chatbot: I don't understand that. Try asking about total sales or an item.")

chatbot()

