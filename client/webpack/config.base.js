import webpack from 'webpack';

export default {
    entry: [
        '/project/client/src/index.js'
    ],
    devtool: 'source-map',
    output: {
        path: '/project/client/dist/',
        publicPath: '/static/',
    },
    module: {
        loaders: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel',
            },
            {
                test: /\.json$/,
                loader: 'json',
            },
            {
                test: /\.css$/,
                loader: 'style!css'
            },
            {
                test: /\.styl$/,
                loader: 'style!css!stylus'
            },
            {
                test: /\.(mp4|webm|mp3|ogg|wav|jpeg|jpg|bmp|ico|png|gif|ttf|otf|woff|eot)$/,
                loader: 'file?name=[path][name].[ext]?[hash]'
            }
        ]
    },
    target: 'web',
    plugins: [
        new webpack.NoErrorsPlugin()
    ]
};
