import { routerMiddleware } from 'react-router-redux';
import { applyMiddleware, compose, createStore } from 'redux';
import createLogger from 'redux-logger';
import thunk from 'redux-thunk';
import appReducer from './app/reducers';

export const configureStore = (initialState, history) => {
    const logger = createLogger();
    const reduxRouterMiddleware = routerMiddleware(history);
    const middleware = applyMiddleware(thunk, logger, reduxRouterMiddleware);
    const createStoreWithMiddleware = compose(middleware);
    return createStoreWithMiddleware(createStore)(appReducer, initialState);
};
