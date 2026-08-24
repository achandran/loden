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
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "loden-night",
    },
  },
  {
    "nvim-lualine/lualine.nvim",
    opts = {
      options = { theme = "loden-night" },
    },
  },
}
