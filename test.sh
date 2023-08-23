#!/bin/sh

# sample
bean-example > .artifacts/example.beancount
bean-report .artifacts/example.beancount balances > .artifacts/example-balances.txt

rm -rf .artifacts/example_aggregate
python -m beansieve \
  --type aggregate \
  --source ".artifacts/example.beancount" \
  --dest ".artifacts/example_aggregate" \
  --rule "Etrade|Income:US:ETrade:.*,Payroll|Income:US:Babble:Salary"
bean-report .artifacts/example_aggregate/main.beancount balances > .artifacts/example_aggregate-balances.txt

rm -rf .artifacts/example_archive
python -m beansieve \
  --type archive \
  --source ".artifacts/example.beancount" \
  --dest ".artifacts/example_archive" \
  --keep 7d
bean-report .artifacts/example_archive/main.beancount balances > .artifacts/example_archive-balances.txt

# production

bean-report .artifacts/prod/main.book balances > .artifacts/prod-balances.txt

rm -rf .artifacts/prod_aggregate
python -m beansieve \
  --type aggregate \
  --source ".artifacts/prod/main.book" \
  --dest ".artifacts/prod_aggregate" \
  --rule "Housing|Assets:SocietySecurity:Housing"
bean-report .artifacts/prod_aggregate/main.beancount balances > .artifacts/prod_aggregate-balances.txt

rm -rf .artifacts/prod_archive
python -m beansieve \
  --type archive \
  --source ".artifacts/prod/main.book" \
  --dest ".artifacts/prod_archive" \
  --keep 7d
bean-report .artifacts/prod_archive/main.beancount balances > .artifacts/prod_archive-balances.txt
