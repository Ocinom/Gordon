from Question import qn, start

light_on = qn('Is the light on?')
electricity_off = qn('Is the electricity turned off?')
brown_globe = qn('Has the light globe blown?')
fuse_blown = qn('Has the fuse blown?')

fuse_blown.add_query('Call an electrician.', 'Replace the fuse.')
brown_globe.add_query(fuse_blown, 'Replace the light globe.')
electricity_off.add_query(brown_globe, 'Turn on the electricity at the switch.')
light_on.add_query(electricity_off, 'Good, all is OK.')

start(light_on)
