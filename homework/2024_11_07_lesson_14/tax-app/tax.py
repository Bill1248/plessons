def calculateTax(amount, percent, assignment_amount):
    """Calculates the tax of amount.

    Args:
        amount: The sum
        percent: The tax percent
        assignment_amount: Assignment of ammount

    Returns:
        List of amount, percent, assignment_amount, tax

    """
    tax = amount * percent / 100.0
    return[amount, percent, assignment_amount, tax]

