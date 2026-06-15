import json
import time
import requests
import asyncio
from product_url_collector import product_url_collector


class review_processor:
    def __init__(
        self,
        product_name,
        review_limit=900,
        hash_file="hashmap2.json",
        review_file="all_reviews2.json",
        sleep_time=5,
            alpha=8,
            page=10
    ):
        self.page=page
        self.product_name = product_name
        self.review_limit = review_limit

        self.hash_file = hash_file
        self.review_file = review_file
        self.sleep_time = sleep_time

        self.hashmap = self._load_json(self.hash_file)
        self.all_reviews = self._load_json(self.review_file)
        self.alpha=alpha

        self.all_urls = []

    async def get_all_urls(self):
        collector = product_url_collector(
            product_name=self.product_name,
            pages=self.page,
            concurrency=3
        )
        return await collector.run()

    async def init_urls(self):
        self.all_urls = await self.get_all_urls()

    def extract_pid(self, url):
        return url.split("pid=")[1].split("&")[0]

    def _load_json(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_json(self, filename, data):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def run(self):
        for idx, url in enumerate(self.all_urls):
            pid = None

            try:
                pid = self.extract_pid(url)

                print(f"\n[{idx}/{len(self.all_urls)}] {self.product_name} → {pid}")

                self.hashmap[pid] = {
                    "link": url,
                    "product": self.product_name
                }
                self._save_json(self.hash_file, self.hashmap)

                if pid in self.all_reviews:
                    print(f"Skipping {pid}")
                    continue

                api = (
                    f"http://127.0.0.1:8001/reviews"
                    f"?url={url}"
                    f"&const_alpha={self.alpha}"
                    f"&limit={self.review_limit}"
                    f"&product={self.product_name}"
                )

                print("Calling API...")

                response = requests.get(api, timeout=None)
                response.raise_for_status()

                data = response.json()

                t = data.get("time")
                s = data.get("speed")

                if t:
                    del data["time"]

                if s:
                    del data["speed"]

                self.all_reviews[pid] = {
                    "status": "success",
                    "link": url,
                    "product": self.product_name,
                    "data": data
                }
                try:
                    print(f'time : {t}\nspeed : {s}\nquantity',data['count'])

                except:
                    print('error agaya')
                    pass


                self._save_json(self.review_file, self.all_reviews)

                print(f"Saved {pid}")

            except Exception as e:
                print(f"Failed {pid}: {e}")

                self.all_reviews[pid] = {
                    "status": "failed",
                    "link": url,
                    "product": self.product_name,
                    "error": str(e)
                }

                self._save_json(self.review_file, self.all_reviews)

            time.sleep(self.sleep_time)

        print("\nDone.")
