from ants import *
beehive, layout = Hive(AssaultPlan()), dry_layout
gamestate = GameState(None, beehive, ant_types(), layout, (1, 9))     

bodyguard = BodyguardAnt()
first_ant = ThrowerAnt()
place = gamestate.places['tunnel_0_0']
place.add_insect(bodyguard)
place.add_insect(first_ant)
second_ant = ThrowerAnt()
place.add_insect(second_ant)