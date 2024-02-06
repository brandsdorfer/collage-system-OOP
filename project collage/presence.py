from datetime import datetime

class Presence():

    ENTRY = "entry"
    EXIT = "exit"

    def __init__(self):

        # the system is bilding for a week, in case that w'll bilt it for real w'll base on a outer DB
        self._presence_DB = {"Sunday":{Presence.ENTRY:None, Presence.EXIT:None},
                        "Monday":{Presence.ENTRY:None, Presence.EXIT:None},
                        "Tuesday":{Presence.ENTRY:None, Presence.EXIT:None},
                        "Wednesday":{Presence.ENTRY:None, Presence.EXIT:None},
                        "Thursday":{Presence.ENTRY:None, Presence.EXIT:None},
                        "Friday":{Presence.ENTRY:None, Presence.EXIT:None},
                        "Saturday":{Presence.ENTRY:None, Presence.EXIT:None},}
        
    def update_entry_exit(self, entry_or_exit):
        time = datetime.now()
        today_in_week = time.strftime("%A")
        if self._presence_DB[today_in_week][entry_or_exit] == None:
            self._presence_DB[today_in_week][entry_or_exit] = time.strftime("%H:%M:%S")
        else:
            return "there is already clicked for entry or exit"

    def entry(self):
        self.update_entry_exit(Presence.ENTRY)

    def exit(self):
        self.update_entry_exit(Presence.EXIT)

    def get_presence_per_day(self, day):
        return self._presence_DB[day]
    
    def set_presence_time(self, day, time, entry_or_exit):
        # need to check validation!!!!
        self._presence_DB[day][entry_or_exit] = time
    
    def convert_time_to_seconds(self, time_str):
        #this  function dont checks validetuon
        seconds = int(time_str[6:])
        minute_in_sec = seconds + int(time_str[3:5]) * 60
        hours_in_sec = minute_in_sec + int(time_str[:2]) * 60 * 60
        return hours_in_sec
    
    def convert_seconds_to_time(self, seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return (hour, minutes, seconds)
    
    def get_total_hours_per_day(self, day):
            
        try:
            entry_time = self.convert_time_to_seconds(self._presence_DB[day][Presence.ENTRY])
            exit_time = self.convert_time_to_seconds(self._presence_DB[day][Presence.EXIT])
            presence_time_in_seconds = exit_time - entry_time
            if entry_time and exit_time != None:
                h = self.convert_seconds_to_time(presence_time_in_seconds)
                return ("in %s is the presence time: %d hours, %d minute, %d seconds")%(day, h[0], h[1], h[2])
            
        except Exception:
            return "an entry time or an exit time is nuccecery"


    def update(self):
        today = str(datetime.now().strftime("%A"))

        while  True:
            k = input("""
                      to update entry press 1
                      to exit press 2
                      to see the presence time press 3
                      to get out of the system press 4:\n""")
            if k == "1":
                self.entry()

            elif k == "2":
                self.exit()

            elif k == "3":
                print(self.get_presence_per_day(today))
                print("total time:",self.get_total_hours_per_day(today))

            elif k == "4":
                return
            
            else:
                print("enter a valid comend")
