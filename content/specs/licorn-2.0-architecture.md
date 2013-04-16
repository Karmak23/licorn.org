Title: Licorn® 2.0 architecture
Slug: licorn-2.0-architecture
Status: draft
Date: 2013-04-14
Tags: daemon, internals, CLI, WMI, API, messages
Lang: en

## Common parts

### Cached core objects

Any daemon/worker could need to:

- instantiate core objects on demand
- cache these objects a little while
- them tear them down to give back RAM
- subscribe to core messages to force cache expiration / reload
    - ignore messages if origin_id == my_ID
- publish core messages when it modifies any of the objects instanciated.
- avoid getting it's own messages, as the changes are already done
    - include an 'origin_id' (uuid4), to filter the messages.

This feature is one united (eg. cache is mandatory), but is optional (eg. some
workers won't use it, it must not be included/run by default.)

### Backends

- are essentially the same as in Licorn® 1.6.
    - as much as possible, can load / save individual objects.
- are called many times, from many instances, in many daemons / processes.

### Extensions

- retain all the Licorn® 1.6 features (threads, locks, classes…),
- and bring in more, eg. the tasks thread/worker is “ just another worker ” and not a fixed part of the main daemon.

## Supervisor daemon

- is a real daemon (background service, daemonized)
- starts zmq forwarder device for pub/sub
- launches workers via multiprocessing
    - opens a direct multiprocessing.??? for statistics?
        - or they just go via a transient request/response tube?
            - or is it not transient at all, and a dedicated worker is responsible of collecting statistics all the time? And thus, no need for a req/rep tube, it just subscribes to stat* messages and every other worker sends them.
- keep them alive (or relaunch)
- tear them down when asked to, or when terminating
- accepts commands from CLI
    - statistics
    - management

## Workers

Dedicated tasks used to be run as threads in the main deamon, which is not multicore-friendly, and leaded to inotify event miss and bad RPC response time.

In fact, task can be splitted in different workers which will have all the same base, like logging, PID and log-file management, statistics primitives or thread, etc.

### www-REST worker

- uses cached core objects
- runs a web server and a RESTfull API -> an official extension??

### Scheduled tasks worker

- runs 1.6-epoch like tasks (they need refactor and cut down)
- runs extensions threads?? (TO BE DECIDED)
    - possible to have a separate daemon for 1+ particular extension(s)?

### Inotifier worker

- does NOT need cached core objects
- **buffers** the kernel/libc inotify events
    - is dedicated to this task, to avoid loosing events.
- counts inotify events based on paths for statistics
    - serialization for life-time statistics
- publishes inotify-related messages to others
- subscribes to:
    - core messages
        - to add / mod / del watched paths
    - CLI check messages
        - to avoid inotifying on currently-checked entries
        - to re-install inotify watches on check-finished messages
- its job can eventually be split across many inotifiers, eg:
    - one for configuration files
    - one for groups
        - fork a new when reaching 50k+ inotify watches?
    - one for users

### Aclchecker worker

- uses cached core objects
- handle it's own inotify-prevent system (avoid re-checking just-checked entries)
- subscribes to:
    - inotify messages
        - to auto-check paths
    - CLI check messages
        - to prevent double-checking
    - core messages
        - to check (create directories) on object creation
        - to check archives/ and other special directories
        - …

### ClusterNode worker

- replaces the complex Licorn® 1.6 `CommandListener` bi-directional mechanism.
- uses cached core objects
- opens a REP socket
- receives REQs, do things and sends REPs
- has primitives to:
    - add / remove a node
    - define "definitive" (serialized) or temporary (one-operation-related) cluster
    - run each REQs in parallel on connected nodes.


## AngularWMI

- is the “ AngularJS WMI ”, runs client-side
- on the server, it's just a bunch of inert HTML/JS files
- can connect to any REST-worker
    - the one it's served from,
    - but others on the same LAN
    - on internet if the REST interface is available?
        - how to do strong authentication?
- does REST-full calls on the REST-workers
- DOES NOT holds the cached core objects at all
    - but has its own models, forms, etc…
- subscribes to core messages notifications (HOW? NullMQ)

## CLI

There are 5 cli tools (`get`, `add`, `mod`, `del`, `chk`). They do different things but I will describe them as one generic process, because their behavior is the same.

- is a transient process, lauched just to **do** things on core objects or not.
- uses cached core objects
    - and thus, publishes messages after changes / deletions…

## workers (and others) statistics

*Currently under design*.
