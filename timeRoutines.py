# This is a class on its own to provide some functions to deal with time
# intervals found in the physical sciencies and other areas where
# describing time intervals is important.
#
# This code is based on timex.pl, part of the wAPPPA package.
#
# Stack overflow experts strongly recommend rewriting a perl module into
# python, not trying to convert it automagically. I'll follow that advice.
#
# plotopy already has the jdutil.py module in it. 
# I will include that functionality "as is" in this script
#
# Author: Patricio F. Ortiz
# Website: http://github.com/pfortiz
# Date: May 26, 2017 AD

import math
import datetime as dt
import time
import sys
import arrow   # handles time in an elegant way
import pytz

#class timextra():

# some arrays used by many routines:
timeUnits = ["day", "month", "year", "century", "hour", "minute",
    "second", "doy"]
daysInMond = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthNames = ["dummy", "January", "February", "March", "April", "May",
    "June", "July", "August", "September", "October", "November", "December"]

timeStringDecimalSec = "%Y-%m-%dT%H-%M-%S.%f"
timeStringIntegerSec = "%Y-%m-%dT%H-%M-%S"

#ListOfYears = []

def helloWorld(salut):
    print "hello world, ciao mondo", daysInMond[1], salut

def is_dst(dt=None, timezone="UTC"):
    if dt is None:
       dt = datetime.utcnow()
    timezone = pytz.timezone(timezone)
    timezone_aware_date = timezone.localize(dt, is_dst=None)
    return timezone_aware_date.tzinfo._dst.seconds != 0


def unixTimeFromUniversalTimeString(dateString, _format):
    __name__ = "unixTimeFromUniversalTimeString"
#    strip = time.gmtime(dateString,_format)
#    unixt = time.mktime(dt.datetime.strptime(dateString, _format).timetuple())
#    nformat = "{}Z".format(_format)
#    toby = dt.datetime.strptime(dateString, _format)
#    import timezone
#    unixt = dt.datetime.utcfromtimestamp(float(toby).strftime(_format)) #, dt.timezone.utc)
#    dtst=dateString.strftime(_format)
#    print __name__, dateString, _format, type(toby), toby
#    print unixt - t0
#    import dateutil
#    from dateutil.parser import *
#    print dateutil.parser.parse("2015-07-17 06:01:51.066141+00:00")
#    print dateutil.parser.parse("{}+00:00".format(dateString))
    unix_time= arrow.get("{}+00:00".format(dateString)).timestamp
#    print unix_time, unix_time - t0
    return unix_time

def unixTimeFromLocalTimeString(dateString, _format):
    __name__ = "unixTimeFromLocalTimeString"
    unixt = time.mktime(dt.datetime.strptime(dateString, _format).timetuple())
#    print __name__, dateString, _format, unixt
#    print unixt - t0
    return unixt
#    unix_time= arrow.get(dateString).timestamp
#    print unix_time, unix_time - t0


# I need this routine to extract pairs of unix time-stamps and return them
# as a second arguments in the form [ [t1, t2], ...[t1,t2] ]
# Of course when there is a clear initial date and final day without gaps
# in the middle the above list of lists should contain only one pair of
# unix times
def getListOfDates(dateString, verbose=False, **xargs):
    __name__ = "getListOfDates"
    """
    get the list of dates in a valid date-string
    All times are in UTC
    The dateString can take several formats
    interval=1day will be assumed as default if the extra argument is not
    given
    """
    interval = "1day"
    separator = "-"  # the alternative is to use '/' for paths
    unixTS = []
    if xargs:
        argos = {}
        for a in xargs.keys():
            argos[a.lower()] = xargs[a]
        if 'interval' in argos:
           interval = argos['interval']
        if 'separator' in argos:
           separator = argos['separator']

    intValue = "1"
    intUnit = "day"
    for unit in timeUnits:
        if unit in interval:
            intValue = interval.replace(unit,"")
            intUnit = unit.lower()
            break
#    print dateString, interval, intValue, intUnit, separator

    # time to decide what to do with the string based on its content

    listofdates = []
    if "@" in dateString:
        listofdates, unixTS = _segmentedDates(dateString, separator)
