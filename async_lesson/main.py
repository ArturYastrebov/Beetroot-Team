import asyncio


async def factorial(name, number, flag=None):
    if flag:
        raise Exception("Error")
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # Schedule three calls *concurrently*:

    task1 = asyncio.create_task(factorial("A", 2))
    task2 = asyncio.create_task(factorial("B", 3))
    task3 = asyncio.create_task(factorial("C", 4))

    L = await asyncio.gather(
        task1, task2, task3, return_exceptions=True
    )
    print(L)

asyncio.run(main())