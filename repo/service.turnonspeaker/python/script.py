import xbmcaddon

from lib import tinytuya
 
addon = xbmcaddon.Addon(id="service.turnonspeaker")
ip = addon.getSetting("ip")
device_id = addon.getSetting("device_id")
local_key = addon.getSetting("local_key")

d = tinytuya.OutletDevice(device_id, ip, local_key)
d.set_version(3.3)
d.turn_on()
