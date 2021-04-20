from earth import humans
from earth import sicknesses

for human in range(len(earth.humans)):
    if human.is_sick:
      human.is_sick = False
    if not human.has_antibodies:
      human.has_antibodies = True
      
humans.need_to_mask = False
humans.need_to_quarantine = False

for sickness in sicknesses:
    sickness.active = False
    sickness.has_cure = True
    
