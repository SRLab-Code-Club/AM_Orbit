# -*- coding: utf-8 -*-
"""LMIO.py Litchi Mission I/O module
---
# Purpose
Read and write the Litchi mission in csv format.
---
# Main objects:
    * LMIO.LitchiWaypoint: Handle the information of each waypoint.
    * LMIO.LitchiMission: Collection of LMIO.LitchiWaypoint and some additional information about the mission.
---
Please write long docstring to describe the objects or methods. A good example is provide by [numpydoc](https://numpydoc.readthedocs.io/en/latest/example.html#example). 
"""
from pathlib import Path
import csv
from dataclasses import dataclass,field

@dataclass
class LitchiWaypoint():
    """ The Litchi Waypoint information.
    Methods
    -----
    self.fromCsvStr(csvString:str,delimiter:str=',') 分解 CSV 字串並填入對應的欄位中。
    self.asCsvStr(delimiter:str=',')->str 以 delimiter 指定之字元連結所有欄位並且輸出一個字串。
    """
    latitude:float=field(init=False)
    longitude:float=field(init=False)
    altitude:float=field(init=False) #(m),
    heading:float=field(init=False) #(deg),
    curvesize:float=field(init=False) #(m),
    rotationdir:int=field(init=False)
    gimbalmode:int=field(init=False)
    gimbalpitchangle:int=field(init=False)
    actiontype1:int=field(init=False)
    actionparam1:int=field(init=False)
    actiontype2:int=field(init=False)
    actionparam2:int=field(init=False)
    actiontype3:int=field(init=False)
    actionparam3:int=field(init=False)
    actiontype4:int=field(init=False)
    actionparam4:int=field(init=False)
    actiontype5:int=field(init=False)
    actionparam5:int=field(init=False)
    actiontype6:int=field(init=False)
    actionparam6:int=field(init=False)
    actiontype7:int=field(init=False)
    actionparam7:int=field(init=False)
    actiontype8:int=field(init=False)
    actionparam8:int=field(init=False)
    actiontype9:int=field(init=False)
    actionparam9:int=field(init=False)
    actiontype10:int=field(init=False)
    actionparam10:int=field(init=False)
    actiontype11:int=field(init=False)
    actionparam11:int=field(init=False)
    actiontype12:int=field(init=False)
    actionparam12:int=field(init=False)
    actiontype13:int=field(init=False)
    actionparam13:int=field(init=False)
    actiontype14:int=field(init=False)
    actionparam14:int=field(init=False)
    actiontype15:int=field(init=False)
    actionparam15:int=field(init=False)
    altitudemode:int=field(init=False) #0: above take-off, 1: above ground
    speed:float=field(init=False) #(m/s)
    poi_latitude:float=field(init=False)
    poi_longitude:float=field(init=False)
    poi_altitude:float=field(init=False) #(m)
    poi_altitudemode:int=field(init=False)
    photo_timeinterval:float=field(init=False)
    photo_distinterval:float =field(init=False)

    def fromCsvStr(self,csvString:str,delimiter:str=',')->None:
        """ Initialize this object from csv string.
        
        Parameters
        -----
        csvString:str 輸入的字串。
        delimiter:str=',' 字串分隔符號。

        Outputs
        -----
        """
        valuesFromStr:list = csvString.split(delimiter)
        # Check the length of data is correct
        if len(valuesFromStr) != 46:
            raise ValueError(f"The string shold contain 46 data fileds, {len(valuesFromStr)} are found. Check the input string again:\n{csvString}")
        # Fill in the values
        self.latitude:float = float(valuesFromStr[0])
        self.longitude:float = float(valuesFromStr[1])
        self.altitude:float = float(valuesFromStr[2]) #(m),
        self.heading:float = float(valuesFromStr[3]) #(deg),
        self.curvesize:float = float(valuesFromStr[4]) #(m),
        self.rotationdir:int = int(valuesFromStr[5])
        self.gimbalmode:int = int(valuesFromStr[6])
        self.gimbalpitchangle:int = int(valuesFromStr[7])
        self.actiontype1:int = int(valuesFromStr[8])
        self.actionparam1:int = int(valuesFromStr[9])
        self.actiontype2:int = int(valuesFromStr[10])
        self.actionparam2:int = int(valuesFromStr[11])
        self.actiontype3:int = int(valuesFromStr[12])
        self.actionparam3:int = int(valuesFromStr[13])
        self.actiontype4:int = int(valuesFromStr[14])
        self.actionparam4:int = int(valuesFromStr[15])
        self.actiontype5:int = int(valuesFromStr[16])
        self.actionparam5:int = int(valuesFromStr[17])
        self.actiontype6:int = int(valuesFromStr[18])
        self.actionparam6:int = int(valuesFromStr[19])
        self.actiontype7:int = int(valuesFromStr[20])
        self.actionparam7:int = int(valuesFromStr[21])
        self.actiontype8:int = int(valuesFromStr[22])
        self.actionparam8:int = int(valuesFromStr[23])
        self.actiontype9:int = int(valuesFromStr[24])
        self.actionparam9:int = int(valuesFromStr[25])
        self.actiontype10:int = int(valuesFromStr[26])
        self.actionparam10:int = int(valuesFromStr[27])
        self.actiontype11:int = int(valuesFromStr[28])
        self.actionparam11:int = int(valuesFromStr[29])
        self.actiontype12:int = int(valuesFromStr[30])
        self.actionparam12:int = int(valuesFromStr[31])
        self.actiontype13:int = int(valuesFromStr[32])
        self.actionparam13:int = int(valuesFromStr[33])
        self.actiontype14:int = int(valuesFromStr[34])
        self.actionparam14:int = int(valuesFromStr[35])
        self.actiontype15:int = int(valuesFromStr[36])
        self.actionparam15:int = int(valuesFromStr[37])
        self.altitudemode:int = int(valuesFromStr[38]) #0: above take-off, 1: above ground
        self.speed:float = float(valuesFromStr[39]) #(m/s)
        self.poi_latitude:float = float(valuesFromStr[40])
        self.poi_longitude:float = float(valuesFromStr[41])
        self.poi_altitude:float = float(valuesFromStr[42]) #(m)
        self.poi_altitudemode:int = int(valuesFromStr[43])
        self.photo_timeinterval:float = float(valuesFromStr[44])
        self.photo_distinterval:float  = float(valuesFromStr[45])

    def asCsvStr(self,delimiter:str=',')->str:
        """ Export the string to a csv format string.
        """
        return delimiter.join([str(self.latitude),str(self.longitude),str(self.altitude),str(self.heading),str(self.curvesize),str(self.rotationdir),str(self.gimbalmode),str(self.gimbalpitchangle),str(self.actiontype1),str(self.actionparam1),str(self.actiontype2),str(self.actionparam2),str(self.actiontype3),str(self.actionparam3),str(self.actiontype4),str(self.actionparam4),str(self.actiontype5),str(self.actionparam5),str(self.actiontype6),str(self.actionparam6),str(self.actiontype7),str(self.actionparam7),str(self.actiontype8),str(self.actionparam8),str(self.actiontype9),str(self.actionparam9),str(self.actiontype10),str(self.actionparam10),str(self.actiontype11),str(self.actionparam11),str(self.actiontype12),str(self.actionparam12),str(self.actiontype13),str(self.actionparam13),str(self.actiontype14),str(self.actionparam14),str(self.actiontype15),str(self.actionparam15),str(self.altitudemode),str(self.speed),str(self.poi_latitude),str(self.poi_longitude),str(self.poi_altitude),str(self.poi_altitudemode),str(self.photo_timeinterval),str(self.photo_distinterval)])