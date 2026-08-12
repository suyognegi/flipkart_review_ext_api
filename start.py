

import asyncio
from review_processor import review_processor


async def start():
    processor = review_processor(
        product_name="laptop",
        review_limit=1000,
        page=15,
        alpha=12
    )

    await processor.init_urls()
    processor.run()


asyncio.run(start())
