module.exports = {
    devServer: {
        proxy: {
            "/v1/*": {
                target: "https://tohru.bednarski.dev/",
                secure: false,
                changeOrigin: true
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
