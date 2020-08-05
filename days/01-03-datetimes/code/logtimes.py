from datetime import datetime
from datetime import timedelta
import os
import urllib.request

SHUTDOWN_EVENT = "Shutdown initiated"

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, "log")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/messages.log", logfile
)


with open(logfile) as f:
    loglines = f.readlines()


def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """

    # each line seems prefixed with "INFO", "WARNING " or "ERROR "
    # Find the first space and the timestamp is the next 19 chars
    fmt_string = "%Y-%m-%dT%H:%M:%S"
    string_len = 19
    start_char = line.find(" ") + 1
    date_string = line[start_char : start_char + string_len]
    return datetime.strptime(date_string, fmt_string)


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_events = []
    for line in loglines:
        if SHUTDOWN_EVENT in line:
            shutdown_events.append(line)

    if len(shutdown_events) < 2:
        return timedelta(days=0)
    else:
        return convert_to_datetime(shutdown_events[-1]) - convert_to_datetime(
            shutdown_events[0]
        )


if __name__ == "__main__":
    print(time_between_shutdowns(loglines))