#        unixTS.append(uts)
#        print "FromSeg: ", listofdates, unixTS
#        for ld in listofdates:
#            xstring = '{:s}:{:s}'.format(ld, ld)
#            print "LD: ", ld, xstring
#            junk, uts = _datesInterval(xstring, separator)
#            unixTS.append(uts)
    elif ":" in dateString:
        listofdates, uts = _datesInterval(dateString, separator, verbose)
        if verbose:
            print __name__, "Found an interval:", uts
        unixTS.append(uts)
    elif "," in dateString:   # user provided list
        if separator not in dateString:
            listofdates = dateString.replace("-", separator).split(",")
        else:
            listofdates = dateString.split(",")
        # Here, we have to go date by date looking for intervals
        for ld in listofdates:
            xstring = '{:s}:{:s}'.format(ld, ld)
            junk, uts = _datesInterval(xstring, separator)
            unixTS.append(uts)
    else:
        # We need to figure out whether the string contains a month, or a
        # day or a year
        parts = dateString.split("-")
        nParts = len(parts)
        print "String parts: ", parts, nParts
        jahre = parts[0]
        dom = [x for x in daysInMond]
        if isLeap(jahre):
            dom[2] = 29
        else:
            dom[2] = 28
        if nParts == 1:
#            xstring = '{:s}:{:s}'.format(dateString, dateString)
            day1 = "{:s}-01-01".format(dateString)
            dayLast = "{:s}-12-31".format(dateString)
            xstring = '{:s}:{:s}'.format(day1, dayLast)
        elif nParts == 2:
            day1 = "{:s}-01".format(dateString)
            dayLast = "{:s}-{:02d}".format(dateString, dom[int(parts[1])] )
            xstring = '{:s}:{:s}'.format(day1, dayLast)
        elif nParts == 3:
            xstring = '{:s}:{:s}'.format(dateString, dateString)
#        listofdates = _fromSingleDate(dateString, separator)
        listofdates, uts = _datesInterval(xstring, separator)
        unixTS.append(uts)

    # At this point, we examine what is the interval and decide what to
    # return, and produce whatever needs to be returned

    if "day" in intUnit:
        return listofdates, unixTS
    elif "doy" in intUnit:
        # first, extract the years from the listofdates. We don't want to
        # be evaluating 365 times whether a year is leap or not, we just
        # want to do it once
        years = {}
        for d in listofdates:
            year_, month_, day_ = d.split(separator)
            yy = int(year_)
            years[yy] = 1
        
        loy = []
        for k in sorted(years):
            loy.append(k)
#        print "List of years 1: ", loy
#        print "List of years 2: ", ListOfYears
        premierJour = {}
        for y in loy:
            dom = daysInMond
            if isLeap(y):
                dom[2] = 29
            else:
                dom[2] = 28

            firstDay = [None] * 15
            fd = 0
            firstDay[1] = 0
            ym = y * 100 + 1
            premierJour[ym] = 0
            for m in range(2,13):
                fd += dom[m-1]
                firstDay[m] = fd
                ym = y * 100 + m
                premierJour[ym] = fd

#                print "Year: ", y, "m: ", m, "fdom: ", firstDay[m]

#        print "First day: ", premierJour
        lofdoy = []
        for d in listofdates:
            year_, month_, day_ = d.split(separator)
            yy = int(year_)
            mm = int(month_)
            ym = yy * 100 + mm
            doyval = premierJour[ym] + int(day_)
            cudate = "{:s}{:s}{:03d}".format(year_, separator, doyval)
            lofdoy.append(cudate)
            
        return lofdoy, unixTS

    elif "month" in intUnit:
        months = {}
        for d in listofdates:
            year_, month_, day_ = d.split(separator)
            ym = "{:s}{:s}{:s}".format(year_, separator, month_)
            months[ym] = 1
        
        lom = []
        for k in sorted(months):
            lom.append(k)
        return lom, unixTS

    elif "year" in intUnit:
        years = {}
        for d in listofdates:
            year_, month_, day_ = d.split(separator)
            yy = int(year_)
            years[yy] = 1
        
        loy = []
        for k in sorted(years):
            loy.append(k)
        return loy, unixTS

    elif "hour" in intUnit:
        dt = int(intValue)
        inHours = []
        for d in listofdates:
            for h in range(0,24,dt):
                hh = "{:s}T{:02d}:00:00".format( d, h)
                hh = "{:s}T{:02d}0000".format( d, h)
                inHours.append(hh)

        return inHours, unixTS

    elif "minute" in intUnit:
        dt = int(intValue)
        inMinutes = []
        for d in listofdates:
            for m in range(0,1440,dt):
                hh = int(m/60)
                mm = int( m % 60 )
