# This class performs the display and the update of the client

import time

from game.game.entitymodel import player as pl
from game.game.entityclass.entitymanager import EntityManager as em
from game.game.map.mapmanager import MapManager as mam
from game.inputs.inputmanager import InputManager as im
from game.screen.gamemanager import GameManager as gm
from game.screen.screens import screen
from game.game.gameplay.hud import Hud
from game.render.text import text


class GameScreen(screen.Screen):

	def __init__(self):
		super(GameScreen, self).__init__()

	def init(self):
		em.init()

		player1 = pl.Player(["Player", em.PLAYER_1, [0, 0], 0, "players/player1.png"])
		em.addWithId(player1)
		player2 = pl.Player(["Player", em.PLAYER_2, [0, 0], 1, "players/player2.png"])
		em.addWithId(player2)

		mam.init()
		Hud.init()

		from game.inputs import playercontroler as plc
		self.controlPlay1 = plc.PlayerController()
		self.controlPlay1.setPlayer(em.PLAYER_1)
		self.controlPlay1.setEntity(em.entities[em.PLAYER_1])

		self.controlPlay2 = plc.PlayerController()
		self.controlPlay2.setPlayer(em.PLAYER_2)
		self.controlPlay2.setEntity(em.entities[em.PLAYER_2])

		gm.cam.trackEntity(em.PLAYER_1)

		self.text = text.Text("test")
		self.text.setSize(0.4)
		self.text.setColor([0.4,0.1,0.8,1])
		self.text.setPosition([18, 0])
		self.text.setCentering("down-right")
		self.text.setText("Test Enaéled\nTest concluded by a success\nText enter in the BATTLE !")

		self.inPause = False

	def update(self):
		# Receive and create data
		serverData = gm.serverData
		clientData = im.getState()

		if not self.inPause:
			# Update
			self.controlPlay1.update()
			self.controlPlay2.update()
			em.update()

			# Keys test
			if im.inputPressed(im.ESCAPE):
				from game.main.window import Window
				Window.exit()

			if im.inputPressed(im.RESET):
				mam.reserveChange(mam.zone, mam.id, mam.defaultEntry)

			if im.inputPressed(im.ITEM2_0):
				gm.cam.trackEntity(1 - gm.cam.entityId)

			if im.keyBoardManager.getKey(290):
				from game.game.command import Command
				Command.command(input('\n[COMMAND] $ '))

			# Dispose components
			gm.cam.goToEntity()
			em.dispose()
			Hud.dispose()

		mam.update()

		# Return data
		clientData.append(time.time_ns())
		gm.clientData = clientData

	def display(self):
		mam.display()
		Hud.display()
		self.text.display()

	def unload(self):
		mam.unload()
		Hud.unload()
		em.entities[em.PLAYER_1].unload()
		em.entities[em.PLAYER_2].unload()
		self.text.unload()
