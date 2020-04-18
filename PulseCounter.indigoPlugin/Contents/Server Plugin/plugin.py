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
		self.sleepTime = 10
		
		self.reset = False

		self.curPulses = dict()
		self.timeSinceReset = dict()
		self.hourOfDay = int(time.strftime("%H"))
		self.dayOfMonth = int(time.strftime("%d"))
		self.monthOfYear = int(time.strftime("%m"))

	def deviceStartComm(self, dev):
		dev.stateListOrDisplayStateIdChanged()
		#self.sleepTime = 30
		self.updating = False
		self.tempStore = 0
		self.resetCounters(dev)
		self.curPulses[dev.id] = 0
		self.timeSinceReset[dev.id] = 0

	def pulseInc(self, action, dev):
		#indigo.server.log("Pulse received: %s" % dev.name)
		self.curPulses[dev.id] = self.curPulses[dev.id] + 1
	

	def resetCounters(self,dev):
		dev.ownerProps['curPulses'] = 0
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
		{"key":"hour23","value":0}
		]
		dev.updateStatesOnServer(key_value_list)
		stateToDisplay = dev.ownerProps.get("stateToDisplay","")
		if (stateToDisplay != ""):
			dev.updateStateOnServer("displayState",dev.states[stateToDisplay])
		

	def runConcurrentThread(self):
		try:
			while True:
			
				self.hourOfDay = int(time.strftime("%H"))
				self.dayOfMonth = int(time.strftime("%d"))
				self.monthOfYear = int(time.strftime("%m"))
			
				for d in indigo.devices.iter("self.counter"):
					self.timeSinceReset[d.id] = self.timeSinceReset[d.id] + 10
					
					key_value_list = [
					{"key":"hourCurrent","value":self.curPulses[d.id]}
					]
					d.updateStatesOnServer(key_value_list)
					
					if (self.timeSinceReset[d.id] % 3600 == 0): #On the hour
						key_value_list = [
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
						{"key":"hourCurrent","value":self.curPulses[d.id]}
						]
						d.updateStatesOnServer(key_value_list)
						self.curPulses[d.id] = 0
					
					
					stateToDisplay = d.ownerProps.get("stateToDisplay","")
					if (stateToDisplay != ""):
						d.updateStateOnServer("displayState",d.states[stateToDisplay])
		
				self.sleep(10)
		except self.StopThread:
			pass
