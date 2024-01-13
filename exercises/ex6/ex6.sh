#!/bin/bash

read input_string

echo $input_string

hash=$(echo -n "$input_string" | sha256sum | cut -d' ' -f1)

echo $hash

if [ "$hash" = "9e11c362bc3d3572970b973d5cd86c073da358b6f9bceaa3be65d1a6487f8819" ]; then
    echo "Exercise Complete!"
else
    echo "Exercise not complete."
fi
