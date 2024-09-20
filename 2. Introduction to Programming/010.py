def gbp_to_euro(num_gpb: float) -> float:
    conversion_rate = 1.18 # the current conversion rate from gbp to euro

    num_euros = num_gpb * conversion_rate # converts to euros usng our conversion rate
    rounded_euros = round(num_euros, 2) # rounds the number of euros to be 2 decimal places

    return rounded_euros # returns the gbp to euro conversion after being rounded

if __name__ == "__main__":
    converted_euros = gbp_to_euro(7) # converts gbp to euro using our function

    print(f"Euros: {converted_euros}") # prints the number of euros from gbp to terminal