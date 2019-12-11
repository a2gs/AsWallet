#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

import sys, os
import bitcoinlib

VERSION = float(0.1)
BTCLIB_DB_PATH = str('/home/agnes/.bitcoinlib/database/bitcoinlib.sqlite')
STATUSBAR = str('')
MSGBAR = str('')
OS_CLEARSCREEN = str('')

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

		print('\n')

		[print(i) for i in opts]

		print('\n')

		try:
			x = int(input('Option: '))
		except:
			continue

		if x < totOpts:
			return x - 1

def setStatusMsgBars(sts, msg):
	global STATUSBAR
	global MSGBAR

	STATUSBAR = sts
	MSGBAR = msg

def printScreenHeader():
	global VERSION
	global BTCLIB_DB_PATH
	global STATUSBAR
	global MSGBAR

	clearscreen()
	print('As Wallet\n=========')
	print(f'(Version: \'{VERSION}\' BitcoinLib DB path: \'{BTCLIB_DB_PATH}\')\n')
	print(f'{STATUSBAR}')
	print(f'Status: {MSGBAR}\n')

def screen_SelPthBTCLib():
# bitcoinlib.db.DbInit(databasefile='/home/docs/.bitcoinlib/database/bitcoinlib.sqlite')[source]
	print('Not implemented')
	sys.exit(0)

def screen_CreaBTCWltt():
	wlttype  = str('')
	wltnet   = str('')
	wltname  = str('')

	setStatusMsgBars('Create BTC Wallet Menu', '')

	try:
		wltname = input('Wallet name (blank to go back): ')
	except:
		return

	setStatusMsgBars('Create BTC Wallet Menu', 'Name ' + wltname)

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

	setStatusMsgBars('Create BTC Wallet Menu', 'Name [' + wltname + '] Type [' + wlttype + ']')

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

	setStatusMsgBars('Create BTC Wallet Menu', 'Name [' + wltname + '] Type [' + wlttype + ']' + ' Net [' + wltnet + ']')
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
	acc = bitcoinlib.wallets.wallets_list(BTCLIB_DB_PATH)
	[print(i) for i in acc]

	input()

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
			"1 - Select a new Bitcoin lib path",
			"2 - Confirm default path and go to Wallet menu",
			"0 - Exit"
		],
		'funcs':[
			screen_SelPthBTCLib,
			screen_Wallet,
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
	OS_CLEARSCREEN = os.name
	main(sys.argv)
	sys.exit(0)
