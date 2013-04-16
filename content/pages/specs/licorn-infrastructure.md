Title: Licorn.org infrastructure
Slug: licorn-infrastructure
Status: hidden
Lang: en

## SSH Access

Here are the lines you need to insert into your `~/.ssh/config` to access public Licorn® servers:

    Host duncan.licorn.org duncan
            Port 22

    Host docs.licorn.org docs doc.licorn.org doc
            Port 2250

    Host daily.licorn.org daily
            Port 2260

    Host packages.licorn.org packages archive.licorn.org archive
            Port 2261
