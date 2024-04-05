def centsPriceFormatter(cents):
    dollars = cents // 100
    cents = cents % 100
    return f"${dollars}.{cents}"

formatters = {
    "formatCents": centsPriceFormatter
}    