#                print "types: ", type(hh), type(mm)
#                hh = "{:s}T{:02d}:{:02d}:00".format( d, hh, mm)
                haha = "{:s}T{:02d}{:02d}00".format( d, hh, mm)
                inMinutes.append(haha)

        return inMinutes, unixTS

    elif "second" in intUnit:
        dt = int(intValue)
        inHours = []
        for d in listofdates:
            for h in range(0,24,dt):
                hh = "{:s}T{:02d}:00:00".format( d, h)
                hh = "{:s}T{:02d}0000".format( d, h)
                inHours.append(hh)

        return inHours, unixTS

def _segmentedDates(ds, sep):
    """
    picks all days of one or more months from one or more years
    the @ symbol separates the list of months from the list of years
    if months or years are separated by commas, they are interpreted as a list.
    if months or years are separated by dash, they are interpreted as a range.
    """
    months, years = ds.split("@");
#    print "Months: ", months
#    print "Years: ", years
    lmonths = []
    lyears = []
    unixTS = []
    if "-" in months:  # we have an interval
        m1, m2 = months.split("-")
        lmonths = range(int(m1), int(m2)+1)
    elif "," in months:
        lmonths = months.split(",")
    else:
        lmonths.append(months)
        
#    print "list of months: ", lmonths

    if "-" in years:  # we have an interval
        y1, y2 = years.split("-")
        lyears = range(int(y1), int(y2)+1)
    elif "," in years:
        lyears = years.split(",")
    else:
        lyears.append(years)
        
    lod = []
#    print "list of years: ", lyears
    for y in lyears:
        iy = int(y)
#        ListOfYears.append(y)
        for m in lmonths:
            im = int(m)
            date = '{:d}-{:02d}'.format(iy, im)
#            print "extracting: ", date
            fullMonth = _datesBetween(date, date, sep)
#            print "FullMonth", fullMonth
            lod.extend(fullMonth[0])
            unixTS.append(fullMonth[1])

#    print "UNXTS: ", unixTS
    intime = unixTS[0][0]
    ftime = unixTS[0][1]
    nint = len(unixTS)
    uts = []
    for i in range(1,nint):
        interval = unixTS[i]
#        print "INTERVALUM: ", interval, ftime, interval[0] - ftime
        if (interval[0] - ftime) < 2.:
            ftime = interval[1]
        else:
            uts.append([intime, ftime])
            intime=interval[0]
            ftime = interval[1]
    uts.append([intime, ftime])
    return lod, uts

def _datesInterval(ds, separator, verbose=False):
    __name__ = "_datesInterval"
    """
    assumes the data has the form: firstDate:lastDate
    """
    try:
        fdate,ldate = ds.split(":")
    except:
        msg = """Date intervals should be specified as: date1:date2
One colon (:) only.

date1 or date2 should be of the form:
  yyyy-mm-dd or
  yyyy-mm-ddTHH-MM-SS (note the 'T' to separate date from time) or
  UNIX_timestamp
"""
        print msg
        print "You entered:\n\t\t", ds
        print "Fix this and try again"
        sys.exit()
#    print "First date: ", fdate
#    print "Last date: " , ldate
    results = _datesBetween(fdate, ldate, separator, verbose)
#    print "RESULTS: ", results
#    return _datesBetween(fdate, ldate, separator) 
    return results


def _datesBetween(fd, ld, sep, verbose=False):
    """
    given first date and last date, get all dates in between
    """
    __name__ = "_datesBetween"
