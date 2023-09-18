#!/bin/sh

# sample
bean-example > example.beancount
bean-report example.beancount balances > example-balances.txt

# aggregate
rm -rf example_aggregate
python -m beansieve \
  --type aggregate \
  --source "example.beancount" \
  --dest "example_aggregate" \
  --rule "Etrade|Income:US:ETrade:.*,Payroll|Income:US:Babble:Salary"
bean-report example_aggregate/main.beancount balances > example_aggregate-balances.txt

# archive
rm -rf .artifacts/example_archive
python -m beansieve \
  --type archive \
  --source "example.beancount" \
  --dest "example_archive" \
  --keep 7d
bean-report example_archive/main.beancount balances > example_archive-balances.txt
