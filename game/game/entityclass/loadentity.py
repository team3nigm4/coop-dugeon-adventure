class LoadEntity:
	from game.game.entitymodel import activationblock
	from game.game.entitymodel import activationplate
	from game.game.entitymodel import arrow
	from game.game.entitymodel import bat
	from game.game.entitymodel import bridge
	from game.game.entitymodel import door
	from game.game.entitymodel import itemrecoverable
	from game.game.entitymodel import lockeddoor
	from game.game.entitymodel import mannequin
	from game.game.entitymodel import player
	from game.game.entitymodel import pressureplate
	from game.game.entitymodel import slidingblock
	from game.game.entitymodel import spawn
	from game.game.entitymodel import spider
	from game.game.entitymodel import toggleplate

	entities = {
		"ActivationBlock": activationblock.ActivationBlock,
		"ActivationPlate": activationplate.ActivationPlate,
		"Arrow": arrow.Arrow,
		"Bat": bat.Bat,
		"Bridge": bridge.Bridge,
		"Door": door.Door,
		"ItemRecoverable": itemrecoverable.ItemRecoverable,
		"LockedDoor": lockeddoor.LockedDoor,
		"Mannequin": mannequin.Mannequin,
		"Player": player.Player,
		"PressurePlate": pressureplate.PressurePlate,
		"SlidingBlock": slidingblock.SlidingBlock,
		"Spawn": spawn.Spawn,
		"Spider": spider.Spider,
		"TogglePlate": toggleplate.TogglePlate
	}

	# reset = 0, no reset = 1
	LIST_RESET = {
		"ActivationBlock": 0,
		"ActivationPlate": 0,
		"Arrow": 0,
		"Bat": 0,
		"Bridge": 0,
		"Door": 0,
		"ItemRecoverable": 1,
		"LockedDoor": 1,
		"Mannequin": 0,
		"Player": 1,
		"PressurePlate": 0,
		"SlidingBlock": 0,
		"Spawn": 0,
		"Spider": 0,
		"TogglePlate": 0
	}

	TO_RESET = 0
	NO_RESET = 1

	reset = False

	@staticmethod
	def setReset(state):
		LoadEntity.reset = state

	@staticmethod
	def instance(args):
		if args[0] in LoadEntity.entities:
			if LoadEntity.reset:
				if LoadEntity.LIST_RESET[args[0]] == LoadEntity.NO_RESET:
					return False
				else:
					return LoadEntity.entities[args[0]](args)
			else:
				return LoadEntity.entities[args[0]](args)
		else:
			return False
