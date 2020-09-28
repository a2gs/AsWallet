#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

import os
import As_util

TRM_LINES=int()
TRM_COLS=int()

def clearscreen():
	if os.name == 'posix':
		os.system('clear')
	elif os.name == 'nt':
		os.system('cls')
	else:
		print('\n\n\n\n\n')

def setStatusMsgBars(scr, msg):
	As_util.SCREENBAR = scr
	As_util.MSGBAR = msg

def getTerminalSize(sig, frame):
	global TRM_COLS
	global TRM_LINES

	TRM_COLS, TRM_LINES = os.get_terminal_size()

def printScreenHeader(scrBar = '', msgBar = ''):
	global TRM_COLS
	global TRM_LINES

	if scrBar != '':
		As_util.SCREENBAR = scrBar

	if msgBar != '':
		As_util.MSGBAR = msgBar

	clearscreen()
	print('As Wallet'.center(TRM_COLS))
	print('========='.center(TRM_COLS))
	print('-' * TRM_COLS)
	print(f'(Version: \'{As_util.VERSION}\' BitcoinLib DB path: \'{As_util.BTCLIB_DB_PATH}\')\n')
	print(f'* {As_util.SCREENBAR} *'.center(TRM_COLS))
	print(f'Status: {As_util.MSGBAR}\n')
	print('-' * TRM_COLS)

def exec_menu(opts):
	totOpts = len(opts)

	while(1):
		printScreenHeader()

		[print(i) for i in opts]

		print('\n')

		try:
			x = int(input('Option: '))
		except:
			continue

		if x < totOpts:
			return x - 1
