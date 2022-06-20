#! /usr/bin/env python
# -*- coding: utf-8 -*-
####################
# Copyright (c) 2016, Perceptive Automation, LLC. All rights reserved.
# http://www.indigodomo.com

import indigo

import os
import sys

import time
import datetime

from datetime import timedelta

# Note the "indigo" module is automatically imported and made available inside
# our global name space by the host process.

################################################################################
class Plugin(indigo.PluginBase):
	########################################
	def __init__(self, pluginId, pluginDisplayName, pluginVersion, pluginPrefs):
		super(Plugin, self).__init__(pluginId, pluginDisplayName, pluginVersion, pluginPrefs)
		self.sleepTime = int(pluginPrefs.get("sleepTime", 10))
		#self.sleepTime = 10

		#self.debug = True

		self.fixit = False #For fixing things only!

		self.reset = False

		self.curPulses = dict()
		#self.timeSinceReset = dict()
		self.hourOfDay = time.strftime("%H")
		self.dayOfMonth = time.strftime("%d")
		self.monthOfYear = time.strftime("%m")

	def deviceStartComm(self, dev):
		dev.stateListOrDisplayStateIdChanged()
		#self.sleepTime = 30
		#self.updating = False
		#self.tempStore = 0
		#self.resetCounters(dev) #No! Stupid idea!
		self.curPulses[dev.id] = int(dev.states['hourCurrent'])
		#self.timeSinceReset[dev.id] = 0
		#dev.updateStateOnServer("day29",128) #182
		#dev.updateStateOnServer("day01",1303) #1303
		#dev.updateStateOnServer("day02",0) #0

	def deviceStopComm(self, dev):
		dev.updateStateOnServer("hourCurrent",self.curPulses[dev.id])

	def getStateList(self, filter=None, valuesDict=dict(), typeId='', targetId=0):
		stateList = list()
		self.debugLog(valuesDict)
		#devId = zint(valuesDict.get(filter,''))
		#if devId:
			#for state in indigo.devices[devId].states:
				#stateList.append((state,state))
		return stateList

	def pulseInc(self, action, dev):
		#indigo.server.log("Pulse received: %s" % dev.name)
		self.curPulses[dev.id] = self.curPulses[dev.id] + 1

	def doReset(self, action, dev):
		self.resetCounters(dev)


	def resetCounters(self,dev):
		self.curPulses[dev.id] = 0
		key_value_list = [
		{"key":"hourMinus24","value":0},
		{"key":"hourMinus23","value":0},
		{"key":"hourMinus22","value":0},
		{"key":"hourMinus21","value":0},
		{"key":"hourMinus20","value":0},
		{"key":"hourMinus19","value":0},
		{"key":"hourMinus18","value":0},
		{"key":"hourMinus17","value":0},
		{"key":"hourMinus16","value":0},
		{"key":"hourMinus15","value":0},
		{"key":"hourMinus14","value":0},
		{"key":"hourMinus13","value":0},
		{"key":"hourMinus12","value":0},
		{"key":"hourMinus11","value":0},
		{"key":"hourMinus10","value":0},
		{"key":"hourMinus09","value":0},
		{"key":"hourMinus08","value":0},
		{"key":"hourMinus07","value":0},
		{"key":"hourMinus06","value":0},
		{"key":"hourMinus05","value":0},
		{"key":"hourMinus04","value":0},
		{"key":"hourMinus03","value":0},
		{"key":"hourMinus02","value":0},
		{"key":"hourMinus01","value":0},
		{"key":"hourCurrent","value":0},
		{"key":"hour00","value":0},
		{"key":"hour01","value":0},
		{"key":"hour02","value":0},
		{"key":"hour03","value":0},
		{"key":"hour04","value":0},
		{"key":"hour05","value":0},
		{"key":"hour06","value":0},
		{"key":"hour07","value":0},
		{"key":"hour08","value":0},
		{"key":"hour09","value":0},
		{"key":"hour10","value":0},
		{"key":"hour11","value":0},
		{"key":"hour12","value":0},
		{"key":"hour13","value":0},
		{"key":"hour14","value":0},
		{"key":"hour15","value":0},
		{"key":"hour16","value":0},
		{"key":"hour17","value":0},
		{"key":"hour18","value":0},
		{"key":"hour19","value":0},
		{"key":"hour20","value":0},
		{"key":"hour21","value":0},
		{"key":"hour22","value":0},
		{"key":"hour23","value":0},
		{"key":"dayMinus31","value":0},
		{"key":"dayMinus30","value":0},
		{"key":"dayMinus29","value":0},
		{"key":"dayMinus28","value":0},
		{"key":"dayMinus27","value":0},
		{"key":"dayMinus26","value":0},
		{"key":"dayMinus25","value":0},
		{"key":"dayMinus24","value":0},
		{"key":"dayMinus23","value":0},
		{"key":"dayMinus22","value":0},
		{"key":"dayMinus21","value":0},
		{"key":"dayMinus20","value":0},
		{"key":"dayMinus19","value":0},
		{"key":"dayMinus18","value":0},
		{"key":"dayMinus17","value":0},
		{"key":"dayMinus16","value":0},
		{"key":"dayMinus15","value":0},
		{"key":"dayMinus14","value":0},
		{"key":"dayMinus13","value":0},
		{"key":"dayMinus12","value":0},
		{"key":"dayMinus11","value":0},
		{"key":"dayMinus10","value":0},
		{"key":"dayMinus09","value":0},
		{"key":"dayMinus08","value":0},
		{"key":"dayMinus07","value":0},
		{"key":"dayMinus06","value":0},
		{"key":"dayMinus05","value":0},
		{"key":"dayMinus04","value":0},
		{"key":"dayMinus03","value":0},
		{"key":"dayMinus02","value":0},
		{"key":"dayMinus01","value":0},
		{"key":"dayCurrent","value":0},
		{"key":"day01","value":0},
		{"key":"day02","value":0},
		{"key":"day03","value":0},
		{"key":"day04","value":0},
		{"key":"day05","value":0},
		{"key":"day06","value":0},
		{"key":"day07","value":0},
		{"key":"day08","value":0},
		{"key":"day09","value":0},
		{"key":"day10","value":0},
		{"key":"day11","value":0},
		{"key":"day12","value":0},
		{"key":"day13","value":0},
		{"key":"day14","value":0},
		{"key":"day15","value":0},
		{"key":"day16","value":0},
		{"key":"day17","value":0},
		{"key":"day18","value":0},
		{"key":"day19","value":0},
		{"key":"day20","value":0},
		{"key":"day21","value":0},
		{"key":"day22","value":0},
		{"key":"day23","value":0},
		{"key":"day24","value":0},
		{"key":"day25","value":0},
		{"key":"day26","value":0},
		{"key":"day27","value":0},
		{"key":"day28","value":0},
		{"key":"day29","value":0},
		{"key":"day30","value":0},
		{"key":"day31","value":0},
		{"key":"startedOn","value":0}
		]
		dev.updateStatesOnServer(key_value_list)
		stateToDisplay = dev.ownerProps.get("stateToDisplay","")
		if (stateToDisplay != ""):
			dev.updateStateOnServer("displayState",dev.states[stateToDisplay])


	def runConcurrentThread(self):
		try:
			while True:

				key_list_common = []
				key_list_hour = []

				newHour = False
				newDay = False

				if self.fixit: #For fixing things only; not used in normal operation!
					newHour = True
					self.fixit = False

				if self.hourOfDay != time.strftime("%H"):
					newHour = True
				if self.dayOfMonth != time.strftime("%d"):
					newDay = True

				self.hourOfDay = time.strftime("%H")
				self.dayOfMonth = time.strftime("%d")
				self.monthOfYear = time.strftime("%m")

				self.hourOfDayState = "hour" + self.hourOfDay
				self.dayOfMonthState = "day" + self.dayOfMonth

				for d in indigo.devices.iter("self.counter"):

					if int(d.states["startedOn"]) == 0:
						d.updateStateOnServer("startedOn",0) #Start counting days since we've been running
						startedOn = int(self.dayOfMonth)
					elif int(d.states["startedOn"]) <= int(self.dayOfMonth):
						d.updateStateOnServer("startedOn",999) #Disable after 1 month
						startedOn = 999
					else:
						startedOn = int(d.states["startedOn"])


					dayPulses = 0 #Init
					monthPulses = 0 #Init
					month31Pulses = 0 #Init
					hourAvg = 0 #Init
					hourAvg24 = 0 #Init
					dayAvgThisMonth = 0 #Init
					dayAvg31Days = 0 #Init
					daysRunningCount = 1 #Init inc today

					daysLastMonth = 30 #TODO

					for di in range(24):  #00-23
						diStr = str(di)
						if di < int(self.hourOfDay): #Prior to current hour as we add curPulses afterwards
							dayPulses = dayPulses + int(d.states["hour" + diStr.zfill(2)])
						#self.debugLog("%s: %s" % (diStr,str(dayPulses)))
						hourAvg24 = hourAvg24 + int(d.states["hour" + diStr.zfill(2)])

					for mi in range(31): #From 0th to 30th, +1
						miNum = mi+1
						miStr = str(miNum)
						if miNum < int(self.dayOfMonth): #Prior to current day as we add dayPulses afterwards
							monthPulses = monthPulses + int(d.states["day" + miStr.zfill(2)])
							month31Pulses = month31Pulses + int(d.states["day" + miStr.zfill(2)])
							daysRunningCount = daysRunningCount + 1
						elif startedOn <= miNum <= daysLastMonth:
							month31Pulses = month31Pulses + int(d.states["day" + miStr.zfill(2)])
							daysRunningCount = daysRunningCount + 1
						dayAvg31Days = dayAvg31Days + int(d.states["day" + miStr.zfill(2)])


					dayPulses = dayPulses + int(self.curPulses[d.id])
					monthPulses = monthPulses + int(dayPulses)
					month31Pulses = month31Pulses + int(dayPulses)

					hourAvg = dayPulses / (int(self.hourOfDay)+1) # Total so far / how many hours since midnight
					dayAvgThisMonth = monthPulses / int(self.dayOfMonth) # Total so far / how many days into month

					hourAvg24 = hourAvg24 / 24
					dayAvg31Days = month31Pulses / daysRunningCount # Total so far / how many days into month
					#dayAvg31 / 31

					key_list_common = [
					{"key":"hourCurrent","value":self.curPulses[d.id]},
					{"key":self.hourOfDayState,"value":self.curPulses[d.id]},
					{"key":"averageHourlyToday","value":hourAvg},
					{"key":"averageHourly24Hours","value":hourAvg24},
					{"key":"dayCurrent","value":dayPulses},
					{"key":self.dayOfMonthState,"value":dayPulses},
					{"key":"averageDailyThisMonth","value":dayAvgThisMonth},
					{"key":"averageDaily31Days","value":dayAvg31Days},
					{"key":"monthCurrent","value":monthPulses},
					{"key":"hourOfDay","value":self.hourOfDay},
					{"key":"dayOfMonth","value":self.dayOfMonth},
					{"key":"daysRunning","value":daysRunningCount}
					]

					#key_value_list = key_list1 + key_list2
					#d.updateStatesOnServer(key_value_list)

					#if (self.timeSinceReset[d.id] % 3600 == 0): #Every hour, not on the hour
					if (newHour):
						key_list_hour = [
						{"key":"hourMinus24","value":d.states["hourMinus23"]},
						{"key":"hourMinus23","value":d.states["hourMinus22"]},
						{"key":"hourMinus22","value":d.states["hourMinus21"]},
						{"key":"hourMinus21","value":d.states["hourMinus20"]},
						{"key":"hourMinus20","value":d.states["hourMinus19"]},
						{"key":"hourMinus19","value":d.states["hourMinus18"]},
						{"key":"hourMinus18","value":d.states["hourMinus17"]},
						{"key":"hourMinus17","value":d.states["hourMinus16"]},
						{"key":"hourMinus16","value":d.states["hourMinus15"]},
						{"key":"hourMinus15","value":d.states["hourMinus14"]},
						{"key":"hourMinus14","value":d.states["hourMinus13"]},
						{"key":"hourMinus13","value":d.states["hourMinus12"]},
						{"key":"hourMinus12","value":d.states["hourMinus11"]},
						{"key":"hourMinus11","value":d.states["hourMinus10"]},
						{"key":"hourMinus10","value":d.states["hourMinus09"]},
						{"key":"hourMinus09","value":d.states["hourMinus08"]},
						{"key":"hourMinus08","value":d.states["hourMinus07"]},
						{"key":"hourMinus07","value":d.states["hourMinus06"]},
						{"key":"hourMinus06","value":d.states["hourMinus05"]},
						{"key":"hourMinus05","value":d.states["hourMinus04"]},
						{"key":"hourMinus04","value":d.states["hourMinus03"]},
						{"key":"hourMinus03","value":d.states["hourMinus02"]},
						{"key":"hourMinus02","value":d.states["hourMinus01"]},
						{"key":"hourMinus01","value":d.states["hourCurrent"]},
						{"key":"hourCurrent","value":self.curPulses[d.id]}
						]
						#d.updateStatesOnServer(key_value_list)
						self.curPulses[d.id] = 0

					if (newDay):
						key_list_day = [
						{"key":"dayMinus31","value":d.states["dayMinus30"]},
						{"key":"dayMinus30","value":d.states["dayMinus29"]},
						{"key":"dayMinus29","value":d.states["dayMinus28"]},
						{"key":"dayMinus28","value":d.states["dayMinus27"]},
						{"key":"dayMinus27","value":d.states["dayMinus26"]},
						{"key":"dayMinus26","value":d.states["dayMinus25"]},
						{"key":"dayMinus25","value":d.states["dayMinus24"]},
						{"key":"dayMinus24","value":d.states["dayMinus23"]},
						{"key":"dayMinus23","value":d.states["dayMinus22"]},
						{"key":"dayMinus22","value":d.states["dayMinus21"]},
						{"key":"dayMinus21","value":d.states["dayMinus20"]},
						{"key":"dayMinus20","value":d.states["dayMinus19"]},
						{"key":"dayMinus19","value":d.states["dayMinus18"]},
						{"key":"dayMinus18","value":d.states["dayMinus17"]},
						{"key":"dayMinus17","value":d.states["dayMinus16"]},
						{"key":"dayMinus16","value":d.states["dayMinus15"]},
						{"key":"dayMinus15","value":d.states["dayMinus14"]},
						{"key":"dayMinus14","value":d.states["dayMinus13"]},
						{"key":"dayMinus13","value":d.states["dayMinus12"]},
						{"key":"dayMinus12","value":d.states["dayMinus11"]},
						{"key":"dayMinus11","value":d.states["dayMinus10"]},
						{"key":"dayMinus10","value":d.states["dayMinus09"]},
						{"key":"dayMinus09","value":d.states["dayMinus08"]},
						{"key":"dayMinus08","value":d.states["dayMinus07"]},
						{"key":"dayMinus07","value":d.states["dayMinus06"]},
						{"key":"dayMinus06","value":d.states["dayMinus05"]},
						{"key":"dayMinus05","value":d.states["dayMinus04"]},
						{"key":"dayMinus04","value":d.states["dayMinus03"]},
						{"key":"dayMinus03","value":d.states["dayMinus02"]},
						{"key":"dayMinus02","value":d.states["dayMinus01"]},
						{"key":"dayMinus01","value":d.states["dayCurrent"]},
						{"key":"dayCurrent","value":0}
						]
						#d.updateStatesOnServer(key_value_list)
						#self.curPulses[d.id] = 0

					key_value_list = key_list_common + key_list_hour #Combine lists
					d.updateStatesOnServer(key_value_list) #Only calls once to server

					stateToDisplay = d.ownerProps.get("stateToDisplay","")
					if (stateToDisplay != ""):
						d.updateStateOnServer("displayState",d.states[stateToDisplay])

				self.sleep(self.sleepTime)
		except self.StopThread:
			pass
