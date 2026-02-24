import asyncio
import time 

async def brew(name):
    print(f"brewing {name}")
    await asyncio.sleep(5)
    print(f"{name} is ready....")


async def main():
    await asyncio.gather(
        brew("masala chai"),
        brew("elaichi chai "),
        brew("clove chai")
    )

asyncio.run(main())