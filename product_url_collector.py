import asyncio
import datetime
from playwright.async_api import async_playwright


class product_url_collector:
    def __init__(self, product_name, pages=15, concurrency=4):
        self.product_name = product_name.strip()
        self.pages = pages
        self.concurrency = concurrency
        self.search_query = product_name.replace(" ", "%20")
        self.final_data = []

    async def _extract_links(self, browser, page_no):
        url = (
            f"https://www.flipkart.com/search?"
            f"q={self.search_query}"
            f"&otracker=search&otracker1=search"
            f"&marketplace=flipkart&as-show=on&as=off"
            f"&page={page_no}"
        )

        page = await browser.new_page()

        try:
            await page.goto(url)
            await page.wait_for_load_state("domcontentloaded")

            links = await page.evaluate("""
                () => {
                    const results = [];
                    document.querySelectorAll("a[href*='/p/']").forEach(a => {
                        if (a.href && !results.includes(a.href)) {
                            results.push(a.href);
                        }
                    });
                    return results;
                }
            """)

            return links

        finally:
            await page.close()

    async def _worker(self, browser, queue, results):
        while True:
            page_no = await queue.get()

            if page_no is None:
                queue.task_done()
                break

            try:
                links = await self._extract_links(browser, page_no)
                results.extend(links)
            finally:
                queue.task_done()

    async def run(self):
        start_time = datetime.datetime.now()
        print("started_at:", start_time.strftime("%Y-%m-%d %H:%M:%S"))

        queue = asyncio.Queue()
        results = []

        for page_no in range(1, self.pages + 1):
            queue.put_nowait(page_no)

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)

            workers = [
                asyncio.create_task(self._worker(browser, queue, results))
                for _ in range(self.concurrency)
            ]

            await queue.join()

            for _ in workers:
                queue.put_nowait(None)

            await asyncio.gather(*workers)

            await browser.close()

        self.final_data = list(set(results))

        print("total_links_found:", len(self.final_data))
        print("finished_at:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        return self.final_data