#    print "DB: ", fd, ld
    lod = []
    uts = []
    if 'T' in fd:
        laDate, leTemp = fd.split("T")
    else:
        laDate = fd
        leTemp = "00-00-00"
    firstString = "{}T{}".format(laDate, leTemp)
    fdc = laDate.split("-")
    lfd = len(fdc)
    fyear = int(fdc[0])
    if fyear < 10000:
        fday = 1
        fmonth = 1
        if lfd == 3:
            fday = int(fdc[2])
            fmonth = int(fdc[1])
        elif lfd == 2:
            fmonth = int(fdc[1])
        # in principle, this should be enough to define the UNIX time stamp in
        # GMT
        th, tm, ts = leTemp.split('-')
        hh = int(th)
        mm = int(tm)
        ss = int(ts)
        isdst = 0
        if(fday > daysInMond[fmonth]):
            fday -= 1
        if verbose:
            print __name__, "for first date: ", fdc, lfd, fyear, fmonth, fday
        utc1a = time.mktime([fyear, fmonth, fday, hh, mm, ss, 1, 1, isdst] )
        utc1 = unixTimeFromLocalTimeString(firstString, timeStringIntegerSec)
        if verbose:
            print __name__, "firstUnixTime: ", utc1a, utc1
    else:
        # we have a unix time stamp...
        utc1 = float(fdc[0])
        # let's get the year, month and day of it
        gmt = time.gmtime(utc1)
        fyear = gmt.tm_year
        fmonth = gmt.tm_mon
        fday = gmt.tm_mday
#        print "UTC/GMT-1: ", utc1,  gmt
#        sys.exit()


    fstMonth = {}
    lstMonth = {}
    fstMonth[fyear] = fmonth
    fstMonth[fyear*100 + fmonth] = fday

    if 'T' in ld:
        laDate, leTemp = ld.split("T")
    else:
        laDate = ld
        leTemp = "23-59-59"   # The last minute of the day
    ldc = laDate.split("-")
#    ldc = ld.split("-")
    lld = len(ldc)
    lyear = int(ldc[0])
    if lyear < 10000:
        lday = 31
        lmonth = 12
        if lld == 3:
            lday = int(ldc[2])
            lmonth = int(ldc[1])
        elif lld == 2:
            lmonth = int(ldc[1])
            lday = _daysInMonth(lmonth, lyear)
        th, tm, ts = leTemp.split('-')
        hh = int(th)
        mm = int(tm)
        ss = int(ts)
        # this definition assumes (wrongly) that the date is in UTC, when
        # in the vast majority of cases, it shall be Local Time
        if(lday > daysInMond[lmonth]):
            lday -= 1
        utc2a = time.mktime([lyear, lmonth, lday, hh, mm, ss, 1, 1, isdst] )
        lastString = "{}T{}".format(laDate, leTemp)
        if verbose:
            print __name__, "for last date: ", ldc, lld, lyear, lmonth, lday, utc2a
        utc2 = unixTimeFromLocalTimeString(lastString, timeStringIntegerSec)
        if verbose:
            print __name__, "lastUnixTime: ", utc2a, utc2
    else:
        # we have a unix time stamp...
        utc2 = float(ldc[0])
        # let's get the year, month and day of it
        gmt = time.gmtime(utc2)
        lyear = gmt.tm_year
        lmonth = gmt.tm_mon
        lday = gmt.tm_mday
#        print "UTC/GMT-2: ", utc2,  gmt
        
    lstMonth[lyear] = lmonth
    lstMonth[lyear*100 + lmonth] = lday
#    print "for last date: ", ldc, lld, lyear, lmonth, lday
    dom = daysInMond
    imond = 1
    iday = 1
#    print "type of sep: ", type(sep)
    for jahre in range(fyear, lyear+1):
#        ListOfYears.append(jahre)
#        print "type of jahre: ", type(jahre)
        leap = ""
        if isLeap(jahre):
            leap = "Leap year"
            dom[2] = 29
        else:
            dom[2] = 28

