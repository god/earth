from earth import humans
from earth import sicknesses

for human in range(len(earth.humans)):
    if human.is_sick:
      human.is_sick = False
    if not human.has_antibodies:
      human.has_antibodies = True
      
earth.humans.need_to_mask = False
earth.humans.need_to_quarantine = False

for sickness in earth.sicknesses:
    sickness.active = False
    sickness.has_cure = True
    
