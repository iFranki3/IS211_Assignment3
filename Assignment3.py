import argparse
import urllib.request
import datetime
import csv
import re


def downloadData(url):
    """Downloads the data"""
    with urllib.request.urlopen(url) as response:
        web_data = response.read().decode('utf-8')

    return web_data


def main(url):
    """
    Main function

    :param url:
    :return:
    """
    print(f"Running main with URL = {url}...")

    data = downloadData(url)

    data_lines = data.split("\n")

    browser_count = {
        'FIREFOX': 0,
        'MSIE': 0,
        'SAFARI': 0,
        'CHROME': 0
    }
    image_counter = 0
    for row in csv.reader(data_lines):
        if len(row) == 0:
            continue
        url_hit, timestamp_str, browser, status_code, hit_size = row
        url_hit = url_hit.upper()
        if re.search("PNG|GIF|JPG|JPEG", url_hit.upper()):
            image_counter += 1

        if browser.upper().find("FIREFOX") != -1:
            browser_count['FIREFOX'] += 1
        elif browser.upper().find("MSIE") != -1:
            browser_count['MSIE'] =+ 1
        elif browser.upper().find("SAFARI") != -1:
            browser_count['SAFARI'] =+ 1
        elif browser.upper().find("CHROME") != -1:
            browser_count['CHROME'] =+ 1
        timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        print(row)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)