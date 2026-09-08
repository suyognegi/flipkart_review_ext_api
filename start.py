
import asyncio
from review_processor import review_processor

item='smartphones'
async def start():
    processor = review_processor(
        product_name=item,
        review_limit=93,
        page=10,
        alpha=8,
        hash_file=f"{item}_hashmap.json",
        review_file=f"{item}_review.json"
    )

    await processor.init_urls()
    processor.run()


asyncio.run(start())
