find ./resource/xml/schema/ -type f -name '*.xsd' | xargs -i -t ./.venv/bin/xsdata \
    --package mugimugi.bo \
    --output dataclasses \
    {}
