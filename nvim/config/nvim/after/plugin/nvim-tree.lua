vim.opt.termguicolors = true
local api = require("nvim-tree.api")

local function global_opts()
	return { desc = "nvim-tree: Toggle", noremap = true, silent = true, nowait = true }
end

vim.keymap.set('n', '<C-n>', api.tree.toggle, global_opts())

local function my_on_attach(bufnr)
	local function opts(desc)
		return { desc =  "nvim-tree: " .. desc, buffer = bufnr, noremap = true,
		silent = true, nowait = true }
	end
	api.config.mappings.default_on_attach(bufnr)
	vim.keymap.set('n', '?', api.tree.toggle_help, opts('Help'))
	vim.keymap.set('n', '<C-n>', api.tree.toggle, opts('Toggle'))
end

require("nvim-tree").setup({
	renderer = {
		icons = {
			web_devicons = {
				file = {
					enable = false
				},
				folder = {
					enable = false
				}
			},
			show = {
				file = true,
				folder = true,
				folder_arrow = true,
				git = true,
				modified = true
			},
			glyphs = {
				default = "f",
				symlink = "s",
				bookmark = "b",
				modified = "m",
				folder = {
					arrow_closed = ">",
					arrow_open = "v",
					default = "d",
					open = "d",
					empty = "d",
					empty_open = "d",
					symlink = "ds",
					symlink_open = "ds"
				},
				git = {
					unstaged = "us",
					staged = "s",
					unmerged = "um",
					renamed = "r",
					untracked = "u",
					deleted = "d",
					ignored = "i"
				}
			}
		}
	},
	on_attach = my_on_attach,
    sync_root_with_cwd = true,
    update_focused_file = {
        enable = true,
        update_root = true
    },
    actions = {
        open_file = {
            quit_on_open = true
        }
    }
})

