
# Polish Railway Expert Discord Bot

## Overview

The Polish Railway Expert Discord Bot is a helpful assistant for all enthusiasts of the Polish railway system and helps also the Users of Train Driver 2 and SimRail. Powered by OpenAI's ChatGPT, this bot can answer detailed questions about the Polish railway system, provide information about railway simulators, and much more. The Bot uses the Custom ChatGPT Assistant API where a custom GPT has been created with the Data of the Simulators and the Polish Railway Rulebooks. 

## Features

- **Expert Knowledge**: Provides detailed and accurate information about the Polish railway system.
- **Simulator Support**: Answers questions about Train Driver 2 and SimRail simulators.
- **Queue System**: Manages multiple queries efficiently using a queue system.

## Samples:
Question: /askpkp question: how fast can a train go when he gets an Sz Signal in Train Driver 2?
Answer: Wenn ein Zug das Sz-Signal in Train Driver 2 erhält, darf er mit einer Geschwindigkeit von maximal 40 km/h fahren. Diese Geschwindigkeit muss jedoch so reguliert werden, dass der Lokführer jederzeit in der Lage ist, den Zug im Falle einer plötzlichen Hinderniswarnung zum Stehen zu bringen.

Question: /askpkp question: who are the authors of the scenery czermin? Answer in English
Answer: The authors of the scenery "Czermin" are:

-   **Ares28**  - Track layout, signaling, and surroundings.
-   **Matz32**  - Satellite sleepers, poles, and milestone signs.
-   **jabol438**  - Assistance with the overhead line.
-   **Trichlor**  - Help in adapting the scenery to the new version.

Question: /askpkp question: im in a offline scenery in train driver 2. what do i have to do as a driver to drive into the next online szenery? answer in english
Answer: o drive from an offline scenery to the next online scenery in Train Driver 2, you must follow these steps:

1.  **Ensure You Have a Valid Timetable**: Make sure that you are operating under a valid timetable that includes the next scenery which is online.

2.  **Contact the Dispatcher**: Use the TS3 communicator or the command `/swdr <content>` to request permission from the dispatcher of the next online scenery.

3.  **Wait for Confirmation**: The dispatcher will respond to your request, and you must wait for their approval before proceeding.

4.  **Follow Dispatcher Instructions**: Adhere to any additional instructions given by the dispatcher to ensure a smooth transition into the online scenery.

5.  **Proceed Once Authorized**: After receiving permission, you can continue your journey into the online scene.

It is important to comply with all rules and protocols set by the simulator to avoid penalties.

## Getting Started

### Prerequisites

- Docker
- Python 3.11
