def calculate_stock_value(price_per_share, num_shares):
    """
    Calculate the total value of stocks.
    
    Args:
        price_per_share (float): The current price per share of the stock.
        num_shares (int): The number of shares owned.
        
    Returns:
        float: The total value of the stocks.
    """
    return price_per_share * num_shares

def main():
    price_per_share = float(input("Enter the current price per share: "))
    num_shares = int(input("Enter the number of shares owned: "))
    
    total_value = calculate_stock_value(price_per_share, num_shares)
    print("Total value of stocks: $", total_value)

if __name__ == "__main__":
    main()
