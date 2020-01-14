#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

import sys, signal, os
import bitcoinlib # https://bitcoinlib.readthedocs.io/en/latest/index.html#
try:
	import qrcode # https://github.com/lincolnloop/python-qrcode
except ModuleNotFoundError as err:
	QRCODE_LIB_PRESENT = False
	print("\nYou haven\'t qrcode module. You will not able to generate any qrcode image. Pause [ENTER].")
	input()
else:
	QRCODE_LIB_PRESENT = True

VERSION = float(0.1)
BTCLIB_DB_PATH = str('')
HOME_DIR = str('')
SCREENBAR = str('')
MSGBAR = str('')
TRM_LINES=int()
TRM_COLS=int()

widReg = []

def getTerminalSize(sig, frame):
	global TRM_COLS
	global TRM_LINES

	TRM_COLS, TRM_LINES = os.get_terminal_size()

def clearscreen():
	if os.name == 'posix':
		os.system('clear')
	elif os.name == 'nt':
		os.system('cls')
	else:
		print('\n\n\n\n\n')

def exec_menu(opts):
	totOpts = len(opts)

	while True:
		printScreenHeader()

		[print(i) for i in opts]

		print('\n')

		try:
			x = int(input('Option: '))
		except:
			continue

		if x < totOpts:
			return x - 1

def setStatusMsgBars(scr, msg):
	global SCREENBAR
	global MSGBAR

	SCREENBAR = scr
	MSGBAR = msg

def printScreenHeader(scrBar = '', msgBar = ''):
	global VERSION
	global BTCLIB_DB_PATH
	global SCREENBAR
	global MSGBAR
	global TRM_COLS
	global TRM_LINES

	if scrBar != '':
		SCREENBAR = scrBar

	if msgBar != '':
		MSGBAR = msgBar

	clearscreen()
	print('As Wallet'.center(TRM_COLS))
	print('========='.center(TRM_COLS))
	print('-' * TRM_COLS)
	print(f'(Version: \'{VERSION}\' BitcoinLib DB path: \'{BTCLIB_DB_PATH}\')\n')
	print(f'* {SCREENBAR} *'.center(TRM_COLS))
	print(f'Status: {MSGBAR}\n')
	print('-' * TRM_COLS)

def screen_SelPthBTCLib():
# bitcoinlib.db.DbInit(databasefile='/home/docs/.bitcoinlib/database/bitcoinlib.sqlite')[source]
	screenTitle = 'Set bitcoinlib DB path'
	newPath = str('')
	global BTCLIB_DB_PATH

	while True:
		printScreenHeader(scrBar = screenTitle)

		try:
			newPath = input('New SQLite bitcoinlib DB path (blank to go back): ')
		except:
			return screen_ERROR('select new bitcoinlib DB path  input() throw exception')

		if newPath == '':
			return screen_Main

		if os.path.isfile(newPath) == False:
			print('Invalid file path! Pause [ENTER]')
			input()
		else:
			break

	BTCLIB_DB_PATH = newPath

	return screen_Main

def screen_ERROR(errStr):
	print('Erro: ' + errStr)
	sys.exit(1)


def screen_CreaBTCWltt():
	screenTitle = 'Create BTC Wallet Menu'
	wlttype  = str('')
	wltnet   = str('')
	wltname  = str('')

	printScreenHeader(scrBar = screenTitle)

	try:
		wltname = input('Wallet name (blank to go back): ')
	except:
		return screen_ERROR('wallet name input() throw exception')

	if wltname == '':
		return screen_CreaWltt

	setStatusMsgBars(screenTitle, 'Name [' + wltname + ']')

	menu = ["1 - Legacy",
	        "2 - Segwit",
	        "3 - P2sh-segwit",
	        "4 - Back",
	        "0 - Exit"]

	opt = exec_menu(menu)

	if opt == -1:
		sys.exit(0)
	elif opt == 3:
		return screen_CreaWltt
	elif opt == 0:
		wlttype = 'legacy'
	elif opt == 1:
		wlttype = 'segwit'
	elif opt == 2:
		wlttype = 'p2sh-segwit'

	setStatusMsgBars(screenTitle, 'Name [' + wltname + '] Type [' + wlttype + ']')

	menu = ["1 - BTC Main net",
	        "2 - Litecoin",
	        "3 - BTC Test net",
	        "4 - Back",
	        "0 - Exit"]

	opt = exec_menu(menu)

	if opt == -1:
		sys.exit(0)
	elif opt == 2:
		return screen_CreaWltt
	elif opt == 0:
		wltnet = 'bitcoin'
	elif opt == 1:
		wltnet = 'testnet'
	elif opt == 2:
		wltnet = 'litecoin'

	setStatusMsgBars(screenTitle, 'Name [' + wltname + '] Type [' + wlttype + ']' + ' Net [' + wltnet + ']')
	sys.exit(0)

