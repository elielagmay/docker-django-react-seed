import 'babel-polyfill';
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { Router, browserHistory } from 'react-router';
import { syncHistoryWithStore } from 'react-router-redux';
import { configureStore } from './store';
import routes from './routes';
import './ui/index.styl';

const store = configureStore({}, browserHistory);
const history = syncHistoryWithStore(browserHistory, store);

const target = document.getElementById('root');
const node = (
    <Provider store={store}>
        <Router history={history}>
            {routes}
        </Router>
    </Provider>
);

ReactDOM.render(node, target);
