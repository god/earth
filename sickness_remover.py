from earth import humans
from earth import sicknesses

for human in humans:
    human.is_sick = False
    human.has_antibodies = True
    if human.is_karen or human.is_anti_vaxxer or human.is_anti_masker:
        humans.pop(humans.index(human))

for sickness in sicknesses:
    sickness.active = False
    sickness.has_cure = True


humans.need_to_mask = True
humans.need_to_get_vaccinated = True
humans.need_to_quarantine = False
