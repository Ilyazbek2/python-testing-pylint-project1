#!/usr/bin/env bash

echo "Running Pylint..."
pylint --output-format=text,json:pylint_report.json \
    --reports=y --score=y decrypt.py test_decrypt.py
pylint_status=$?

echo
echo "Running unit tests..."
python -m unittest -v test_decrypt
test_status=$?

if [ "$pylint_status" -eq 0 ] && [ "$test_status" -eq 0 ]; then
    echo "OK"
else
    echo "Имеются ошибки"
    exit 1
fi
