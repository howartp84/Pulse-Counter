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

from sunrise_sunset import SunriseSunset

# Note the "indigo" module is automatically imported and made available inside
# our global name space by the host process.

################################################################################
class Plugin(indigo.PluginBase):
	########################################
	def __init__(self, pluginId, pluginDisplayName, pluginVersion, pluginPrefs):
		super(Plugin, self).__init__(pluginId, pluginDisplayName, pluginVersion, pluginPrefs)
		self.sleepTime = 30
		self.dontStart = True
		self.reset = False

		indigo.server.log("Waiting for system clock to reach :00 seconds...")

	def deviceStartComm(self, dev):
		dev.stateListOrDisplayStateIdChanged()
		#self.sleepTime = 30
		self.updating = False
		self.tempStore = 0
		self.resetCounters(dev)

	def resetCounters(self,dev):
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
		{"key":"hourMinus9","value":0},
		{"key":"hourMinus8","value":0},
		{"key":"hourMinus7","value":0},
		{"key":"hourMinus6","value":0},
		{"key":"hourMinus5","value":0},
		{"key":"hourMinus4","value":0},
		{"key":"hourMinus3","value":0},
		{"key":"hourMinus2","value":0},
		{"key":"hourMinus1","value":0},
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
		{"key":"dayMinus9","value":0},
		{"key":"dayMinus8","value":0},
		{"key":"dayMinus7","value":0},
		{"key":"dayMinus6","value":0},
		{"key":"dayMinus5","value":0},
		{"key":"dayMinus4","value":0},
		{"key":"dayMinus3","value":0},
		{"key":"dayMinus2","value":0},
		{"key":"dayMinus1","value":0},
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
		{"key":"monthMinus12","value":0},
		{"key":"monthMinus11","value":0},
		{"key":"monthMinus10","value":0},
		{"key":"monthMinus9","value":0},
		{"key":"monthMinus8","value":0},
		{"key":"monthMinus7","value":0},
		{"key":"monthMinus6","value":0},
		{"key":"monthMinus5","value":0},
		{"key":"monthMinus4","value":0},
		{"key":"monthMinus3","value":0},
		{"key":"monthMinus2","value":0},
		{"key":"monthMinus1","value":0},
		{"key":"monthCurrent","value":0},
		{"key":"month01","value":0},
		{"key":"month02","value":0},
		{"key":"month03","value":0},
		{"key":"month04","value":0},
		{"key":"month05","value":0},
		{"key":"month06","value":0},
		{"key":"month07","value":0},
		{"key":"month08","value":0},
		{"key":"month09","value":0},
		{"key":"month10","value":0},
		{"key":"month11","value":0},
		{"key":"month12","value":0}
		]
		dev.updateStatesOnServer(key_value_list)
		

	def runConcurrentThread(self):
		try:
			while True:
			
				if (self.dontStart):
					secs = time.strftime("%S")
					#indigo.server.log(secs)
					if (int(secs) > 1):
						self.sleep(1)
						continue
					else:
						indigo.server.log("Starting clock timer at {} seconds".format(secs))
						self.dontStart = False
			
				for d in indigo.devices.iter("self.pulsecounter"):
					hourOfDay = int(time.strftime("%H")
					dayOfMonth = int(time.strftime("%d")
					monthOfYear = int(time.strftime("%m")
					
					if (hourOfDay != int(d.states["hourOfDay"])):
						if (abs(hourOfDay - int(d.states["hourOfDay"]) > 1)):
							self.reset = True
						else:
							key_value_list = [
							{"key":"hourOfDay","value":str(hourOfDay)},
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
							{"key":"hourMinus10","value":d.states["hourMinus9"]},
							{"key":"hourMinus9","value":d.states["hourMinus8"]},
							{"key":"hourMinus8","value":d.states["hourMinus7"]},
							{"key":"hourMinus7","value":d.states["hourMinus6"]},
							{"key":"hourMinus6","value":d.states["hourMinus5"]},
							{"key":"hourMinus5","value":d.states["hourMinus4"]},
							{"key":"hourMinus4","value":d.states["hourMinus3"]},
							{"key":"hourMinus3","value":d.states["hourMinus2"]},
							{"key":"hourMinus2","value":d.states["hourMinus1"]},
							{"key":"hourMinus1","value":d.states["hourCurrent"]},
							{"key":"hourCurrent","value":0}
							]
							d.updateStatesOnServer(key_value_list)
						
					
					if (dayOfMonth != int(d.states["dayOfMonth"])):
						if (abs(dayOfMonth - int(d.states["dayOfMonth"]) > 1)):
							self.reset = True
						else:
							key_value_list = [
							{"key":"dayOfMonth","value":str(dayOfMonth)},
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
							{"key":"dayMinus10","value":d.states["dayMinus9"]},
							{"key":"dayMinus9","value":d.states["dayMinus8"]},
							{"key":"dayMinus8","value":d.states["dayMinus7"]},
							{"key":"dayMinus7","value":d.states["dayMinus6"]},
							{"key":"dayMinus6","value":d.states["dayMinus5"]},
							{"key":"dayMinus5","value":d.states["dayMinus4"]},
							{"key":"dayMinus4","value":d.states["dayMinus3"]},
							{"key":"dayMinus3","value":d.states["dayMinus2"]},
							{"key":"dayMinus2","value":d.states["dayMinus1"]},
							{"key":"dayMinus1","value":d.states["dayCurrent"]},
							{"key":"dayCurrent","value":0}
							]

					
					if (monthOfYear != int(d.states["monthOfYear"])):
						if (abs(monthOfYear - int(d.states["monthOfYear"]) > 1)):
							self.reset = True
						else:
							key_value_list = [
							{"key":"monthOfYear","value":str(monthOfYear)},
							{"key":"monthMinus12","value":d.states["monthMinus11"]},
							{"key":"monthMinus11","value":d.states["monthMinus10"]},
							{"key":"monthMinus10","value":d.states["monthMinus9"]},
							{"key":"monthMinus9","value":d.states["monthMinus8"]},
							{"key":"monthMinus8","value":d.states["monthMinus7"]},
							{"key":"monthMinus7","value":d.states["monthMinus6"]},
							{"key":"monthMinus6","value":d.states["monthMinus5"]},
							{"key":"monthMinus5","value":d.states["monthMinus4"]},
							{"key":"monthMinus4","value":d.states["monthMinus3"]},
							{"key":"monthMinus3","value":d.states["monthMinus2"]},
							{"key":"monthMinus2","value":d.states["monthMinus1"]},
							{"key":"monthMinus1","value":d.states["monthCurrent"]},
							{"key":"monthCurrent","value":0}
							]
							d.updateStatesOnServer(key_value_list)


					if (self.reset):
						self.resetCounters(d)


					stateToDisplay = dev.ownerProps.get("stateToDisplay","")
					if (stateToDisplay != ""):
						dev.updateStateOnServer("displayState",stateToDisplay)
		
				self.sleep(self.sleepTime)
		except self.StopThread:
			pass
