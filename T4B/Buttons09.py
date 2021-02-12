from Question import qn, start

view_months = qn('View months?')
view_weekend = qn('View Weekend?')
view_all_months = qn('View all months?')
view_long_months = qn("View long months?")

view_long_months.add_query('Show 30 day months', 'Show 31 day months')
view_all_months.add_query(view_long_months, 'Show all months')
view_weekend.add_query('Show weekdays', 'Show Week end days')
view_months.add_query(view_weekend, view_all_months)

start(view_months)