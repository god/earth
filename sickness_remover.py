from earth import humans
from earth import sicknesses

for human in range(len(humans)):
    human.is_sick = False
    human.has_antibodies = True
      
humans.need_to_mask = False
humans.need_to_quarantine = False

for sickness in sicknesses:
    sickness.active = False
    sickness.has_cure = True
    
