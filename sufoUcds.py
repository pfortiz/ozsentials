#
# datOz18/UAM : semantics
# Author: Patricio F. Ortiz
# Date:  June 5, 2017
#
# Version 1.0 Declaration of UCDs as a dictionary

# Version 1.1 Adding descriptions and possible units
# Data: August 29, 2019

utcUnix = "TIME_UTC_UNIX"
year = "TIME_YEAR"
month = "TIME_MONTH"
day = "TIME_DAY"
hours = "TIME_HOURS"
minutes = "TIME_MINUTES"
seconds = "TIME_SECONDS"
timeOfDay = "TIME_LOCAL_TOD"
minSinceMidnight = "TIME_LOCAL_MINUTES"
secSinceMidnight = "TIME_LOCAL_SECONDS"
dow = "TIME_DOW"
doy = "TIME_DOY"
isdst = "TIME_ISDST"
hrLocal = "TIME_HUMAN_LOCAL"
hrUTC = "TIME_HUMAN_UTC"
msmmof5 = "DB_ACCEL_MSMMOF5"

timeDerived = [year, month, day, hours, minutes, seconds, timeOfDay, 
    minSinceMidnight, secSinceMidnight, dow, doy, isdst]

categories = {
    "AIR_QUALITY": {
        "UCDS": [ "AQ_PM1", "AQ_PM25", "AQ_PM10", "AQ_PM4", "AQ_PMSUM",
                "AQ_PART_DENSITY", "AQ_NOISE", "AQ_CO", "AQ_NO", "AQ_NO2",
                    "AQ_NOX", "AQ_O3", "AQ_SO2"],
        "description": "Quantities related to air quality, always outdoors"
        },
        
    "METEOROLOGICAL":{
        "UCDS": ["MET_TEMP", "MET_RH", "MET_AP", "MET_WIND_SPEED_HORIZ",
                       "MET_WIND_SPEED_VERT", "MET_WIND_BEARING",
                       "MET_PRECIP_TYPE", "MET_PRECIP_RATE", "MET_PRECIP_VOLUME", ],
        "description": "Meteorological quantities, always outdoors"
        },
    "TRAFFIC" :{
        "UCDS": [ "TRAFF_FLOW","TRAFF_OCCUP", "TRAFF_COUNTS", "TRAFF_INTERVAL"],
        "description": "Traffic quantities, some may have to describe the sensor used to acquire the data, e.g, camera, magnetic loops"
        },
    "GEOLOCATION":{
        "UCDS": [ "GLOC_LON", "GLOC_LAT", "GLOC_HASL"], 
        "description": "Description of a place on planet Earth"
        },
    "DATA":{
        "UCDS": ["DATA_DR", "COUNTER"],
        "description": "Quantities related to any kind of data"
        },
    "TIME":{
        "UCDS": ["TIME_UTC_UNIX", "TIME_YEAR", "TIME_MONTH", "TIME_DAY",
             "TIME_HOURS", "TIME_MINUTES", "TIME_SECONDS", "TIME_LOCAL_TOD",
             "TIME_LOCAL_MINUTES", "TIME_LOCAL_SECONDS", "TIME_DOW",
             "TIME_ISDST", "TIME_HUMAN_LOCAL", "TIME_HUMAN_UTC",],
        "description": "Time related quantities"
        },
    "IDENTIFIEERS":{
        "UCDS": ["ID_MAIN" ],
        "description": "Information used to identify a resource or instrument"
        },
    "INDOORS":{
        "UCDS": [],
        "description": "Quantities measured indoors only. Indoors and outdoors should not be described by the same UCDs. If someone what to compare them, then it should be done explicitely, e.g., comparing indoors and outdoors air temperature."
        },
}

