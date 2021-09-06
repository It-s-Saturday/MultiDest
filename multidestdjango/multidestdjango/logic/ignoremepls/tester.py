cost = 1513
if cost > 1440:
    days_cost = cost // (24 * 60)
    hours_cost = (cost // 60) % 24
    mins_cost = cost % 24 % 60
    if days_cost == 1:
        out_day = "day"
    else:
        out_day = "days"
    if hours_cost == 1:
        out_hour = "hour"
    else:
        out_hour = "hours"
    if mins_cost == 1:
        out_min = "min"
    else:
        out_min = "mins"
    print(str(days_cost) + " {}, ".format(out_day) + str(hours_cost) + " {}, and ".format(out_hour) + str(
        mins_cost) + " {}".format(out_min))
elif cost >= 60 and cost < 1440:
    hours_cost = cost // 60
    mins_cost = cost % 60
    if hours_cost == 1:
        out_hour = "hour"
    else:
        out_hour = "hours"
    if mins_cost == 1:
        out_min = "min"
    else:
        out_min = "mins"

    print(str(hours_cost) + " {} and ".format(out_hour) + str(mins_cost) + " {}".format(out_min))

else:
    print(str(cost) + " mins")