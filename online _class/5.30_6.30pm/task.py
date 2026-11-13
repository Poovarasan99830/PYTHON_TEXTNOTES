
# import asyncio

# async def handle_user(name):
#     for i in range(3):
#         await asyncio.sleep(1)
#         print(f"{name}: message {i+1}")

# async def main():
#     users = ["Alice", "Bob", "Charlie"]

#     tasks = [asyncio.create_task(handle_user(u)) for u in users]
#     await asyncio.gather(*tasks)

# asyncio.run(main())


# import asyncio

# async def make_tea(order_no):
#     print(f"Tea {order_no} started...")
#     await asyncio.sleep(2)
#     print(f"Tea {order_no} ready!")
#     return order_no




# async def main():
#     tasks = []

#     for i in range(1, 6):
#         tasks.append(asyncio.create_task(make_tea(i)))

#     results = await asyncio.gather(*tasks)
#     print("All teas completed:", results)

# asyncio.run(main())



import asyncio

async def do_work(name, seconds):
    print(f"{name} started (will take {seconds}s)")
    await asyncio.sleep(seconds)
    print(f"{name} finished")
    return f"{name}-result"


async def main():
    t1 = asyncio.create_task(do_work("Job-A", 2))
    t2 = asyncio.create_task(do_work("Job-B", 1))
    t3 = asyncio.create_task(do_work("Job-C", 3))

    await t1
    await t2
    await t3


asyncio.run(main())