ucds = {
    "AQ_PM1" :{
        "face":"PM1",
        "dash": "PM1",
        "button":"PM1",
        "label":"PM1",
        "export":"PM1",
        "description": "Particulate Matter less than 1 micron in diameter density",
        "units":["ug/m3"],
        "validMin":0,
        "validMax":"",
        "names":["PM1", "pm1"]},
    "AQ_PM25" :{
        "face":"PM25",
        "dash": "PM25",
        "button":"PM25",
        "label":"PM25",
        "export":"PM25",
        "description": "Particulate Matter less than 2.5 microns in diameter density",
        "units":["ug/m3"],
        "validMin":0,
        "validMax":"",
        "names":["PM25", "PM2.5", "pm25", "pm2.5"]},
    "AQ_PM10" :{
        "face":"PM10",
        "dash": "PM10",
        "button":"PM10",
        "label":"PM10",
        "export":"PM10",
        "description": "Particulate Matter less than 10 micron in diameter density",
        "units":["ug/m3"],
        "validMin":0,
        "validMax":"",
        "names":["PM10", "pm10"]},
    "AQ_PM4" :{
        "face":"PM4",
        "dash": "PM4",
        "button":"PM4",
        "label":"PM4",
        "export":"PM4",
        "description": "Particulate Matter less than 4 micron in diameter density",
        "units":["ug/m3"],
        "validMin":0,
        "validMax":"",
        "names":["PM4", "pm4"]},
    "AQ_PMSUM" :{
        "face":"TSP",
        "dash": "TSP",
        "button":"TSP",
        "label":"TSP",
        "export":"TSP",
        "description": "Total Suspended Particulate density",
        "units":["ug/m3"],
        "validMin":0,
        "validMax":"",
        "names":["TSP", "tsp"]},
    "AQ_PART_DENSITY" :{
        "face":"P.Count",
        "dash": "P.Count",
        "button":"P.Count",
        "label":"PartCount",
        "export":"P.Count",
        "description": "Particle Count (density per number)",
        "units":["P/cm3", "1/cm3"],
        "validMin":0,
        "validMax":"",
        "names":["PARTICLE COUNT", "particle Count"]},

    "COUNTER" :{
        "face":"Count",
        "dash": "Count",
        "button":"Count",
        "label":"Count",
        "export":"Count",
        "description": "Generic counter...",
        "units":[""],
        "validMin":0,
        "validMax":"",
        "names":["ntimes", "count"]},
    "INST_BATTERY_VOLTAGE" :{
        "face":"Battery Voltage",
        "dash": "Batt Vltg",
        "button":"BattVltg",
        "label":"BattVltg",
        "export":"batVoltage",
        "description": "Battery Voltage",
        "units":["V"],
        "validMin":0,
        "validMax":"",
        "names":["batt", "v", "batteryVoltage", "voltage"]},
    "INST_BATTERY_LEVEL" :{
        "face":"Battery percentage of charge",
        "dash": "Batt Lev",
        "button":"BattLev",
        "label":"BattLev",
        "export":"batLevel",
        "description": "Battery Level",
        "units":["%"],
        "validMin":0,
        "validMax":"",
        "names":["battLev", "batteryLevel" ]},
    "MET_TEMP" : {
        "face":"Air Temperature",
        "dash":"Air Temp",
        "button":"AirTemp",
        "label":"AirTemp",
        "export":"airTemperature",
        "description": "Air temperature (outdoors)",
        "units":["C", "K"],
        "validMin":-35,
        "validMax":45,
        "names":["temp", "t", "airtemp", "temperature"]},
    "MET_RH" : {
        "face":"Relative Humidity",
        "dash":"Rel Hum",
        "button":"RelHum",
        "label":"RelHum",
        "export":"relativeHumidity",
        "description": "Relative Humidity",
        "units":["%"],
        "validMin":0,
        "validMax":100,
        "names":["rh", "relhum", "relativehumidity"]},
    "MET_AP" : {
        "face":"Air Pressure",
        "dash":"Air Press",
        "button":"AirPress",
        "label":"AirPressure",
        "export":"airPressure",
        "description": "Atmospheric Pressure",
        "units":["hPa","mmHg", "kPa"],
        "validMin":930,
        "validMax":1300,
        "names":["pressure", "atmpress", "airpressure", "barometricpressure"]},
    "DATA_NOBS" : {
        "face":"N. of measurements",
        "dash":"# Measurements",
        "button":"NPoints",
        "label":"NPoints",
        "export":"nMeasures",
        "description": "Number of observations",
        "units":[""],
        "validMin":0,
        "validMax":"",
        "names":["npoints", "nmeasurements"]},
    "DATA_DR" : {
        "face":"Dynamic Range",
        "dash":"Dyn.Range",
        "button":"Dyn.Range",
        "label":"Dyn.Range",
        "export":"Dyn.Range",
        "description": "Dynamic range",
        "units":["%s"],
        "validMin":0,
        "validMax":"",
        "names":["dynamic range" ]},
    "GLOC_LON" : {
        "face":"Longitude (east is positive)",
        "dash":"Lon",
        "button":"Lon",
        "label":"Longitude",
        "export":"Lon",
        "description": "Geographic Longitude (East is positive)",
        "units":["deg"],
        "validMin":-180,
        "validMax":180,
        "names":["longitude", "east longitude"]},
    "GLOC_LAT" : {
        "face":"Latitude",
        "dash":"Lat",
        "button":"Lat",
        "label":"Latitude",
        "export":"Lat",
        "description": "Geographic Latitude (North is positive)",
        "units":["deg"],
        "validMin":-90,
        "validMax":90,
        "names":["latitude"]},
    "GLOC_HASL" : {
        "face":"Height above Sea Level",
        "dash":"HASL",
        "button":"HASL",
        "label":"Elevation",
        "export":"H.A.S.L",
        "description": "Height above sea level",
        "units":["m"],
        "validMin":-413,
        "validMax":8484,
        "names":["elevation", "altitude", "heightabovesealevel"]},
    "AQ_NOISE" : {
        "qualifiers":["Peak"],
        "face":"Noise",
        "dash":"Noise",
        "button":"Noise",
        "label":"Noise",
        "export":"Acoustic Noise",
        "description": "Ambient noise level",
        "units":["dB"],
        "validMin":0,
        "validMax":200,
        "names":["noise"]},
    "AQ_CO" : {
        "face":"Carbon monoxide",
        "dash":"CO",
        "button":"CO",
        "label":"CO",
        "export":"CO",
        "description": "Carbon Monoxide concentration",
        "units":["ppb", "ppm"],
        "validMin":0,
        "validMax":"",
        "names":["co"]},
    "AQ_NO" : {
        "face":"Nitrogen monoxide",
        "dash":"NO",
        "button":"NO",
        "label":"NO",
        "export":"NO",
        "description": "Nitrogen Monoxide concentration",
        "units":["ppb", "ppm"],
        "validMin":0,
        "validMax":"",
        "names":["no"]},
    "AQ_NO2" : {
        "face":"Nitrogen dioxide",
        "dash":"NO2",
        "button":"NO2",
        "label":"NO2",
        "export":"NO2",
        "description": "Nitrogen Dioxide concentration",
        "units":["ppb", "ppm"],
        "validMin":0,
        "validMax":"",
        "names":["no2"]},
    "AQ_NOX" : {
        "face":"Nitrogen monoxide plus nitrogen dioxide",
        "dash":"NOx",
        "button":"NOx",
        "label":"NOx",
        "export":"NOx",
        "description": "Nitrogen monoxide plus Nitrogen dioxide concentration",
        "units":["ppb", "ppm"],
        "validMin":0,
        "validMax":"",
        "names":["nox"]},
    "AQ_O3" : {
        "face":"Ozone",
        "dash":"O3",
        "button":"O3",
        "label":"O3",
        "export":"O3",
        "description": "Ozone concentration",
        "units":["ppb", "ppm"],
        "validMin":0,
        "validMax":"",
        "names":["o3", "O3"]},
    "AQ_SO2" : {
        "face":"Sulphur dioxide",
        "dash":"SO2",
        "button":"SO2",
        "label":"SO2",
        "export":"SO2",
        "description": "Sulphur Dioxide concentration",
        "units":["ppb", "ppm"],
        "validMin":0,
        "validMax":"",
        "names":["so2"]},
    utcUnix : {
        "face":"Time",
        "dash":"Time",
        "button":"Time",
        "label":"Time",
        "export":"utime",
        "description": "Time in seconds since 1970.0, or UNIX time",
        "units":["s"],
        "validMin":0,
        "validMax":32503680000,
        "names":["Time"]},
    year : {
        "face":"Year AD",
        "dash":"Year AD",
        "button":"Year",
        "label":"Year",
        "export":"year",
        "description": "Year (Gregorian calendar)",
        "units":["yr"],
        "validMin":0,
        "validMax":3000,
        "names":["Year"]},
    month : {
        "face":"Month",
        "dash":"Month",
        "button":"Month",
        "label":"Month",
        "export":"month",
        "description": "Month (Gregorian calendar)",
        "units":["mo"],
        "validMin":1,
        "validMax":12,
        "names":["Month"]},
    day : {
        "face":"Day",
        "dash":"Day",
        "button":"Day",
        "label":"Day",
        "export":"day",
        "description": "Day (Gregorian calendar)",
        "units":["d"],
        "validMin":1,
        "validMax":31,
        "names":["day"]},
    hours : {
        "face":"Hours",
        "dash":"Hours",
        "button":"Hours",
        "label":"Hours",
        "export":"Hours",
        "description": "Hours of the day (0 to 23)",
        "units":["h"],
        "validMin":0,
        "validMax":23,
        "names":["hour", "hours"]},
    minutes : {
        "face":"Minutes",
        "dash":"Minutes",
        "button":"Minutes",
        "label":"Minutes",
        "export":"Minutes",
        "description": "Minutes of time",
        "units":["min"],
        "validMin":0,
        "validMax":59,
        "names":["minutes", "Minutes"]},
    seconds : {
        "face":"Seconds",
        "dash":"Seconds",
        "button":"Seconds",
        "label":"Seconds",
        "export":"Seconds",
        "description": "Seconds of time",
        "units":["s"],
        "validMin":0,
        "validMax":59,
        "names":["Seconds", "seconds"]},
    isdst : {
        "face":"isDST",
        "dash":"isDSST",
        "button":"isDST",
        "label":"isDST",
        "export":"isDST",
        "description": "Summer time flag, Winter=0, Summer=1",
        "units":[""],
        "validMin":0,
        "validMax":1,
        "names":["isdst", "isDST"]},
    dow : {
        "face":"DOW",
        "dash":"DOW",
        "button":"DOW",
        "label":"DOW",
        "export":"dayOfWeek",
        "description": "Day of the week. 0=Monday, 6=Sunday",
        "units":["d"],
        "validMin":0,
        "validMax":6,
        "names":["dow", "dayOfWeek"]},
    doy : {
        "face":"DOY",
        "dash":"DOY",
        "button":"DOY",
        "label":"DayOfYear",
        "export":"dayOfYear",
        "description": "Day of the year. Jan 01 = 1",
        "units":["d"],
        "validMin":0,
        "validMax":366,
        "names":["doy", "dayOfYear"]},
    minSinceMidnight : {
        "face":"MinInDay",
        "dash":"Min Since Midn",
        "button":"Mins",
        "label":"MinutesSinceMidnight",
        "export":"minsSinceMidnght",
        "description": "Minutes since midnight. 0 to 1439",
        "units":["min"],
        "validMin":0,
        "validMax":1439,
        "names":["msm", "minutesSinceMidnight"]},
    secSinceMidnight : {
        "face":"SecInDay",
        "dash":"Sec Since Midn",
        "button":"Secs",
        "label":"secondsSinceMidnght",
        "export":"secsSinceMidnght",
        "description": "Seconds since midnight. 0 to 86399",
        "units":["sec"],
        "validMin":0,
        "validMax":86399,
        "names":["ssm", "secondsSinceMidnight"]},
    timeOfDay : {
        "face":"timeOfDay",
        "dash":"T.o.day",
        "button":"t.o.day",
        "label":"timeOfDay",
        "export":"timeOfDay",
        "description": "Compacted time of the day (HH:MM): 0000 to 2359",
        "units":["hhmm"],
        "validMin":0,
        "validMax":2359,
        "names":["timeOfDay"]},
    "TIME_OFFSET" : {
        "face":"Offset",
        "dash":"Offset",
        "button":"Offset",
        "export":"timeOffset",
        "label":"timeOffset",
        "description": "Time offset (generic)",
        "units":["m", "s", "d"],
        "validMin":-1000000,
        "validMax":1000000,
        "names":["timeOffset"]},
    "TRAFF_FLOW" : {
        "face":"Flow",
        "dash":"Flow",
        "button":"T-Flow",
        "export":"T_Flow",
        "label":"TrafficFlow",
        "description": "Traffic Flow (number of cars over a time interval)",
        "units":["cars/min"],
        "validMin":0,
        "validMax":5000,
        "names":["flow"]},
    "TRAFF_SPEED" : {
        "face":"TSpeed",
        "dash":"TSpeed",
        "button":"TSpeed",
        "label":"TrafficSpeed",
        "export":"TSpeed",
        "description": "Traffic Speed ",
        "units":["km/h", "mi/h"],
        "validMin":0,
        "validMax":200,
        "names":["Tspeed", "trafficSpeed"]},
    "TRAFF_OCCUP" : {
        "face":"TOccup",
        "dash":"TOccup",
        "button":"TOccup",
        "label":"TrafficOccup",
        "export":"TOccup",
        "description": "Traffic occupancy (number of cars on a sensor)",
        "units":["%"],
        "validMin":0,
        "validMax":5000,
        "names":["occupancy", "occup"]},
    "TRAFF_COUNTS" : {
        "face":"NCars",
        "dash":"NCars",
        "button":"NCars",
        "label":"NCars",
        "export":"NCars",
        "description": "Traffic counts (number of cars on a sensor)",
        "units":[""],
        "validMin":0,
        "validMax":5000,
        "names":["ncars", "counts"]},
    "TRAFF_INTERVAL" : {
        "face":"Interval",
        "dash":"Interval",
        "button":"Interval",
        "label":"TrafficInterval",
        "export":"Interval",
        "description": "Time interval used to determine Traffic properties",
        "units":["min"],
        "validMin":0,
        "validMax":5000,
        "names":["interval"]},
    "LUT_INDEX" : {
        "face":"LUTind",
        "dash":"LUTind",
        "button":"LUTind",
        "label":"LUTind",
        "export":"LUTind",
        "description": "Variable used as an LUT index. Var = np.take(lut_values, lut_index)",
        "units":[""],
        "validMin":0,
        "validMax":3000000,
        "names":["lut_index"]},
    "LUT_VALUES" : {
        "face":"LUTval",
        "dash":"LUTval",
        "button":"LUTval",
        "label":"LUTval",
        "export":"LUTval",
        "description": "Variable used as an LUT values. Var = np.take(lut_values, lut_index)",
        "units":[""],
        "names":["lut_value"]},
    "ID_MAIN" : {
        "face":"Identifier",
        "dash":"I.D.",
        "button":"I.D.",
        "label":"MainID",
        "export":"MainId",
        "description": "Main Identifier",
        "units":[""],
        "validMin":"A|0",
        "validMax":"z|10000",
        "names":["identity", "sensor"]},
    "DB_ACCEL_MSMMOF5" : {
        "face":"N/A",
        "dash":"N/A",
        "button":"N/A",
        "label":"N/A",
        "export":"timePick5m",
        "description": "Indices for elements with minSinceMidnight multiple of 5",
        "units":[""],
        "validMin":0,
        "validMax":1000000000,
        "names":["msmmof5", "accMinMultOf5"]},
}



def recognise():
    equis = {}
    for ucd in ucds.keys():
        names = ucds[ucd]["names"]
        for name in names:
            equis[name.upper()] = ucd
    return equis

def ucdByName(seek):
    sought = seek.upper()
    known = None
    for ucd in ucds.keys():
        names = ucds[ucd]["names"]
        for name in names:
#            print "s/n", sought, name
            if sought == name.upper():
                ucds[ucd]["id"] = ucd
                return ucds[ucd]
    return known

def isUCD(seek):
    sought = seek.upper()
    try:
        ucd = ucds[sought]
        ucd["id"] = str(sought)
        ucd["tname"] = ucd["names"][0]
        return ucd
    except:
        for ucd in ucds.keys():
            names = ucds[ucd]["names"]
            for name in names:
#            print "s/n", sought, name
                if sought == name.upper():
                    ucds[ucd]["id"] = ucd
                    ucds[ucd]["tname"] = seek
                    return ucds[ucd]
    return {"id": None, "tname":None }
