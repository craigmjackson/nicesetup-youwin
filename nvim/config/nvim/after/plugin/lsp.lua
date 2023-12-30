local lsp = require("lsp-zero")
lsp.preset("recommended")
lsp.ensure_installed({
	'bashls',
	'cssls',
	'docker_compose_language_service',
	'eslint',
	'html',
	'jsonls',
	'lua_ls',
	'powershell_es',
	'pylsp',
	'tsserver',
	'volar',
	'yamlls'
})
local cmp = require('cmp')
local cmp_select = {behavior = cmp.SelectBehavior.Select}
local cmp_mappings = lsp.defaults.cmp_mappings({
    ['<Left>'] = cmp.mapping.scroll_docs(-4),
    ['<Right>'] = cmp.mapping.scroll_docs(4),
	['<C-p>'] = cmp.mapping.select_prev_item(cmp_select),
	['<C-n>'] = cmp.mapping.select_next_item(cmp_select),
	['<cr>'] = cmp.mapping.confirm({ select = true }),
	["<C-Space>"] = cmp.mapping.complete(),
})
lsp.setup_nvim_cmp({
	mapping = cmp_mappings
})
lsp.setup()

