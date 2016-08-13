import base_config from './config.base';
import webpack from 'webpack';

export default {
    ...base_config,
    debug: true,
    output: {
        ...base_config.output,
        publicPath: 'http://localhost:9000' + base_config.output.publicPath,
        filename: 'bundle.js'
    },
    entry: [
        'webpack-dev-server/client?http://0.0.0.0:9000',
        'webpack/hot/dev-server',
        ...base_config.entry
    ],
    plugins: [
        ...base_config.plugins,
        new webpack.HotModuleReplacementPlugin(),
        new webpack.DefinePlugin({
            '__DEV__': true,
            'process.env': JSON.stringify('development')
        })
    ]
};
