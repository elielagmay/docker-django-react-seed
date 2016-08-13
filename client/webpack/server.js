import webpack  from 'webpack';
import WebpackDevServer from 'webpack-dev-server';
import config  from './config.dev';

new WebpackDevServer(webpack(config), {
    publicPath: config.output.publicPath,
    filename: config.output.filename,
    inline: true,
    hot: true,
    stats: false,
    historyApiFallback: true,
    headers: {
        'Access-Control-Allow-Origin': 'http://localhost:8000/',
        'Access-Control-Allow-Headers': 'X-Requested-With'
    }
}).listen(9000, '0.0.0.0', function (err) {
    if (err) {
        console.error(err);
    } else {
        console.log('webpack dev server listening on http://localhost:9000');
    }
});
