Title: (Re-)starting (again)…
Tags: development, blog, infrastructure, Trac, PostgreSQL

I wanted to migrate Licorn® `Trac` 0.12.2 to 1.0 for a long time, and took time to acheive it this week-end. This has perfectly failed for a bunch of undocumented and non-googled reasons. Seems like Trac is not used that much nowadays (but I still enjoy it). As a consequence, [dev1.licorn.org](http://dev1.licorn.org/) is down, totally unusable.

I feel tired in advance when I think about it, because I just would like to go on and code Licorn®, not spending time repairing a failed database migration, a failed system python packages upgrade and an old-and-odd WSGI script, doing boring sysadmin work. I *do have* backups. Plenty of them. I even re-backed-up the LXC once more before starting the migration.

I could just restore the previous setup. But it’s old, and it really needs a refresh. I don’t want to see this old website and old theme again. I *will* set it back up for historical purposes; but later. For now, I will just turn this failure into an oportunity to start a brand fresh install, a brand new roadmap and get rid of open-for-3-years-but-never-done task issues. 

This is the right moment to announce that **Licorn 2.0 is on the way**. This is a low-level from-scratch rewrite. I learned a lot recently, and pushed my Python knowledge to the next level. Licorn® could be times smaller, with a bunch of new really helpful features, retaining the main ones and gaining use of multi-core machines.

For the development infrastructure, I could just have switched over to github [*even Twitter uses it for Bootstrap!*]. You can already find a **temporarily empty** [Licorn® 2.0 repository](https://github.com/Karmak23/licorn) over there.

But I’m still in need of my own freedom, and the github repository purpose is just to handle punctual pull requests without having to create a full Licorn® developer account on my own servers. The main Licorn® repository will remain on [dev.licorn.org](http://dev.licorn.org/).

I’m thus rebuilding this server from scratch, with a (hopefully) clean `Trac` 1.0 installation, and a `PostgreSQL` database (`SQLite` has showed a lot of its limitations lately). I won’t reinstall the developer blog and other Trac plugins, they have been unmaintained for too much time and they make every database migration painful.

The present blog is a perfect and much easier replacement.

See you on [dev.licorn.org](http://dev.licorn.org/) when everything is back online. And this should happen soon: I’m on it.