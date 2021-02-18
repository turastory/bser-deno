import os
from crawl_utils import *
from upload_utils import getCollection
import pymongo
from date_utils import *
import gc


def parseRow(row):
    return [x.text for x in row('td')]


def extractContents(contents):
    def get(items):
        return {
            "winRate": round(float(items[0].strip('%')) / 100, 3),
            "pickRate": round(float(items[1].strip('%')) / 100, 3),
            "avgKill": float(items[2]),
            "avgRank": float(items[3])
        }

    return [
        get(contents[:4]),
        get(contents[4:8]),
        get(contents[8:12])
    ]


def isEnd(row):
    return not row[1] and not row[2]


class Stats:
    uri = "https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vTYndan9I6ZAVdyrZL0mN7346NsdGCgDoC1jOUnzRzDtApBXeqdlN46S_lQKcHQwDV_sO6blm-2qnHO/pubhtml/sheet?headers=false&gid=1074509683"
    htmlfile = "out/stats/data.html"
    jsonfile = "out/stats/data.json"
    col = getCollection("stats")

    def read(self):
        print(f"Start getting stats data from [{self.uri}]")
        read(self.uri, self.htmlfile)

    def shouldUpdate(self, currentUpdated):
        lastData = self.col.find_one(
            {},
            ['updated'],
            sort=[('updated', pymongo.DESCENDING)]
        )
        if lastData == None:
            return True
        return isNew(lastData['updated'], currentUpdated)

    def write(self, data):
        write_file(self.jsonfile, toJson(data))

    def upload(self, data):
        self.col.insert_one(data)

    def parseInternal(self, rows, idx):
        result = {}
        result['solo'] = {}
        result['duo'] = {}
        result['squad'] = {}
        result['solo']['builds'] = []
        result['duo']['builds'] = []
        result['squad']['builds'] = []

        # Get average data
        if rows[idx][2] == '':
            avgRow = rows[idx][3:]
        else:
            avgRow = rows[idx][2:]
        averageData = extractContents(avgRow)
        result['solo']['average'] = averageData[0]
        result['duo']['average'] = averageData[1]
        result['squad']['average'] = averageData[2]
        idx += 1

        # Get data
        character = ""
        builds = []
        while True:
            row = rows[idx]
            if isEnd(row):
                break

            if row[1]:
                # new character
                character = toSnake(row[1].lower())
            weapon = toSnake(row[2].lower())
            info = extractContents(row[3:])
            base = {
                'character': codefix(character),
                'weapon': codefix(weapon),
            }
            build = base.copy()
            build['stat'] = info[0]
            result['solo']['builds'].append(build)
            build = base.copy()
            build['stat'] = info[1]
            result['duo']['builds'].append(build)
            build = base.copy()
            build['stat'] = info[2]
            result['squad']['builds'].append(build)
            idx += 1

        return result

    def parse(self):
        path = os.path.abspath(self.htmlfile)
        bsObject = resolve(f'file://{path}')

        # Locate table
        rows = bsObject.table.tbody('tr')
        parsedRows = list(map(parseRow, rows))

        # Update date
        updated = toEpoch(parsedRows[3][3])
        periods = parsedRows[4][3].split('~')
        periodStart = periods[0].strip()
        periodEnd = toEpoch(periods[-1].strip())
        # periodEnd = toEpoch(
        #     f"{periodStart.split(' ')[0]} {periods[1].strip()}")
        periodStart = toEpoch(periodStart)

        def findTop1000():
            for i, row in enumerate(parsedRows):
                if row[1] and row[1] == "Top Tiers":
                    return i + 3

        allResult = self.parseInternal(parsedRows, 9)
        top1000Result = self.parseInternal(parsedRows, findTop1000())

        data = {
            "updated": updated,
            "periodStart": periodStart,
            "periodEnd": periodEnd,
            "all": allResult,
            "top1000": top1000Result
        }

        return data


def run_stats():
    stats = Stats()

    # Read HTML
    stats.read()
    data = stats.parse()
    print(data)

    # Check if it needs an update
    if stats.shouldUpdate(data['updated']):
        stats.write(data)
        stats.upload(data)
        print("Data upload successful.")
    else:
        print("No need to update.")
