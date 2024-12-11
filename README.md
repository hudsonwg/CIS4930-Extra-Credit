# Data Processing & Storage CLI
### Hudson Goddard

# Setup

This application is lightweight and easy to set up. There are no required dependencies. Simply import the python main file into an environment of your choosing and run with native configurations

## General Use

This application implements a command parser to streamline the use process. Common commands are outlined below.

## Commonly Used Commands
- Start: open a new transaction
- Put [arg1] [arg2]: inputs a new pending entry into transaction with key: arg1 and value: arg2
- Get [arg]: returns database value of argument or null if key doesn't exist
- Debug: returns display of pending transaction, database, and use states
- Commit: commits current transaction to main database
- Rollback: aborts current pending transaction, reverts to pre-transaction state
- Exit: type exit at any time to exit the program
