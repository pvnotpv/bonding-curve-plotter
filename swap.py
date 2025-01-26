def get_swap_y_in_x_out(curve, amount1_in, liq, sqrtpC):
    price_diff = amount1_in/liq
    price_next = sqrtpC+price_diff 

    x_new = curve.calc_xReal(liq, sqrtpC, price_next)
    y_new = curve.calc_yReal(liq, sqrtpC, price_next)

    changeX = ((1/price_next)-(1/sqrtpC))*liq

    return x_new, y_new, price_next, price_diff



def get_swap_x_in_y_out(curve, amount0_in, liq, sqrtpC):
    price_next = (liq*sqrtpC)/(amount0_in*sqrtpC+liq)

    x_new = curve.calc_xReal(liq, price_next, sqrtpC)
    y_new = curve.calc_yReal(liq, price_next, sqrtpC)

    return x_new, y_new, price_next


def swap(curve, buySell, amount):
    if (buySell):
        (x_new, y_new, price_next, price_diff) = get_swap_y_in_x_out(curve, amount, curve.liq, curve.sqrtpC)
        curve.update_y_in_x_out(x_new, y_new, price_next)
        return (x_new, y_new, price_next, price_diff) 
    else:
        (x_new, y_new, price_next) = get_swap_x_in_y_out(curve, amount, curve.liq, curve.sqrtpC)
        curve.update_x_in_y_out(x_new, y_new, price_next)
        return (x_new, y_new, price_next)



