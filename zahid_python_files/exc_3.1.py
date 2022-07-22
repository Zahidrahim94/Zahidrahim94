# # num=0
# # tot=0.0
# # while True:
# #     sval= input("Enter a number: ")
# #     if sval== "done" :
# #         break
# #     try:
# #         fval=float(sval)
# #     except:
# #         print("invalid input")
# #         continue
# #     fval=float(sval)
# #     print(fval)
# #     num=num+1
# #     tot= tot + fval


# # print("All Done")
# # print(tot,num,tot/num)
# largest = None
# smallest = None

# while True:
#     num = input("Enter a number: ")
#     if num == 'done':
#         break
#     try:
#         n = int(num)
#     except:
#         print('Invalid input')
#         continue
#     if largest is None or largest < n:
#         largest = n
#     elif smallest is None or smallest > n:
#         smallest = n
#     elif n < smallest:
#         smallest = n

# print('Maximum is',largest)
# print('Minimum is',smallest)

import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())