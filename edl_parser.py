# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
import pycmx
from timecode import Timecode


def main(input):
    if os.path.exists(fn) is False:
        print("Files don't exist")
        exit()
    with open(input) as f:
        try:
            edl = pycmx.parse_cmx3600(f)
        except:
            print("File is impossible to parse")
            exit()
    print(list(edl.events))
    for clip in edl.events:
        tc = Timecode('24', clip.edits[0].record_in)
        tc2 = Timecode('24', clip.edits[0].record_out)
        print(clip.edits[0].clip_name, tc.frames, tc2.frames)

if __name__ == "__main__":
    fn = sys.argv[1]
    main(fn)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
