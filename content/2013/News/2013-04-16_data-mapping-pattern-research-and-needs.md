Title: Data mapping pattern research and needs
Lang: en

## ActiveRecord, DataMapper or Repository?

I'm currently reading a lot on these subjects, to bring a clean, simple and hopefully flexible and powerful implementation in Licorn® core. The problem is hard to solve at first glance: unlike `Django` and other frameworks, Licorn® cannot rely on a relational (or NoSQL) database when it has to deal with system data.

We have only *flat* configuration file, each with a different format, storing different kind of data. Needless to say this is a mess which needs something *very cool* to be solved elegantly, in a quite-uniform manner.

## My needs

- Core objects (users, groups, machines…) are classes with business logic. While I enjoy the ActiveRecord pattern, it's not strictly mandatory to implement it.
- they can have multiple, decoupled and parallel (*more-than-one-active*) storages (`shadow`, LDAP, Relational (or not) DB, `dnsmasq` (or `bind9`, whatever) configuration files, even *volatile* in RAM): eg. some users can be in shadow, others in LDAP; idem for groups; some machines can be part in dnsmasq and others in RAM when the network has been scanned and new unknown machines are discovered;
- a core object must be "live-movable" from a storage to another. Atomicity should be mandatory but I won't cry if it's not. The problem is complex enough ;-)

- Extensions add custom attributes / methods to:
    - core object classes (via mixins, like in the Licorn® 1.6 `simplesharing` extension, which will probably be pulled back in “ as is ”, modulo the Python 3 port)
    - backends? I still have to find a real-life example…
- They can have multiple, decoupled and parallel storages too.
- Storage can be different from base classes:
        - LDAP, postfix DB, local files (simplefile, JSON, caldalvd XML…), other…

- To build interfaces (web, CLI…) quickly, I would *love* to have a facility like Django's `ModelForm`: one line of code gives me an auto-built form with validators, etc.

## Bonus

Eventually, I could write a converter to generate `AngularJS` HTML forms from the Django-like `{{ form }}` output, and even possibly automated JS-code for validators (via a coffee-script bridge?).

This way we would have the validators written only once, but data checked on both sides: client-side for user comfort and server-side for security.

This converter could be reusable in other “ real ” Django projects. Wow. This seems cool.

##### And I pushed a bunch of commits in [Licorn® Github repository](https://github.com/Karmak23/licorn). Even more are in the pipe.