#        print "Year: ", jahre, dom[2], leap
        if jahre in fstMonth.keys():
            fmon = fstMonth[jahre]
        else:
            fmon = 1;

        if jahre in lstMonth.keys():
            lmon = lstMonth[jahre]
        else:
            lmon = 12;
        for mond in range(fmon, lmon+1):
            imond = '{:02d}'.format(mond)
#            print "Type(imond) = ", type(imond)
            ymcombo = jahre*100 + mond
#            print "Year/Mond: ", jahre, mond, ymcombo
            if ymcombo in fstMonth:
                fday = fstMonth[ymcombo]
            else:
                fday = 1
            if ymcombo in lstMonth:
                lday = lstMonth[ymcombo]
            else:
                lday = dom[mond]
            
            for tag in range(fday, lday+1):
                iday = '{:02d}'.format(tag)
#                print "Type(iday) = ", type(iday)
#                laDat = '{:d}'.format(jahre)
#                laDat = '{:d}{:s}'.format(jahre, sep)
#                laDat = '{:d}{:s}{:s}'.format(jahre, sep, imond)
#                laDat = '{:d}{:s}{:s}{:s}'.format(jahre, sep, imond, sep)
                laDat = '{:d}{:s}{:s}{:s}{:s}'.format(jahre, sep, imond, sep, iday)
#                print "Y/M/D", jahre, sep, imond, sep, iday
#                print "Y/M/D", laDat
                lod.append(laDat)

#    print __name__, fd, ld, utc1, utc2
    uts.extend([utc1, utc2])
    return lod, uts


def _daysInMonth(month, year):
    """
        This routine takes care of the presence of leap years
    """
    if month == 2 and isLeap(year):
        return 29
    else:
        return daysInMond[month]


#
# This routine is available to general usage as it may be useful for some
def isLeap(year):
    iyear = int(year)
    if (iyear%4 == 0) and ( (iyear%100 != 0) or (iyear%400 == 0) ):
        return True
    else:
        return False






# the code below is not my own, it belongs to Matt Davis

"""
Functions for converting dates to/from JD and MJD. Assumes dates are historical
dates, including the transition from the Julian calendar to the Gregorian
calendar in 1582. No support for proleptic Gregorian/Julian calendars.

:Author: Matt Davis
:Website: http://github.com/jiffyclub

"""


# Note: The Python datetime module assumes an infinitely valid Gregorian
#       calendar.  The Gregorian calendar took effect after 10-15-1582 and the
#       dates 10-05 through 10-14-1582 never occurred. Python datetime objects
#       will produce incorrect time deltas if one date is from before 10-15-1582.

def mjd_to_jd(mjd):
    """
    Convert Modified Julian Day to Julian Day.
        
    Parameters
    ----------
    mjd : float
        Modified Julian Day
        
    Returns
    -------
    jd : float
        Julian Day
    
        
    """
    return mjd + 2400000.5

    
def jd_to_mjd(jd):
    """
    Convert Julian Day to Modified Julian Day
    
    Parameters
    ----------
    jd : float
        Julian Day
        
    Returns
    -------
    mjd : float
        Modified Julian Day
    
    """
    return jd - 2400000.5

    
def date_to_jd(year,month,day):
    """
    Convert a date to Julian Day.
    
    Algorithm from 'Practical Astronomy with your Calculator or Spreadsheet', 
        4th ed., Duffet-Smith and Zwart, 2011.
    
    Parameters
    ----------
    year : int
        Year as integer. Years preceding 1 A.D. should be 0 or negative.
        The year before 1 A.D. is 0, 10 B.C. is year -9.
        
    month : int
        Month as integer, Jan = 1, Feb. = 2, etc.
    
    day : float
        Day, may contain fractional part.
    
    Returns
    -------
    jd : float
        Julian Day
        
    Examples
    --------
    Convert 6 a.m., February 17, 1985 to Julian Day
    
    >>> date_to_jd(1985,2,17.25)
    2446113.75
    
    """
    if month == 1 or month == 2:
        yearp = year - 1
        monthp = month + 12
    else:
        yearp = year
        monthp = month
    
    # this checks where we are in relation to October 15, 1582, the beginning
    # of the Gregorian calendar.
    if ((year < 1582) or
        (year == 1582 and month < 10) or
        (year == 1582 and month == 10 and day < 15)):
        # before start of Gregorian calendar
        B = 0
    else:
        # after start of Gregorian calendar
        A = math.trunc(yearp / 100.)
        B = 2 - A + math.trunc(A / 4.)
        
    if yearp < 0:
        C = math.trunc((365.25 * yearp) - 0.75)
    else:
        C = math.trunc(365.25 * yearp)
        
    D = math.trunc(30.6001 * (monthp + 1))
    
    jd = B + C + D + day + 1720994.5
    
    return jd
    
    
