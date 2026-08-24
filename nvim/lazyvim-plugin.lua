-- Copy this spec into your LazyVim plugins directory while developing Loden.
return {
  {
    dir = "/Users/anand/code/loden/nvim",
    name = "loden.nvim",
    dependencies = { "webhooked/kanso.nvim" },
    lazy = false,
    priority = 1000,
    opts = {
      bold = true,
      italics = true,
    },
  },
  {
    "cormacrelf/dark-notify",
    config = function()
      require("dark_notify").run({
        schemes = {
          light = { colorscheme = "loden" },
          dark = { colorscheme = "loden-night" },
        },
      })
    end,
  },
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "loden",
    },
  },
  {
    "nvim-lualine/lualine.nvim",
    opts = function(_, opts)
      opts.options = opts.options or {}
      opts.options.theme = vim.g.colors_name == "loden-night" and "loden-night" or "loden-day"
    end,
  },
}
