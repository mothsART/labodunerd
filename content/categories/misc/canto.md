Title: config-canto
Category: misc
Tags: python, rss, canto
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: config-canto
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

INTERNAL USAGE
       Within the program you can use the following (default) keys.  These can
       be  changed in your configuration file by using the "key" configuration
       option.

       UP / DOWN or k / j
              Select previous or next item. (next_item) (prev_item)

       PGUP / PGDOWN or o / l
              Goto previous or next tag. (next_tag) (prev_tag)

       RIGHT / LEFT
              Set item unread or read (just_unread) (just_read)

       [ / ]  Cycle through defined filters (prev_filter) (next_filter)

       { / }  Cycle   through   defined   tag    filters    (prev_feed_filter)
              (next_feed_filter)

       - / =  Cycle through defined tag sorts (prev_tag_sort) (next_tag_sort)

       < / >  Cycle through defined tag sets (prev_tagset) (next_tagset)

       :      Goto a specific tag (order of the config) (goto_tag)

       ;      Goto a specific visible tag (goto_reltag)

       TAB    Switch focus between list and reader (only useful with dedicated
              reader space)
                  (switch)

       h      Display this man page. (help)

       Space  Read a story (reader)

       g      Use the defined browser to goto the item's URL (goto)

       C / V  Collapse/Uncollapse      all       tags       (set_collapse_all)
              (unset_collapse_all)

       c      Collapse/Uncollapse current tag (toggle_collapse_tag)

       f      Inline search (inline_search)

       m      Toggle item marked/unmark (toggle_mark)

       M      Unmark all items (all_unmarked)

       n / p  Goto next/previous marked item (next_mark) (prev_mark)

       , / .  Goto next/previous unread item (next_unread) (prev_unread)

       r / u  Mark tag read/unread (tag_read) (tag_unread)

       R / U  Mark all read/unread (all_read) (all_unread)

       Ctrl+R Refresh feeds (force_update)

       Ctrl+L Redraw screen (refresh)

       \      Restart Canto (restart)

       q      Quit Canto (quit)
