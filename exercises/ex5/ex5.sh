#!/bin/bash

read input_string

hash=$(echo -n "$input_string" | sha256sum | cut -d' ' -f1)

if [ "$hash" = "f6e0a1e2ac41945a9aa7ff8a8aaa0cebc12a3bcc981a929ad5cf810a090e11ae" ]; then
    echo "Exercise Complete!"
else
    echo "Exercise not complete."
fi
