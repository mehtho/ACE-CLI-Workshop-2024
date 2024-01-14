#!/bin/bash

read input_string

hash=$(echo -n "$input_string" | sha256sum | cut -d' ' -f1)

if [ "$hash" = "e0f05da93a0f5a86a3be5fc0e301606513c9f7e59dac2357348aa0f2f47db984" ]; then
    echo "Exercise Complete! "Bee" occurs $input_string times!"
else
    echo "Exercise not complete."
fi
