from game.game.map import loadentity
from game.game.entityclass import entity

class Spawn(entity.Entity):

	ARGS_EVENT = 1
	ARGS_ENTITY_INFO = 2

	def __init__(self, args):
		super().__init__([args[0], [0, 0]])

		self.event = args[Spawn.ARGS_EVENT]

		self.entityInfo = args[Spawn.ARGS_ENTITY_INFO]
		self.hasSpawn = False

	def activate(self):
		if not self.hasSpawn:
			from game.game.map.eventmanager import EventManager as ev
			self.em.remove(self.id)
			self.em.add(loadentity.LoadEntity.instance(self.entityInfo))
			ev.removeActive(self.event, self.id)
			self.hasSpawn = True

	def setId(self, id):
		super().setId(id)
		from game.game.map.eventmanager import EventManager
		EventManager.addActive(self.event, self.id)

	def deactivate(self):
		pass