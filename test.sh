#!/bin/sh
bean-example > .artifacts/example.beancount

bean-report .artifacts/example.beancount balances > .artifacts/example-balances.txt

# python -m beansieve --type sql   --source ".artifacts/example.beancount" --dest ".artifacts/example.sqlite"
#
# python -m beansieve --type plain --source ".artifacts/example.sqlite"    --dest ".artifacts/example_plain.beancount"
#
# bean-report .artifacts/example_plain.beancount balances > .artifacts/example_plain-balances.txt

rm -rf .artifacts/example_aggregate

python -m beansieve \
  --type aggregate \
  --source ".artifacts/example.beancount" \
  --dest ".artifacts/example_aggregate" \
  --rule "Etrade|Income:US:ETrade:.*,Payroll|Income:US:Babble:Salary"

bean-report .artifacts/example_aggregate/Main.beancount balances > .artifacts/example_aggregate-balances.txt

# python -m beansieve \
#   --type archive \
#   --source ".artifacts/example.beancount" \
#   --dest ".artifacts/example_archive" \
#   --keep 7d
#
# bean-report .artifacts/example_archive/main.beancount balances > .artifacts/example_archive-balances.txt
