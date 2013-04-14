Title: Features
Date: 2013-03-22
Lang: en

# *Traditional* system management

- classic **users** and **groups** (either `LDAP` or traditional `shadow`), with easy massive creation and importing features,
- **workgroups**, via shared directories. This is one of Licorn® strengths, nevertheless it's a [very simple approach](http://docs.licorn.org/groups/),
- **privileges**, to delegate a subset of management roles to any user,
- **incremental backups**, handled auto-magically (plug an empty external drive on your server and head to [your WMI](https://localhost:3356/backups)),

# Network-related

- **remote management** on the LAN and from the outside, via the WMI or SSH (from one Licorn® server to other local Licorn® servers or clients),
- **web proxy** on the LAN (via [squid](http://www.squid-cache.org/)), auto-configured from one Licorn® server to its local peers,
- `Samba` (with some unique features) and `netatalk` management,
- simple **remote monitoring** (via [MyLicorn®](http://my.licorn.org/) freemium service),
- various local **services auto-configuration** and management (`OpenSSH`, `udisks`… [See complete list](http://docs.licorn.org/extensions/))

# Advanced or unique features

- **Simple web sharing** ([read more…][webshare]),
- **laptop and power-management friendly**. Install it on your prefered machine to manage it as easily as your server. It will mount your USB keys (retaining backup functionality), won't prevent *suspend* and will even tell [MyLicorn®](http://my.licorn.org/) that your laptop just suspended;
- **low-resources daemon** ([environmental institution sponsored][ademe]),
- **Powerful extension mechanism** to plug-in and handle a new service at any time, any place in the Licorn® daemon. This allows developers to write new [extensions][] in terms of hours instead of weeks.


  [webshare]: http://docs.licorn.org/userdoc/simplesharing
  [extensions]: http://docs.licorn.org/extensions/
  [ademe]: |filename|/pdf/Rapport_Scientifique_ADEME_Licorn_2012.pdf
    "2012 Scientific Report of Licorn® work sponsored by ADEME in 2010-2011 (PDF in french, 55 pages, 22Mib)"
