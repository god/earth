from earth import humans
from earth.statistics.humans import min_iq

for human in humans:
  if human['iq'] < min_iq:
    del human
