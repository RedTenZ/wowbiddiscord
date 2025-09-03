# Discord Auction Bot

A Discord bot for bidding on different items, configurable by the server owner. Perfect for servers that want to organize auctions for in-game items or community events.  

Built in **Python** using **discord.py**.  

---

## Features

- Start an auction in a specific channel (`!start`)  
- Place bids (`!bid <amount>`)  
- Remove bids (`!unbid <user>`)  
- Automatic embed updates with current highest bids  
- Notifications sent to bidders when a new bid is placed  

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/discord-auction-bot.git
cd discord-auction-bot
```

2. **Install dependencies**  

Make sure you have Python 3.8+ installed.

```bash
pip install discord.py
```

3. **Configure the bot**

- Create a new Discord bot via the [Discord Developer Portal](https://discord.com/developers/applications)  
- Copy the bot token

4. **Set the token**  

In your `bot.py` (or main script), replace:

```python
TOKEN = "YOUR_BOT_TOKEN_HERE"
```

## Configuration

Each auction is configured directly in the channel topic. The format is:

```
<ITEM_ID>
<ICON_ID>
<MINIMUM_PRICE>
```

ITEM_ID: The ID of the item (used for Wowhead link)
ICON_ID: Icon filename for the item image
MINIMUM_PRICE: The minimum bid in gold

Example : 

```
12345
inv_sword_01
500
```

## Usage

- **Start an auction (Admin only)**  
```!start``` 
Creates an embed with the item info and minimum price.  

- **Place a bid**  
```!bid <amount>  ```
Bids must be higher than the current highest bid.  

- **Remove a bid (Admin only)**  
```!unbid <@user>  ```
Removes a user’s bid from the auction.  

Bidders are automatically notified via DM whenever a new highest bid is placed.  
