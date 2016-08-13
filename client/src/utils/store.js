import { routerMiddleware } from 'react-router-redux';
import { applyMiddleware, compose, createStore } from 'redux';
import createLogger from 'redux-logger';
import thunk from 'redux-thunk';
import appReducer from '../app/reducers';

export const configureStore = (initialState, history) => {
    const logger = createLogger();
    const reduxRouterMiddleware = routerMiddleware(history);
    const middleware = applyMiddleware(thunk, logger, reduxRouterMiddleware);
    const createStoreWithMiddleware = compose(middleware);
    const store = createStoreWithMiddleware(createStore)(appReducer, initialState);
    return store;
};

export const dataStorage = {
    get: (key) => {
        return localStorage.getItem(key);
    },
    set: (key, value) => {
        return localStorage.setItem(key, value);
    },
    unset: (key) => {
        return localStorage.removeItem(key);
    },
    clear: () => {
        return localStorage.clear();
    }
};
