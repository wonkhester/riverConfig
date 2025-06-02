local wezterm = require 'wezterm'

return {
    enable_tab_bar = false,
    disable_default_key_bindings = true,

    keys = {
        -- Reload config
        {
            key = "r",
            mods = "CTRL|SHIFT",
            action = wezterm.action.ReloadConfiguration,
        },

        -- Copy (Ctrl+Shift+C)
        {
            key = "c",
            mods = "CTRL|SHIFT",
            action = wezterm.action.CopyTo "Clipboard",
        },

        -- Paste (Ctrl+Shift+V)
        {
            key = "v",
            mods = "CTRL|SHIFT",
            action = wezterm.action.PasteFrom "Clipboard",
        },

        -- Scroll up (Shift+PageUp)
        {
            key = "PageUp",
            mods = "SHIFT",
            action = wezterm.action.ScrollByPage(-1),
        },

        -- Scroll down (Shift+PageDown)
        {
            key = "PageDown",
            mods = "SHIFT",
            action = wezterm.action.ScrollByPage(1),
        },
    },

    colors = {
        foreground = "#d4be98",
        background = "#282828",
        cursor_bg = "#d4be98",
        cursor_border = "#d4be98",
        cursor_fg = "#282828",
        selection_bg = "#3c3836",
        selection_fg = "#d4be98",

        ansi = {
            "#32302f", -- black
            "#ea6962", -- red
            "#a9b665", -- green
            "#d8a657", -- yellow
            "#7daea3", -- blue
            "#d3869b", -- magenta
            "#89b482", -- cyan
            "#d4be98", -- white
        },
        brights = {
            "#5a524c", -- bright black
            "#ef938e", -- bright red
            "#bbc585", -- bright green
            "#e1bb7e", -- bright yellow
            "#9dc2ba", -- bright blue
            "#e0b9c6", -- bright magenta
            "#a7cfa3", -- bright cyan
            "#e2d3ba", -- bright white
        },
        tab_bar = {
            background = "#1d2021",
            active_tab = {
                bg_color = "#32302f",
                fg_color = "#d4be98",
            },
            inactive_tab = {
                bg_color = "#1d2021",
                fg_color = "#928374",
            },
            inactive_tab_hover = {
                bg_color = "#3c3836",
                fg_color = "#d4be98",
            },
        },
    },
}

