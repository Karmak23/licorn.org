Title: About…
Date: 2013-03-22
Lang: en

<div style="text-align: center; margin: 3em 0;">
    <h1> “ Licorn®, the efficient and effortless way to manage your Ubuntu/Debian server ”</h1>
</div>

In a nutshell, it's just as simple as:

    add user john
    add user alice
    add group work --with-users john,alice

John and Alice will access the `work` shared group from common places in OSX, Windows and Linux to work together. They can invite other users into their group (like `add user bob --guest-of work` for *read-only* access or `add user bob work` for normal read-write access).

If you managed to `sudo aptitude install calendarserver` before doing these few steps, they will get a standard-friendly calendar for each of them, and another common `work` calendar for shared schedules. Other local services are easily *integrated*.

**This is key feature of Licorn®: it uses *standard* tools, protocols and services, and *tie* them together in a consistent metaphor, directed towards ease of use for system administrators and final users.** Think of it as a *Microsoft Small Business Server or OSX Server for Ubuntu/Debian*, but **much simpler** as far as usability and technical knowledge is concerned.

Talking about simplicity, there's obviously a [web management interface](http://docs.licorn.org/wmi/), in which *you* admin can delegate a part of the job to John and Alice.

Now that you scratched the surface, go discover more about [Licorn®'s features](|filename|01_features.md).

# License and credits

Licorn® is GNU GPL version 2 software, lead and developed by [Olivier Cortès](http://oliviercortes.com) since 2007.

It has been partially sponsored by organizations or public institutions from 2010 to 2012, and contributed by other individuals since the start.

*Licorn®* is a trademark of Olivier Cortès in France.