def screen_CreaLTCWltt():
	print('Not implemented')
	sys.exit(0)

def screen_CreaWltt():
	menu = {
		'titles':[
			"1 - Create a bitcoin wallet",
			"2 - Create a litecoin wallet",
			"3 - Back",
			"0 - Exit"
		],
		'funcs':[
			screen_CreaBTCWltt,
			screen_CreaLTCWltt,
			screen_Wallet,
			screen_Exit
		]
	}

	setStatusMsgBars('Create Wallet Menu', '')

	return menu['funcs'][exec_menu(menu['titles'])]

def screen_DelWltt():
	print('Not implemented')
	sys.exit(0)

def screen_OperWltt():
#  accounts(network='bitcoin')[source]
#  addresslist(account_id=None, used=None, network=None, change=None, depth=None, key_id=None)[source]

# {'id': 1, 'name': 'Wallet1', 'owner': '', 'network': 'bitcoin', 'purpose': 44, 'scheme': 'bip32', 'main_key_id': 1, 'parent_id': None}

	global widReg
	wid = 0

	printScreenHeader(scrBar = 'Operate a Wallet', msgBar = '')

	acc = bitcoinlib.wallets.wallets_list(BTCLIB_DB_PATH)
#	[print(i) for i in acc]

	[print('Id.....: [' + str(i['id']) + ']\nName...: [' + i['name'] + ']\nOwner..: [' + i['owner'] +
	       ']\nNetwork: [' + i['network'] + ']\nInfo...: [' + str(i['purpose']) + '/' + i['scheme'] + ']\n') for i in acc]

	while wid == 0:
		try:
			wid = int(input('Wallet id (blank to go back): '))
		except:
			if wid == 0:
				return screen_Wallet

			continue

		try:
			widReg = [k for k in acc if k['id'] == wid][0]
		except IndexError:
			wid = 0
			print('Invalid Id!')
		except:
			return screen_Wallet

	printScreenHeader(scrBar = '', msgBar = f'Wallet Id selected [{wid} - ' + widReg['name'] + ']')

	menu = {
		'titles':[
			"1 - Send",
			"2 - Receive",
			"3 - Information and history",
			"4 - Export private Key",
			"5 - Back",
			"0 - Exit"
		],
		'funcs':[
			screen_Send,
			screen_Recv,
			screen_BalanceHistoryInfo,
			screen_ExportPrivateKey,
			screen_Wallet,
			screen_Exit
		]
	}

	return menu['funcs'][exec_menu(menu['titles'])]

def screen_Send():

# TODO

	try:
		sendToAddr = input('Send to (blank to go back): ')
		amount = float(input('Amount (blank or 0 to go back): '))
		fee = float(input('Fee (blank to go back. 0 = to automatically estimate): '))
		locktime = int(input('Locktime (blank to go back. 0 = Default): '))
		min_confirms = int(input('Minimal confirmation needed for an UTXO before it will included in inputs (blank to go back. 0 = Default): '))
	except:
		if not sendToAddr or not amount:
			return screen_OperWltt

	confirm = input("CONFIRM? Write 'YES' to confirm out something else to discart.")

	if confirm == 'YES':
		trx = bitcoinlib.wallets.send_to(to_address = sendToAddr, account_id = widReg['id'], amount = amount, fee = fee, min_confirms = min_confirms, locktime = locktime)
	else:
		print('Transaction aborted!')
	
	print('Pause [ENTER].')
	input()

	return screen_OperWltt

def screen_Recv():
	print('Not implemented')
	sys.exit(0)

def screen_ExportPrivateKey():
	global QRCODE_LIB_PRESENT
	global HOME_DIR

	printScreenHeader(scrBar = 'Export Private Key', msgBar = 'Wallet ' + widReg['name'])

	w = bitcoinlib.wallets.HDWallet(widReg['id'])

	print('Private key (WIF): ' + w.get_key().wif)
