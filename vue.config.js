module.exports = {
    devServer: {
        proxy: {
            "/v1/*": {
                target: "https://tohru.sylvanas.dream/",
                secure: false
            }
        }
    },
    pwa: {
        workboxPluginMode: "InjectManifest",
        workboxOptions: {
            swSrc: "public/service-worker.js",
        }
    }
};
