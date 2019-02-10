# This class performs the display and the update of the client

import time

from game.game.entitymodel import player as pl
from game.game.entityclass.entitymanager import EntityManager as em
from game.game.map.mapmanager import MapManager as mam
from game.inputs.inputmanager import InputManager as im
from game.screen.gamemanager import GameManager as gm
from game.screen.screens import screen


class GameScreen(screen.Screen):

	def __init__(self):
		super(GameScreen, self).__init__()

		em.init()

		player = pl.Player(["Player", [0, 0], [0.90, 1.2], "perso.png"])
		em.add(player)

		mam.init()

		from game.inputs import playercontroler as plc
		self.controlPlay1 = plc.PlayerController()
		self.controlPlay1.setPlayer(0)
		self.controlPlay1.setEntity(em.entities[0])

	def update(self):
		# Receive and create data
		serverData = gm.serverData
		clientData = im.getState()

		self.controlPlay1.update()
		em.update()
		em.collision()

		if im.inputPressed(im.ESCAPE):
			from game.main.window import Window
			Window.exit()

		if im.inputPressed(im.RESET):
			mam.reserveChange([mam.zone, mam.id, mam.defaultEntry])

		if im.keyBoardManager.getKey(290):
			self.controlPlay1.setEntity(em.entities[2])
			gm.cam.trackEntity(2)

		mam.checkChangeMap()

		gm.cam.goToEntity()
		em.dispose()

		# Return data
		clientData.append(time.time_ns())
		gm.clientData = clientData

	def display(self):
		mam.display()
		em.display()

	def unload(self):
		mam.unload()
		em.unload()
