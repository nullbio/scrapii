from datetime import datetime
import os
from typing import Tuple
import logging

# Local modules
from request import Request
import parse


class Category:
    def __init__(self, name: str, end_year: int):
        self.name = name
        self.end_year = end_year
        self.month_urls = self.get_month_urls()

    def get_month_urls(self):
        month_urls = []
        curr_yr = datetime.now().year
        curr_mnth = datetime.now().month
        yr = curr_yr
        while yr >= self.end_year:
            for mnth in range(12, 0, -1):
                if yr == curr_yr and mnth > curr_mnth:
                    continue

                # get last two digits of year
                setyr = int(str(yr)[-2:])
                month_urls.append(
                    f"https://arxiv.org/list/{self.name}/{setyr:02d}{mnth:02d}"
                )
            yr -= 1
        return month_urls


class Scrape:
    def __init__(
        self, request: Request, log: logging.Logger, download_dir: str
    ):
        self.request = request
        self.log = log
        self.download_dir = download_dir
        # Create a parser
        self.parse = parse.Parse(request, log)

        # Create the download directory if it doesn't exist
        os.makedirs(download_dir, exist_ok=True)

    # Get the total number of entries on a particular archive url page:
    # Example: https://arxiv.org/list/cs/1805 -> returns int(4158)
    def total_entries(self, url: str) -> int:
        r = self.request.get(url)
        return self.parse.total_entries(r.text)


class ArchivePage:
    def __init__(self, **kwargs):
        self.category = kwargs.get("category")
        self.archive_url = kwargs.get("url")
        self.total_entries = kwargs.get("total_entries")
        self.mm = kwargs.get("month")
        self.year = kwargs.get("year")
        self.collected_entries = 0
        self.last_updated_date = datetime.now()


class ArchivePapers:
    def __init__(self, **kwargs):
        return


# By appending ?skip=0&show=2000 we can get 2000 results
# per page at a time, where skip is the offset (exclusive)
# If we see <dl id="articles"><p>No updates for this
# time period.</p></dl> we know we've reached the end of the archive.
def scrape_archive_page(skip: int) -> Tuple[ArchivePage, ArchivePapers]:
    return ArchivePage(), ArchivePapers()