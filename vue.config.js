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
            globDirectory: "/",
            globPatterns: ["**/*.{css,html,js,png}"],
            swSrc: "public/service-worker.js",
        }
    }
};
