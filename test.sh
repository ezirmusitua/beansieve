#!/bin/sh
bean-example > .artifacts/example.beancount

bean-report .artifacts/example.beancount balances > .artifacts/example-balances.txt

python -m beansieve --type sql   --source ".artifacts/example.beancount" --dest ".artifacts/example.sqlite"

python -m beansieve --type plain --source ".artifacts/example.sqlite"    --dest ".artifacts/example1.beancount"

bean-report .artifacts/example1.beancount balances > .artifacts/example1-balances.txt

