import jsdom from 'jsdom';

const doc = jsdom.jsdom('<div id="root"></div>');
const win = doc.defaultView;

global.document = doc;
global.window = win;
global.navigator = global.window.navigator;
