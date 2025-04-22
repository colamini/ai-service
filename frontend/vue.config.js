module.exports = {
    chainWebpack: config => {
        config.module
            .rule('vue')
            .use('vue-loader')
            .tap(options => {
                options.compilerOptions = options.compilerOptions || {}
                options.compilerOptions.isCustomElement = tag => {
                    return tag === 'vue-advanced-chat' || tag === 'emoji-picker'
                }
                return options
            })
    }
}