# Best example to learn what is async/await situation in real world and in technical world

"""
The Coffee Shop Analogy: What is "Async"?
Imagine your coffee shop operates in a unique way. Instead of just one barista (the "sync" model), you have:

One Primary Barista (The asyncio Event Loop / Your Main Thread): This is the person who takes orders, manages
the flow, and knows how to "delegate" waiting tasks. They are very efficient at switching between things.
Specialized Coffee Machines and Equipment (I/O Devices / External Services): These are things like:
The Espresso Machine: It takes time to pull a shot.
The Milk Steamer: It takes time to heat milk.
The Drip Coffee Maker: It takes time to brew a pot.
The Cash Register / Card Reader: It takes time to process payments with the bank.
The Toastie Press: It takes time to grill a sandwich.
"Async" (Asynchronous Operation): The "I'll Let You Know When It's Ready" Way
In an "async" coffee shop, the primary barista doesn't stand there watching the espresso shot pull or the 
milk steam. Instead, they use a system of "callbacks" or "notifications."

Here's the "async" process:
Customer A orders a Latte:

The primary barista takes the order.
Barista: "Okay, I need an espresso shot." They start the Espresso Machine (an I/O operation).
This is the "async" part: Instead of waiting, the barista gives a little buzz timer to the machine 
(a "future" or "promise"). "Machine, when that shot is ready, let me know (send a notification/signal)!"
The barista then immediately turns their attention to something else. They don't block.
Customer B orders a Black Coffee (while Customer A's espresso is brewing):

The primary barista takes the order.
Barista: "Okay, I need drip coffee." They start the Drip Coffee Maker.
This is another "async" part: "Maker, brew this pot. When it's ready, let me know!"
Again, the barista immediately turns their attention to something else.
Customer C pays for a muffin:

The primary barista takes the muffin.
Barista: "Okay, I need to process payment." They use the Card Reader (another I/O operation talking to the bank).
This is another "async" part: "Card Reader, process this payment. When the bank approves it, let me know!"
The barista, as always, doesn't block. They're ready for the next immediate task.
The Role of the Primary Barista (The Event Loop):
The primary barista is constantly scanning:

"Is any coffee machine done brewing and buzzing?"
"Has the card reader finished processing a payment?"
"Is there a new customer at the counter?"
When the espresso machine buzzes (the "async" operation for Customer A's latte is complete),
the barista grabs the shot and continues making the latte. When the card reader beeps (payment for Customer 
C is approved), the barista prints the receipt.

What "Async" Allows is this non-blocking nature. It's the capability for the primary barista to say to a task:
"Go do your thing, and notify me when you're done. In the meantime, I'm available to help other customers or 
start other parts of orders."
"""


"""
Connecting to FastAPI:
Your FastAPI App: The coffee shop.
The Primary Barista (Single Thread): The asyncio event loop that FastAPI uses.
Customers (Requests): API calls like /get_user, /get_product.
Coffee Machines / Card Readers (I/O operations): Database queries, external API calls, reading/writing files.
When your FastAPI endpoint (async def my_endpoint(...)) encounters an await statement for an I/O operation 
(e.g., await database.fetch_data()), it's like the barista starting the espresso machine:

The await tells the event loop: "I'm starting an operation that will take time. I don't need the CPU for
this part. You can go serve another request (another customer) or continue another ongoing task (another coffee machine)."
The event loop (the primary barista) then immediately looks for something else to do. It doesn't wait for the
database.fetch_data() to return. It processes another incoming HTTP request, or checks if another database query
it started earlier has finished, or if a network call has completed.
When the database responds (the espresso machine buzzes): The event loop receives a notification. It then
"resumes" the specific my_endpoint function right after the await statement, using the data that just arrived 
from the database.
In summary, "async" is the characteristic of being non-blocking and notification-driven. It's the ability to 
initiate a task and then immediately move on to other things while waiting for that task to complete, relying 
on a notification system (the event loop) to resume the task when it's ready. This is what allows a single 
process to handle many concurrent operations efficiently, making FastAPI incredibly fast for I/O-bound workloads.
"""

# Code
"""
from fastapi import FastAPI
import httpx # A popular async HTTP client

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # Simulate an I/O operation (e.g., fetching from a database)
    # In a real app, this would be an actual async database query
    await asyncio.sleep(2) # Simulate a 2-second delay
    return {"item_id": item_id, "data": "Some data fetched asynchronously"}

@app.get("/external-data")
async def get_external_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/todos/1")
        return response.json()
"""


# Reason why fastApi uses async/await and concurrencys
"""
The Problem: Waiting Around
Imagine you're a chef in a busy restaurant (your FastAPI application). You have many customers (incoming requests).
Synchronous (Traditional Blocking): If you take an order for a steak (a request that takes 10 minutes to cook), you 
cannot take any other orders or do anything else until that steak is done. While you're waiting for the steak 
to cook, your other customers are getting impatient, and your restaurant is losing business. This is what 
happens in a traditional, blocking web server. If one request takes a long time (e.g., calling an external API,
database query), all other requests have to wait.
"""