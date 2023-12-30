-- This file can be loaded by calling `lua require('plugins') from your init.vim

-- Only required if you have packer configured as `opt`
vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function(use)
	-- Packer can manage itself
	use 'wbthomason/packer.nvim'
	use {
		'williamboman/mason.nvim',
		config = function()
			require('mason').setup()
		end
	}
	use {
		'nvim-telescope/telescope.nvim', tag = '0.1.0',
		requires = { {'nvim-lua/plenary.nvim'} }
	}
	use {
		'rose-pine/neovim',
		as = 'rose-pine',
		config = function()
			vim.cmd('colorscheme rose-pine')
		end
	}
	use('nvim-treesitter/nvim-treesitter', {run = ':TSUpdate'})
	use('mbbill/undotree')
	use('tpope/vim-fugitive')
	use {
	  'VonHeikemen/lsp-zero.nvim',
	  branch = 'v2.x',
	  requires = {
	    -- LSP Support
	    {'neovim/nvim-lspconfig'},             -- Required
	    {'williamboman/mason.nvim'},           -- Optional
	    {'williamboman/mason-lspconfig.nvim'}, -- Optional

	    -- Autocompletion
	    {'hrsh7th/nvim-cmp'},     -- Required
	    {'hrsh7th/cmp-nvim-lsp'}, -- Required
	    {'L3MON4D3/LuaSnip'},     -- Required
	  }
	}
	use('nvim-tree/nvim-tree.lua')
    use('nvim-lualine/lualine.nvim')
    use('ahmedkhalf/project.nvim')
    use('sunjon/shade.nvim')
    use('askfiy/visual_studio_code')
    use({
        'utilyre/barbecue.nvim',
        tag = '*',
        requires = {
            'SmiteshP/nvim-navic'
        }
    })
    use('yamatsum/nvim-cursorline')
    use('nvim-orgmode/orgmode')
    use('petertriho/nvim-scrollbar')
    use('windwp/nvim-autopairs')
    use('ethanholz/nvim-lastplace')
end)

