""" Provided by Darius"""


class time_romanian:
    """
    This class returns a given time as a range of LED-indices.
    Illuminating these LEDs represents the current time on a romanian WCA
    """

    def __init__(self):
        self.prefix = list(range(0,4)) +  list(range(6,9)) # -> ESTE ORA
        self.minutes=[[], \
            # -> SI CINCI
            list(range(97,99)) + list(range(99,104)), \
            # -> SI ZECE
            list(range(66,68)) + list(range(82,86)), \
            # -> SI UN SFERT
            list(range(66,68)) + list(range(86,88)) + list(range(105,110)), \
            # -> SI DOUAZECI
            list(range(66,68)) + list(range(88,96)), \
            # -> SI DOUAZECI SI CINCI
            list(range(66,68)) + list(range(88,96)) + list(range(97,99)) + list(range(99,104)), \
            # -> SI TREIZECI
            list(range(66,68)) + list(range(69,77)), \
            # -> FARA DOUAZECI SI CINCI
            list(range(77,81)) + list(range(88,96)) + list(range(97,99)) + list(range(99,104)), \
            # -> FARA DOUAZECI
            list(range(77,81)) + list(range(88,96)), \
            # -> FARA UN SFERT
            list(range(77,81)) + list(range(86,88)) + list(range(105,110)), \
            # -> FARA ZECE
            list(range(77,81)) + list(range(82,96)), \
            # -> FARA CINCI
            list(range(77,81)) + list(range(99,104)) ]
            # -> DOUA SPRE ZECE
        self.hours= [list(range(11,15)) + list(range(16,19)) + list(range(28,32)), \
            # -> UNU
            list(range(48,51)), \
            # -> DOUA
            list(range(11,15)), \
            # -> TREI
            list(range(51,55)), \
            # -> PATRU
            list(range(44,49)), \
            # -> CINCI
            list(range(50,65)), \
            # -> SASE
            list(range(40,44)), \
            # -> SAPTE
            list(range(55,60)), \
            # -> OPT
            list(range(37,40)), \
            # -> NOUA
            list(range(33,37)), \
            # -> ZECE
            list(range(28,32)),\
            # -> UNSPREZECE
            list(range(22,32)), \
            # -> DOUA SPRE ZECE
            list(range(11,15)) + list(range(16,19)) + list(range(28,32))]
        self.full_hour= list(range(0,0))

    def get_time(self, time, purist):
        hour=time.hour % 12+(1 if time.minute//5 >= 7 else 0)
        minute=time.minute//5
        # Assemble indices
        return  \
            (self.prefix if not purist else []) + \
            self.minutes[minute] + \
            self.hours[hour] + \
            (self.full_hour if (minute == 0) else [])
