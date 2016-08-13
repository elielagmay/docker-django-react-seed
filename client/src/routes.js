import React from 'react';
import { Route, IndexRoute } from 'react-router';
import App from './app/App';
import IndexPage from './app/IndexPage';
import NotFoundErrorPage from './app/NotFoundErrorPage';

export default(
    <Route path="/" component={App}>
        <IndexRoute component={IndexPage}/>
        <Route path="*" component={NotFoundErrorPage}/>
    </Route>
);
