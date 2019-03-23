from game.game.entityclass import entitycollision


class TriggerBox(entitycollision.EntityCollision):

	ARGS_COUNTER = 3

	def __init__(self, entity, args):
		super().__init__(args)
		self.maxCount = args[TriggerBox.ARGS_COUNTER]
		self.count = 0
		self.entity = entity
		self.entityId = -1

		self.setDrawCol(True)
		self.colRenderer.setAttributes(self.colSize, [0, 0, 1, 0.5])

		self.giveDamage = True

	def update(self):
		super().update()
		if self.count >= self.maxCount:
			print("self.id", self.id)
			self.em.remove(self.id, False)

		self.count +=1

	def setEntityId(self, entityId):
		self.entityId = entityId

	def triggerBox(self, ent):
		self.entity.triggerBox(ent)
