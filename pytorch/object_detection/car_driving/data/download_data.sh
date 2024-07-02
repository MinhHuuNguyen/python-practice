#!/bin/bash

process_onedrive_url() {
    local original_url="$1"

    encode_url() {
        local sharingUrl="$1"
        local base64Value=$(printf "%s" "$sharingUrl" | base64)
        local encodedUrl="u!$(echo "$base64Value" | tr -d '=' | tr '/' '_' | tr '+' '-')"
        echo "$encodedUrl"
    }

    encoded_url=$(encode_url "$original_url")
    local api_url="https://api.onedrive.com/v1.0/shares/${encoded_url}/root/content"

    echo $api_url
}

download_content() {
    local original_url="$1"
    local output_file="$2"
    local api_url=$(process_onedrive_url "$original_url")

    # Download content using wget
    wget -L -O "$output_file" "$api_url"
}


download_content "https://1drv.ms/u/s!Ar6AxGyENvlVgoZ48GK_oUxa4cqqpA?e=dNMEdm" "data.zip"
unzip data.zip

download_content "https://1drv.ms/u/s!Ar6AxGyENvlVgoZ3DOxB9--4McpeGw?e=oWOhqy" "data.zip"
unzip data.zip
