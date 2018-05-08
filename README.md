# crypto-node
This repository contains all coding documents pertinent to the Crypto-node project by Group H of UCSD's ECE 191 class. 
#Project Goals
Currently the project aims to prove the feasability of implementing a fully-fledged crypto project on an arm processor such as the Dragonboard series provided by 96Boards and Linaro. 
Current Goals:
	1. Wallet Implementation
		Using existing apis we can use most wallets that already support linux as the boards will run debian
	2. Node Hosting
		Cryptocurrency nodes provide crypto payout without a large strain on the host device. As such the implementation and automation of such a crypto faucet would be beneficial in an integrated system.
	3. User/Interface and Features
		To familiarize users with the idea of cryptospace, a package of dependencies should be preinstalled or listed such that the user has no missing package errors. Furthermore, a clear listing of account balances and their conversions into BTC and then USD will be helpful for users to grasp investments. Current plan is to package with a selectable stock ticker to implement this function
	4. Hardware
		Hardware needs will segue off of the wallet mainly and provide a more mobile form factor. A battery can power the device on the go and an LCD display and enclosure will account for a unified body. A 'hardware' wallet can be implemented such that coins can be stored offline if the user so chooses (transactions signed offline).

#Current Progress
	Most of the progress so far has been the group researching crypto currency back end and unix scripting as ECE students, most of us have a strong background in circuit design but maybe lacking moreso on software. Wallet implementation currently is done throught the electrum wallet which can either be ran graphically or through the command line interface. Crypto information is currently being pulled in json (dictionary) format from cryptocurrency sites. Work on the battery and battery charging circuits is underway and the enclosure will be designed upon decision of screen and battery profiles.

