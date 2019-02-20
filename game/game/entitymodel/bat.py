# Entity class player, embodies one of the players

from game.game.entityclass import entitycomplex
from game.util import math as mathcda

import math


class Bat(entitycomplex.EntityComplex):
	SPEED_ADD = 0.003
	SPEED_MAX = 0.03
	SPEED_DECREASE = 0.003

	DETECTION_RANGE = 4

	INVINCIBILITY_TIME = 60

	def __init__(self, args):
		super().__init__(args)
		self.setColBox([0.9, 0.9], True)

		self.attributes["enemyDamage"] = 1

		self.direction = 3
		self.damage = 1
		self.maxSpeed = Bat.SPEED_MAX

		self.entityRenderer.setImagePath([1, 1], "entities/bat.png", [0.5, 0.5])

		self.wantDirection = [0, 0]
		self.invincibilityTime = Bat.INVINCIBILITY_TIME

		self.target = None

	def left(self, input):
		if input > 1:
			self.wantDirection[0] -= 1

	def up(self, input):
		if input > 1:
			self.wantDirection[1] += 1

	def right(self, input):
		if input > 1:
			self.wantDirection[0] += 1

	def down(self, input):
		if input > 1:
			self.wantDirection[1] -= 1

	def update(self):
		super().update()

		if self.target == None:
			if mathcda.distE(self, self.em.entities[0]) < Bat.DETECTION_RANGE:
				self.target = 0
			elif mathcda.distE(self, self.em.entities[1]) < Bat.DETECTION_RANGE:
				self.target = 1

		else:
			target = self.em.entities[self.target]
			if self.em.entities[self.target].id == -1:
				self.target = None
			else:
				if mathcda.distEx(self, target) > self.maxSpeed:
					if self.pos[0] > target.pos[0]:
						self.left(2)
					else:
						self.right(2)

				if mathcda.distEy(self, target) > self.maxSpeed:
					if self.pos[1] > target.pos[1]:
						self.down(2)
					else:
						self.up(2)

		for i in range(2):
			if self.wantDirection[i] == 0:
				if self.speed[i] < 0:
					self.speed[i] += Bat.SPEED_DECREASE
					if self.speed[i] > 0:
						self.speed[i] = 0
						self.inMov[i] = False
				else:
					self.speed[i] -= Bat.SPEED_DECREASE
					if self.speed[i] < 0:
						self.speed[i] = 0
						self.inMov[i] = False
			else:
				self.inMov[i] = True
				self.speed[i] += self.wantDirection[i] * Bat.SPEED_ADD
				if math.fabs(self.speed[i]) > self.maxSpeed:
					self.speed[i] = self.wantDirection[i] * self.maxSpeed

		self.setPos([self.pos[0] + self.speed[0], self.pos[1] + self.speed[1]])

		self.wantDirection = [0, 0]

	def collision(self, ent):
		if ent.attributes["playerSword"] == 1 or ent.attributes["playerBow"] == 1:
			ent.triggerBox(self)

		super().collision(ent)
