def future_value(pv, rate, periods):
    """
    Future value as a function of period.
    pv: present value.
    rate: interest rate.
    periods: time in years.
    """
    fv = pv*(1+rate)**periods
    return fv

def present_value(fv, rate, periods):
    """
    Present value as a function of period.
    fv: future value.
    rate: interest rate.
    periods: time in years.
    """
    pv = fv/(1+rate)**periods
    return pv

def real_return(rate, inflation):
    """
    Real return considering inflation.
    rate: interest rate.
    inflation: inflation.
    """
    r_real = (1 + rate)/(1 + inflation) - 1
    return r_real
