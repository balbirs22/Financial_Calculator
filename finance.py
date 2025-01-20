import numpy as np

def future_value(principal, rate, periods):
    """Calculate the future value of an investment."""
    return principal * (1 + rate) ** periods

def present_value(future_val, rate, periods):
    """Calculate the present value of a future sum."""
    return future_val / (1 + rate) ** periods

def compound_interest(principal, rate, compounding, periods):
    """Calculate the compound interest over a period."""
    return principal * (1 + rate / compounding) ** (compounding * periods)

def simple_interest(principal, rate, time):
    """Calculate simple interest."""
    return principal * rate * time

def loan_amortization(principal, rate, periods):
    """Generate an amortization schedule for a fixed rate loan."""
    monthly_interest = rate / 12
    monthly_payment = principal * (monthly_interest * (1 + monthly_interest) ** periods) / ((1 + monthly_interest) ** periods - 1)
    schedule = []
    balance = principal
    for i in range(1, periods + 1):
        interest = balance * monthly_interest
        principal_payment = monthly_payment - interest
        balance -= principal_payment
        schedule.append((i, monthly_payment, principal_payment, interest, balance))
    return schedule

def net_present_value(rate, cashflows):
    """Calculate the net present value of a series of cashflows."""
    return sum(cf / (1 + rate) ** i for i, cf in enumerate(cashflows))

def breakeven_point(fixed_costs, price_per_unit, variable_cost_per_unit):
    """Calculate the breakeven point in units and sales value."""
    units = fixed_costs / (price_per_unit - variable_cost_per_unit)
    sales_value = units * price_per_unit
    return units, sales_value

def capm(risk_free_rate, beta, market_return):
    """Calculate expected return of an asset based on CAPM model."""
    return risk_free_rate + beta * (market_return - risk_free_rate)
