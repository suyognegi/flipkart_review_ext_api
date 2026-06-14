
import asyncio
from review_processor import review_processor


async def start():
    processor = review_processor(
        product_name="smartphone",
        review_limit=90
    )

    await processor.init_urls()
    processor.run()


asyncio.run(start())