#	print('Seed: ' + bitcoinlib.mnemonic.Mnemonic().to_mnemonic(w.get_key().wif))
	print('Path: ' + w.get_key().path)

	if QRCODE_LIB_PRESENT == True:

		menu = ["1 - Print Private key to QR code PNG file",
		        "2 - Print Seed to QR code PNG file",
		        "3 - Print PK and Seed to QR code PNG file",
		        "ENTER - Back"]

		prvQrCodeFileName  = ''
		seedQrCodeFileName = ''

		opt = exec_menu(menu)

		if opt == 0 or opt == 2:
			prvQrCodeFileName = input('PNG file name to print PK: ')
			prvQrCodeFileName = ''.join((HOME_DIR, prvQrCodeFileName))

		if opt == 1 or opt == 2:
			seedQrCodeFileName = input('PNG file name to print seed: ')
			seedQrCodeFileName = ''.join((HOME_DIR, seedQrCodeFileName))

		if prvQrCodeFileName != '':
			if printQRCodeToFile(prvQrCodeFileName, w.get_key().wif) == False:
				print(f'Error creating QRCode PK: {prvQrCodeFileName}')
			else:
				print(f'Created QRCode PK file: {prvQrCodeFileName}')

		if seedQrCodeFileName != '':
			if printQRCodeToFile(seedQrCodeFileName, w.get_key().wif) == False:
				print(f'Error creating seed PK: {prvQrCodeFileName}')
			else:
				print(f'Created QRCode seed file: {prvQrCodeFileName}')

	print("Pause [ENTER].")
	input()

	return screen_OperWltt

def printQRCodeToFile(filename: str, data: str) -> bool:
	try:
		qr = qrcode.QRCode(version = 1,
		                   error_correction = qrcode.constants.ERROR_CORRECT_H,
		                   box_size = 10,
		                   border = 4)
		qr.add_data(data)
		qr.make(fit = True)

		img = qr.make_image(fill_color = "black", back_color = "white")

		img.save(filename)

	except:
		return False

	return True

def screen_BalanceHistoryInfo():
	printScreenHeader(scrBar = 'Wallet Balance', msgBar = 'Wallet ' + widReg['name'])

	print(bitcoinlib.wallets.HDWallet(widReg['id']).info())
#	w = bitcoinlib.wallets.HDWallet(widReg['id'])
#	print('Balance: ', end = '')
#	print(w.balance())

#	print(w.accounts())
#	print(w.balance_update_from_serviceprovider())
#	print(w.default_account_id)
	print('Pause [ENTER]')
	input()
#TODO
	return screen_OperWltt

def screen_Cfg():
	menu = {
		'titles':[
			"1 - Select a new Bitcoin lib path",
			"2 - Back",
			"0 - Exit"
		],
		'funcs':[
			screen_SelPthBTCLib,
			screen_Main,
			screen_Exit
		]
	}

	return menu['funcs'][exec_menu(menu['titles'])]

def screen_Wallet():
	menu = {
		'titles':[
			"1 - Create a new wallet",
			"2 - Delete wallet",
			"3 - Operate wallet (send/recv/export keys/info)",
			"4 - Import a wallet",
			"5 - Back",
			"0 - Exit"
		],
		'funcs':[
			screen_CreaWltt,
			screen_DelWltt,
			screen_OperWltt,
			screen_ImpWltt,
			screen_Main,
			screen_Exit
		]
	}

	setStatusMsgBars('Main Menu', '')

	return menu['funcs'][exec_menu(menu['titles'])]

def screen_ImpWltt():
	print('Not implemented')
	sys.exit(0)

def screen_Exit():
	print('Exit')
	sys.exit(0)

def screen_Main():
	menu = {
		'titles':[
			"1 - Wallet menu",
			"2 - Configs (DB path, backups, nodes/servers)",
			"0 - Exit"
		],
		'funcs':[
			screen_Wallet,
			screen_Cfg,
			screen_Exit
		]
	}

	setStatusMsgBars('Config Menu', '')

	return menu['funcs'][exec_menu(menu['titles'])]

def main(argv):
	scr = screen_Main

	while True:
		scr = scr()

if __name__ == '__main__':

	HOME_DIR = os.path.expanduser("~/")
#	BTCLIB_DB_PATH = os.getenv("HOME") + '/.bitcoinlib/database/bitcoinlib.sqlite'
	BTCLIB_DB_PATH = HOME_DIR + '.bitcoinlib/database/bitcoinlib.sqlite'
	if os.path.isfile(BTCLIB_DB_PATH) == False:
		BTCLIB_DB_PATH = 'UNDEFINED WALLET DB'

#	signal.signal(signal.SIGWINCH, getTerminalSize)     not working now. input() supresses the signal
	getTerminalSize(0, 0)

	main(sys.argv)

	sys.exit(0)
