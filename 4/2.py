from datetime import datetime
from enum import Enum
import re


class Action(Enum):
    BEGIN_SHIFT = 1
    SLEEP = 2
    WAKEUP = 3


class Guard():
    def __init__(self, guard_id):
        self.guard_id = guard_id
        self.sleep_minutes = {}
        self.last_sleep_start = 0

    def fellAsleep(self, time):
        self.last_sleep_start = time

    def wokeUp(self, time):
        total_sleep_minutes = ((time - self.last_sleep_start).seconds // 60) % 60
        for i in range(self.last_sleep_start.minute, self.last_sleep_start.minute + total_sleep_minutes):
            if (not i in self.sleep_minutes.keys()):
                self.sleep_minutes[i] = 0
            self.sleep_minutes[i] += 1

    def getSleepMinutesTotal(self):
        total = 0
        if self.sleep_minutes:
            for minute in self.sleep_minutes.keys():
                total += self.sleep_minutes[minute]
        return total

    def getMostSleptAtMinute(self):
        minute_max = 0
        minute_max_count = 0
        for minute in self.sleep_minutes.keys():
            if self.sleep_minutes[minute] > minute_max_count:
                minute_max = minute
                minute_max_count = self.sleep_minutes[minute]
        return minute_max, minute_max_count


class LogBook():
    def __init__(self):
        self.entries = []
        self.guards = {}

    def addEntry(self, entry):
        self.entries.append(entry)

    def sortByTime(self):
        self.entries = sorted(self.entries, key=lambda r: r.time)

    def parseData(self):
        last_guard_id = None
        for entry in self.entries:
            if entry.guard_id == None:
                entry.guard_id = last_guard_id

            if not entry.guard_id in self.guards.keys():
                self.guards[entry.guard_id] = Guard(entry.guard_id)

            if entry.action == Action.SLEEP:
                self.guards[entry.guard_id].fellAsleep(entry.time)
            elif entry.action == Action.WAKEUP:
                self.guards[entry.guard_id].wokeUp(entry.time)

            last_guard_id = entry.guard_id

    def getSleepiestGuard(self):
        max_sleep = 0
        max_sleep_guard = None

        for i in self.guards:
            if self.guards[i].getSleepMinutesTotal() > max_sleep:
                max_sleep = self.guards[i].getSleepMinutesTotal()
                max_sleep_guard = self.guards[i]

        return max_sleep_guard

    def getGuardSleepingSameMinute(self):
        minute_max = 0
        minute_max_count = 0
        minute_max_guard = 0

        for i in self.guards:
            c_minute_max, c_minute_max_count = self.guards[i].getMostSleptAtMinute()
            if c_minute_max_count > minute_max_count:
                minute_max_count = c_minute_max_count
                minute_max_guard = self.guards[i]
                minute_max = c_minute_max

        return int(minute_max_guard.guard_id) * minute_max


class LogEntry():
    def __init__(self, data):
        self.data = data
        self.time = self.parseTime()
        self.action = None
        self.guard_id = None
        self.parseData()

    def parseTime(self):
        time_str = self.data.split("] ")[0].replace("[", "")
        return datetime.strptime(time_str, "%Y-%m-%d %H:%M")

    def parseData(self):
        data = self.data.split("] ")[1]

        if data == "falls asleep":
            self.action = Action.SLEEP
        elif data == "wakes up":
            self.action = Action.WAKEUP
        else:
            self.action = Action.BEGIN_SHIFT
            guard_match = re.match("Guard #(\d+) begins shift", data)
            if guard_match:
                self.guard_id = guard_match.groups()[0]


def main():
    logbook = LogBook()

    with open("input") as f:
        for line in f.readlines():
            logbook.addEntry(LogEntry(line.strip()))

    logbook.sortByTime()
    logbook.parseData()

    print(logbook.getGuardSleepingSameMinute())


if __name__ == '__main__':
    main()
