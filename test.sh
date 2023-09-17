#!/bin/sh

# sample
bean-example > .artifacts/example.beancount
bean-report .artifacts/example.beancount balances > .artifacts/example-balances.txt

# aggregate
rm -rf .artifacts/example_aggregate
python -m beansieve \
  --type aggregate \
  --source ".artifacts/example.beancount" \
  --dest ".artifacts/example_aggregate" \
  --rule "Etrade|Income:US:ETrade:.*,Payroll|Income:US:Babble:Salary"
bean-report .artifacts/example_aggregate/main.beancount balances > .artifacts/example_aggregate-balances.txt

# archive
rm -rf .artifacts/example_archive
python -m beansieve \
  --type archive \
  --source ".artifacts/example.beancount" \
  --dest ".artifacts/example_archive" \
  --keep 7d
bean-report .artifacts/example_archive/main.beancount balances > .artifacts/example_archive-balances.txt