def jd_to_date(jd):
    """
    Convert Julian Day to date.
    
    Algorithm from 'Practical Astronomy with your Calculator or Spreadsheet', 
        4th ed., Duffet-Smith and Zwart, 2011.
    
    Parameters
    ----------
    jd : float
        Julian Day
        
    Returns
    -------
    year : int
        Year as integer. Years preceding 1 A.D. should be 0 or negative.
        The year before 1 A.D. is 0, 10 B.C. is year -9.
        
    month : int
        Month as integer, Jan = 1, Feb. = 2, etc.
    
    day : float
        Day, may contain fractional part.
        
    Examples
    --------
    Convert Julian Day 2446113.75 to year, month, and day.
    
    >>> jd_to_date(2446113.75)
    (1985, 2, 17.25)
    
    """
    jd = jd + 0.5
    
    F, I = math.modf(jd)
    I = int(I)
    
    A = math.trunc((I - 1867216.25)/36524.25)
    
    if I > 2299160:
        B = I + 1 + A - math.trunc(A / 4.)
    else:
        B = I
        
    C = B + 1524
    
    D = math.trunc((C - 122.1) / 365.25)
    
    E = math.trunc(365.25 * D)
    
    G = math.trunc((C - E) / 30.6001)
    
    day = C - E + F - math.trunc(30.6001 * G)
    
    if G < 13.5:
        month = G - 1
    else:
        month = G - 13
        
    if month > 2.5:
        year = D - 4716
    else:
        year = D - 4715
        
    return year, month, day
    
    
def hmsm_to_days(hour=0,min=0,sec=0,micro=0):
    """
    Convert hours, minutes, seconds, and microseconds to fractional days.
    
    Parameters
    ----------
    hour : int, optional
        Hour number. Defaults to 0.
    
    min : int, optional
        Minute number. Defaults to 0.
    
    sec : int, optional
        Second number. Defaults to 0.
    
    micro : int, optional
        Microsecond number. Defaults to 0.
        
    Returns
    -------
    days : float
        Fractional days.
        
    Examples
    --------
    >>> hmsm_to_days(hour=6)
    0.25
    
    """
    days = sec + (micro / 1.e6)
    
    days = min + (days / 60.)
    
    days = hour + (days / 60.)
    
    return days / 24.
    
    
def days_to_hmsm(days):
    """
    Convert fractional days to hours, minutes, seconds, and microseconds.
    Precision beyond microseconds is rounded to the nearest microsecond.
    
    Parameters
    ----------
    days : float
        A fractional number of days. Must be less than 1.
        
    Returns
    -------
    hour : int
        Hour number.
    
    min : int
        Minute number.
    
    sec : int
        Second number.
    
    micro : int
        Microsecond number.
        
    Raises
    ------
    ValueError
        If `days` is >= 1.
        
    Examples
    --------
    >>> days_to_hmsm(0.1)
    (2, 24, 0, 0)
    
    """
    hours = days * 24.
    hours, hour = math.modf(hours)
    
    mins = hours * 60.
    mins, min = math.modf(mins)
    
    secs = mins * 60.
    secs, sec = math.modf(secs)
    
    micro = round(secs * 1.e6)
    
    return int(hour), int(min), int(sec), int(micro)
    

