Transmission
============

This Ansible role helps with the installation and configuration of the Transmission Bittorrent Client. The role has been build to configure Transmission as a service and will not install the GUI client. You can run the role against your server and access it through your web browser or by
using the CLI on your own system or the server itself.

Requirements
------------

This role has no additional requirements.

Role Variables
--------------

Most of these variables are the same as documented in the Transmission [settings documentation](https://github.com/transmission/transmission/blob/main/docs/Editing-Configuration-Files.md). There are some small differences though.

| Variable | Default | Description |
| -------- | ------- | ----------- |
| transmission_enabled | yes | Controls the running and startup state of the Transmission service |
| transmission_cli | yes | Indicated if the transmission-cli package should also be installed |
| transmission_config_dir | `"/etc/transmission-daemon"` | Configuration directory |
| transmission_user | `"debian-transmission"` | The user to run the service under |
| transmission_user_home_dir | `"/var/lib/transmission-daemon"` | The home directory of the user |
| transmission_group | `"debian-transmission"` | The group to run the service under |
| transmission_service | `"transmission-daemon"` | The name of the Transmission service |
| transmission_utp_enabled | yes | Enable Micro Transport Protocol |
| transmission_port_forwarding_enabled | no | Enable UPnP or NAT-PMP |
| transmission_encryption | `"prefer"` | Encryption preference |
| transmission_encryption_options | `["no-prefer", "prefer", "require"]` | Possible options for the transmission_encryption variable. no-prefer = Don't prefer encryption, prefer = Prefer encryption, require = Require encryption |
| transmission_speed_limit_down_enabled | yes | Enable download speed limit |
| transmission_speed_limit_down | 5000 | The download limit in KB/s |
| transmission_speed_limit_up_enabled | yes | Enable upload speed limit |
| transmission_speed_limit_up | 1000 | The upload limit in KB/s |
| transmission_alt_speed_enabled | no | Enable alternate speed profile |
| transmission_alt_speed_down | 50 | The alternate speed download limit in KB/s |
| transmission_alt_speed_up | 50 | The alternate speed upload limit in KB/s |
| transmission_alt_speed_time_enabled | no | Enable alternate speed time schedule |
| transmission_alt_speed_time_begin | 540 | Schedule start time in minutes starting from midnight 9 AM |
| transmission_alt_speed_time_day | `"{{ transmission_alt_speed_time_day_options['AllDays'] }}"` | Configures the days when the schedule should be active |
| transmission_alt_speed_time_day_options | `{ "Sunday": 1, "Monday": 2, "Tuesday": 4, "Wednesday": 8, "Thursday": 16, "Friday": 32, "Saturday": 64, "Weekdays": 62, "Weekends": 65, "AllDays": 127 }` | Possible options for the transmission_alt_speed_time_day variable. You can combine days by using the '|' operator |
| transmission_alt_speed_time_end | 1020 | Schedule end time in minutes from midnight 5 PM |
| transmission_ratio_limit_enabled | no | Enable ratio seeding limit |
| transmission_ratio_limit | 2 | Ratio seeding limit |
| transmission_download_queue_enabled | yes | Enable download queue |
| transmission_download_queue_size | 5 | Maximum amount of simultaneously downloaded torrents |
| transmission_seed_queue_enabled | no | Enable seed queue |
| transmission_seed_queue_size | 10 | Maximum amount of simultaneously seeded torrents |
| transmission_idle_seeding_limit_enabled | no | Enable idle seeding limit. This will stop the seeding of a torrent after is has been idle for a certain amount of time |
| transmission_idle_seeding_limit | 30 | Idle seeding limit in minutes |
| transmission_upload_slots_per_torrent | 14 | Amount of upload slots per torrent |
| transmission_queue_stalled_enabled | yes | When enabled, torrents that have not seen any activity for a specified amount of time, are not counted towards the seed and download queue limits |
| transmission_queue_stalled_minutes | 30 | Amount of time (in minutes) a torrent has to be idle before it is marked as stalled |
| transmission_download_dir | `"{{ transmission_user_home_dir }}/downloads"` | The directory to store downloaded files |
| transmission_incomplete_dir_enabled | no | Store files of incomplete torrents in a separate directory |
| transmission_incomplete_dir | `"{{ transmission_download_dir }}/incomplete"` | Path of the directory that is to be used to store incomplete torrent files |
| transmission_rename_partial_files | yes | Gives incomplete files the '.part' postfix |
| transmission_scrape_paused_torrents_enabled | yes | Send tracker scraping requests for paused torrents |
| transmission_preallocation | `"fast"` | Disk preallocation preference |
| transmission_preallocation_options | `["off", "fast", "full"]` | Options for the `transmission_preallocation` variable |
| transmission_umask | "022" | umask to use for created files |
| transmission_prefetch_enabled | yes | Enable prefetch |
| transmission_cache_size_mb | 4 | Cache size in MB |
| transmission_watch_dir_enabled | no | Watch a particular directory for new torrent files and add them |
| transmission_watch_dir | `"{{ transmission_user_home_dir }}/watch"` | Path to the directory to watch |
| transmission_pex_enabled | yes | Enable Peer Exchange |
| transmission_lpd_enabled | no | Enable Local Peer Discovery |
| transmission_bind_address_ipv4 | `"0.0.0.0"` | IPv4 bind address for incoming peers |
| transmission_bind_address_ipv6 | `"::"` | IPv6 bind address for incoming peers |
| transmission_peer_congestion_algorithm | `""` | The TCP Congestion Algorithm to use. Leave empty for system default |
| transmission_peer_id_ttl_hours | 6 | Recycle the peer id used for public torrents after N hours of use |
| transmission_peer_limit_global | 200 | Global peer limit |
| transmission_peer_limit_per_torrent | 50 | Peer limit per torrent |
| transmission_peer_port | 51413 | Port to use for incoming peer connections |
| transmission_peer_port_random_on_start | no | Enable random peer port selection |
| transmission_peer_port_random_high | 65535 | Random peer port selection upper bound |
| transmission_peer_port_random_low | 49152 | Random peer port selection lower bound |
| transmission_peer_socket_tos | `"default"` | Set the Type-Of-Service parameter for outgoing TCP packets. Possible values are: "default", "lowcost", "throughput", "lowdelay" and "reliability" |
| transmission_rpc_enabled | yes | Enable RPC |
| transmission_rpc_bind_address | `"0.0.0.0"` | RPC bind address |
| transmission_rpc_port | 9091 | RPC port |
| transmission_rpc_url | `"/transmission/"` | RPC URL |
| transmission_rpc_host_whitelist_enabled | yes | Enable RPC host domain whitelist |
| transmission_rpc_host_whitelist | `[]` | The domains that should have access to RPC |
| transmission_rpc_whitelist_enabled | yes | Enable RPC host IP whitelist |
| transmission_rpc_whitelist | [ `"127.0.0.1"` ] | The IP's that should have access to RPC |
| transmission_rpc_authentication_required | yes | Enable RPC authentication |
| transmission_rpc_username | `"transmission"` | Username to use for RPC |
| transmission_rpc_password | `""` | Password to use for RPC |
| transmission_script_torrent_done_enabled | `"{{ transmission_script_torrent_done_filename | length > 0 }}"` | Execute a script if a torrent has been completed |
| transmission_script_torrent_done_filename | `""` | Path to the script |
| transmission_blocklist_enabled | `"{{ transmission_blocklist_url | length > 0 }}"` | Enable the use of a blocklist |
| transmission_blocklist_url | `""` | The url to the blocklist |
| transmission_message_level | `"error"` | Configures the log level |
| transmission_message_level_options | `["none", "error", "info", "debug"]` | Options for the `transmission_message_level` variable |
| transmission_dht_enabled | yes | Enable Distributed Hash Table |
| transmission_start_added_torrents | yes | Start newly added torrents |
| transmission_trash_original_torrent_files | no | Remove the original torrent file after it has been added |

Role Tags
---------

| Tag | Description |
| --- | ----------- |
| transmission-install | Runs installation tasks such as installing packages, creating users and groups and installing service files |
| transmission-configure | Runs configuration tasks such as creating configuration directories and files |
| transmission-validate | Runs tasks that validate the variables and system configuration and ensures that the role can be properly deployed |
| install | Global install tag. Allows you to easily run the installation tasks on a multitude of compatible roles |
| configure | Global configure tag. Allows you to easily run the configuration tasks on a multitude of compatible roles |
| validate | Global validate tag. Allows you to easily run the validation tasks on a multitude of compatible roles |

Dependencies
------------

This role has no dependencies.

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - vharmers.transmission
  vars:
    transmission_rpc_username: admin
    transmission_rpc_password: ImBatman$12
    transmission_download_dir: /data/torrents
```

Testing
-------

Testing is done with [Molecule](https://molecule.readthedocs.io/en/latest/) and [Vagrant](https://www.vagrantup.com).

**Step 1:** Install a hypervisor such as [VirtualBox](https://www.virtualbox.org).

**Step 2:** Install Vagrant. Follow the installation instructions for your OS on the [downloads](https://www.vagrantup.com/downloads) page.

**Step 3:** Install the necessary Python packages:

```bash
pip install ansible ansible-lint molecule molecule_vagrant pytest-testinfra
```

**Step 4:** Descent into the role directory and run the `molecule test` command.

License
-------

[MIT](LICENSE)

Author Information
------------------

*Valentijn Harmers* ([website](https://www.vharmers.com))
