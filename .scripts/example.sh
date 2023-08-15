#!/bin/sh
bean-example > .artifacts/example.beancount
bean-sql .artifacts/example.beancount > .artifacts/example.sqlite
