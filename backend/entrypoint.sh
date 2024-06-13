#!/bin/sh

if [ -d /sveltedjango/media/public ]; then
    rm -rf /sveltedjango/media/public
fi

mkdir -p /sveltedjango/media/public
cp -r /sveltedjango/public/* /sveltedjango/media/public/

exec "$@"