def datetime_to_jd(date):
    """
    Convert a `datetime.datetime` object to Julian Day.
    
    Parameters
    ----------
    date : `datetime.datetime` instance
    
    Returns
    -------
    jd : float
        Julian day.
        
    Examples
    --------
    >>> d = datetime.datetime(1985,2,17,6)  
    >>> d
    datetime.datetime(1985, 2, 17, 6, 0)
    >>> jdutil.datetime_to_jd(d)
    2446113.75
    
    """
    days = date.day + hmsm_to_days(date.hour,date.minute,date.second,date.microsecond)
    
    return date_to_jd(date.year,date.month,days)
    
    
def jd_to_datetime(jd):
    """
    Convert a Julian Day to an `jdutil.datetime` object.
    
    Parameters
    ----------
    jd : float
        Julian day.
        
    Returns
    -------
    dt : `jdutil.datetime` object
        `jdutil.datetime` equivalent of Julian day.
    
    Examples
    --------
    >>> jd_to_datetime(2446113.75)
    datetime(1985, 2, 17, 6, 0)
    
    """
    year, month, day = jd_to_date(jd)
    
    frac_days,day = math.modf(day)
    day = int(day)
    
    hour,min,sec,micro = days_to_hmsm(frac_days)
    
    return datetime(year,month,day,hour,min,sec,micro)


def timedelta_to_days(td):
    """
    Convert a `datetime.timedelta` object to a total number of days.
    
    Parameters
    ----------
    td : `datetime.timedelta` instance
    
    Returns
    -------
    days : float
        Total number of days in the `datetime.timedelta` object.
        
    Examples
    --------
    >>> td = datetime.timedelta(4.5)
    >>> td
    datetime.timedelta(4, 43200)
    >>> timedelta_to_days(td)
    4.5
    
    """
    seconds_in_day = 24. * 3600.
    
    days = td.days + (td.seconds + (td.microseconds * 10.e6)) / seconds_in_day
    
    return days
    
    
class datetime(dt.datetime):
    """
    A subclass of `datetime.datetime` that performs math operations by first
    converting to Julian Day, then back to a `jdutil.datetime` object.
    
    Addition works with `datetime.timedelta` objects, subtraction works with
    `datetime.timedelta`, `datetime.datetime`, and `jdutil.datetime` objects.
    Not all combinations work in all directions, e.g.
    `timedelta - datetime` is meaningless.
    
    See Also
    --------
    datetime.datetime : Parent class.
    
    """
    def __add__(self,other):
        if not isinstance(other,dt.timedelta):
            s = "jdutil.datetime supports '+' only with datetime.timedelta"
            raise TypeError(s)
        
        days = timedelta_to_days(other)
        
        combined = datetime_to_jd(self) + days
        
        return jd_to_datetime(combined)
        
    def __radd__(self,other):
        if not isinstance(other,dt.timedelta):
            s = "jdutil.datetime supports '+' only with datetime.timedelta"
            raise TypeError(s)
        
        days = timedelta_to_days(other)
        
        combined = datetime_to_jd(self) + days
        
        return jd_to_datetime(combined)
        
    def __sub__(self,other):
        if isinstance(other,dt.timedelta):
            days = timedelta_to_days(other)
            
            combined = datetime_to_jd(self) - days
            
            return jd_to_datetime(combined)
            
        elif isinstance(other, (datetime,dt.datetime)):
            diff = datetime_to_jd(self) - datetime_to_jd(other)
            
            return dt.timedelta(diff)
            
        else:
            s = "jdutil.datetime supports '-' with: "
            s += "datetime.timedelta, jdutil.datetime and datetime.datetime"
            raise TypeError(s)
            
    def __rsub__(self,other):
        if not isinstance(other, (datetime,dt.datetime)):
            s = "jdutil.datetime supports '-' with: "
            s += "jdutil.datetime and datetime.datetime"
            raise TypeError(s)
            
        diff = datetime_to_jd(other) - datetime_to_jd(self)
            
        return dt.timedelta(diff)
        
    def to_jd(self):
        """
        Return the date converted to Julian Day.
        
        """
        return datetime_to_jd(self)
        
    def to_mjd(self):
        """
        Return the date converted to Modified Julian Day.
        
        """
        return jd_to_mjd(self.to_jd())
    
