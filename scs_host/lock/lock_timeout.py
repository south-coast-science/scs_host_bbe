'''
Created on 12 Aug 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
'''


# --------------------------------------------------------------------------------------------------------------------

class LockTimeout(RuntimeError):
    '''
    classdocs
    '''

    def __init__(self, name, ident):
        '''
        Constructor
        '''
        self.__name = name
        self.__ident = ident


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def name(self):
        return self.__name


    @property
    def ident(self):
        return self.__ident


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "LockTimeout:{name:%s, ident:%s}" % (self.name, self.ident)
