#
# ozsentials : timeMetrics
# Author: Patricio F. Ortiz
# Date:  May 15, 2019
#
# Version 1.0 
# Generic methods to do time tracing

import time

version = "1.0.0"


class methods(object):

    t1 = 0
    maxDaysToProcess = 23

    def __init__(self):
        """
            rice is eithher True or False and indicates whether a raise
            condition is thrown (True) or just messages are printed (False)
        """
        self.t0 = time.time()
        self.tLast = self.t0

    def start(self):
        """
            rice is eithher True or False and indicates whether a raise
            condition is thrown (True) or just messages are printed (False)
        """
        self.t0 = time.time()
        self.tLast = self.t0

    def click(self, name, msg, verbose):
        if verbose:
            self.now = time.time()
            print "{} CLICK {} {}[ms] {}[ms]".format(name, msg, (self.now - self.t0) * 1000., (self.now - self.tLast)*1000.)
            self.tLast = self.now

    def deltaT(self, name, msg, ref, verbose):
        if verbose:
            tnow = time.time()
            print "{} Delta-T {} {}[ms] ".format(name, msg, (tnow - ref)* 1000.)

